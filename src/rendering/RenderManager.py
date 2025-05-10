from threading import Thread
from rendering.RenderMode import RenderMode
from ui.LEDMatrix import LEDMatrixWidget
from matrix.Matrix import Matrix
import time
import numpy as np

class RenderManager:
    def __init__(self, width=50, height=20, fps=30, on_mode_changed=None, on_preview_mode_changed=None):
        self.width = width
        self.height = height

        self.fps = fps
        self.fps_mean = 0.0
        self.fps_list = []

        self.modes = {}

        self.active_mode: RenderMode | None = None
        self.preview_mode: RenderMode | None = None

        self.hardware_matrix: Matrix = None
        self.hardware_matrix_enabled = False
        self.virtual_matrix: LEDMatrixWidget = None

        self.on_mode_changed = on_mode_changed
        self.on_preview_mode_changed = on_preview_mode_changed
        
    def SetSize(self, width, height) -> None:
        self.width = width
        self.height = height

    def SetVirtualMatrix(self, matrix: LEDMatrixWidget):
        self.virtual_matrix = matrix

    def SetMatrix(self, matrix: Matrix):
        self.hardware_matrix = matrix

    def AddMode(self, name: str, mode: RenderMode) -> None:
        self.modes[name] = mode

    def GetModes(self) -> list[str]:
        return [str(key) for key in self.modes.keys()]

    def SelectMode(self, name: str) -> None:
        if name in self.modes:
            new_mode = self.modes[name]
            self.on_mode_changed(name)

            # if new mode is not started => start
            if new_mode not in [self.preview_mode, self.active_mode]:
                new_mode.start_mode()
                
            # if active mode is no longer required => stop
            if self.active_mode is not None and self.active_mode not in [self.preview_mode, new_mode]:
                self.active_mode.stop_mode()
                
            self.active_mode = new_mode
    
    def EnableMatrixOutput(self):
        self.hardware_matrix_enabled = True

    def DisableMarixOutput(self):
        self.hardware_matrix_enabled = False

    def ClearMode(self):
        self.active_mode = None
        self.on_mode_changed('-')

    def PreviewMode(self, name: str) -> None:
        if name in self.modes:
            new_mode = self.modes[name]
            self.on_preview_mode_changed(name)

            # if new mode is not started => start
            if new_mode not in [self.preview_mode, self.active_mode]:
                new_mode.start_mode()

            # if active mode is no longer required => stop
            if self.preview_mode is not None and self.preview_mode not in [self.preview_mode, new_mode]:
                self.preview_mode.stop_mode()
                
            self.preview_mode = new_mode


    def Start(self) -> None:
        self.running = True
        self.thread = Thread(target=self.RenderLoop, daemon=True)
        self.thread.start()

    def Stop(self) -> None:
        self.running = False
        self.thread.join()

    def GetFPS(self) -> float:
        return self.fps_mean

    def RenderLoop(self) -> None:
        frame_time = 1 / self.fps
        old_start_time = time.time() - frame_time

        while self.running:
            try:
                start_time = time.time()

                if self.active_mode:
                    buffer = self.active_mode.render()

                    if self.hardware_matrix and self.hardware_matrix_enabled:
                        self.hardware_matrix.display(buffer)
                    
                if self.preview_mode:
                    if self.preview_mode != self.active_mode:
                        buffer = self.preview_mode.render()
                        
                    if self.virtual_matrix:
                        self.virtual_matrix.display(buffer)

                self.fps_list.append(1/(start_time - old_start_time + 1e-6))

                if len(self.fps_list) > self.fps:
                    self.fps_list.pop(0)

                self.fps_mean = np.mean(self.fps_list)
                old_start_time = start_time

                elapsed = time.time() - start_time
                sleep_time = max(0, frame_time - elapsed)
                time.sleep(sleep_time)
            except Exception as e:
                print(e)
                self.running = False

