from threading import Thread
from rendering.RenderMode import RenderMode
from ui.LEDMatrix import LEDMatrixWidget
import time
import numpy as np

class RenderManager:
    def __init__(self, width=50, height=20, fps=30):
        self.width = width
        self.height = height

        self.fps = fps
        self.fps_mean = 0.0
        self.fps_list = []

        self.modes = {}

        self.active_mode: RenderMode | None = None
        self.preview_mode: RenderMode | None = None

        self.hardware_matrix = None
        self.virtual_matrix = None

    def SetSize(self, width, height) -> None:
        self.width = width
        self.height = height

    def SetVirtualMatrix(self, matrix: LEDMatrixWidget):
        self.virtual_matrix = matrix

    def AddMode(self, name: str, mode: RenderMode) -> None:
        self.modes[name] = mode

    def GetModes(self) -> list[str]:
        return [str(key) for key in self.modes.keys()]

    def SelectMode(self, name: str) -> None:
        if name in self.modes:
            self.active_mode = self.modes[name]

            if self.active_mode != self.preview_mode:
                self.active_mode.reset()

    def PreviewMode(self, name: str) -> None:
        if name in self.modes:
            self.preview_mode = self.modes[name]

            if self.preview_mode != self.active_mode:
                self.preview_mode.reset()

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

                    if self.hardware_matrix:
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

