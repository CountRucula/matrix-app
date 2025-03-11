from rendering.RenderMode import RenderMode
import numpy as np
import pyaudio
import logging
from abc import abstractmethod

class MusicMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.max_peak = 1023
        self.frames = 1024
        self.rate = 48000

        self.stream = None

    def open_stream(self):
        try:
            self.stream = self.p.open(format=pyaudio.paInt16, channels=2, rate=self.rate, input=True, frames_per_buffer=self.frames)
        except Exception as e:
            logging.error(f"Audio device missing? {e}")
            self.stream = None

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()

    def callback(self, data, frame_count, time_info, status_flags):
        data = np.frombuffer(data, dtype=np.int16)

        peak = self.find_peak(data)
        self.draw_peak(peak)

        return (bytes(), pyaudio.paContinue)

    def find_peak(self, data: np.ndarray) -> float:
        peak = np.max(np.abs(data))
        peak = int(peak * self.max_peak / 2 ** 16)

        return peak

    def shift_left(self):
        self.framebuffer[:, :-1] = self.framebuffer[:, 1:]

    def shift_right(self):
        self.framebuffer[:, 1:] = self.framebuffer[:, :-1]

    @abstractmethod
    def draw_peak(self, peak: float, color):
        pass

    def render(self):
        return self.framebuffer

class TimelineMode(MusicMode):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw_peak(self, peak: float, color):
        self.shift_left()

        y_start = 0
        y_end = int(peak * self.matrix.height // self.sensitivity)

        self.framebuffer[y_start:y_end, -1] = color
        self.framebuffer[y_end:, -1]        = (0,0,0)

class FrequencyBandsMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

    def render(self):
        return self.framebuffer