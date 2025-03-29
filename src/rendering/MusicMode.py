from rendering.RenderMode import RenderMode
import numpy as np
import pyaudio
import logging
from abc import abstractmethod
from scipy import signal

audio_client = None

class MusicMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.p = pyaudio.PyAudio()

        self.max_peak = 1023
        self.frames = 1024
        self.rate = 48000

        self.stream = None

    def open_stream(self):
        global audio_client

        if audio_client:
            audio_client.close_stream()
            audio_client = None

        try:
            self.stream = self.p.open(format=pyaudio.paInt16, channels=2, rate=self.rate, input=True, frames_per_buffer=self.frames, stream_callback=self.callback)

            audio_client = self

        except Exception as e:
            logging.error(f"Audio device missing? {e}")
            self.stream = None

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()

    @staticmethod
    def callback(data, frame_count, time_info, status_flags):
        global audio_client

        data = np.array(np.frombuffer(data, dtype=np.int16), dtype=float, copy=True)

        audio_client.process_audio(data)

        return (bytes(), pyaudio.paContinue)

    def find_peak(self, data: np.ndarray) -> float:
        peak = np.max(np.abs(data))
        peak = int(peak * (self.max_peak / 2 ** 16))

        return peak

    def shift_left(self):
        self.framebuffer[:, :-1] = self.framebuffer[:, 1:]

    def shift_right(self):
        self.framebuffer[:, 1:] = self.framebuffer[:, :-1]

    @abstractmethod
    def process_audio(self, data: np.ndarray):
        pass

    def render(self):
        return self.framebuffer

class TimelineMode(MusicMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.sensitivity = 75

    def process_audio(self, data: np.ndarray):
        peak = self.find_peak(data)
        self.draw_peak(peak, (255, 255, 255))

    def draw_peak(self, peak: float, color):
        self.shift_left()

        y_start =  self.height - int(peak * self.height // self.sensitivity)

        self.framebuffer[y_start:, -1] = color
        self.framebuffer[:y_start, -1] = (0,0,0)

class FrequencyBandsMode(MusicMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.start_freq = 60
        self.stop_freq = 20000

        self.bins = 6

        self.sensitivity = 75

    def process_audio(self, data):
        N = len(data)
        fs = self.rate

        df = fs/N
        X = np.abs(np.fft.fft(data)) / N

        start = int(self.start_freq / df)
        stop  = int(self.stop_freq  / df)

        bin_len = (stop - start)/self.bins

        for i, start in enumerate(np.arange(start, stop+1, bin_len)):
            m = np.mean(X[int(start):int(start+bin_len)]**2)

            self.draw_bin(i, m)

    def draw_bin(self, index: int, value: float):
        y_start =  self.height - int(value * self.height // self.sensitivity)
        x_start = self.width//self.bins*index
        x_end = self.width//self.bins*(index+1)

        self.framebuffer[y_start:, x_start:x_end] = (255,255,255)
        self.framebuffer[:y_start, x_start:x_end] = (0,0,0)

    def render(self):
        return self.framebuffer