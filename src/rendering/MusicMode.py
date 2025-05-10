from rendering.RenderMode import RenderMode, load_img, load_gif
import numpy as np
import pyaudio
import logging
from abc import abstractmethod
from pathlib import Path

class MusicMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.p = pyaudio.PyAudio()

        self.max_peak = 1023
        self.frames = 1024
        self.rate = 48000

        self.stream = None
        
    def start_mode(self):
        self.open_stream()
        
    def stop_mode(self):
        self.close_stream()

    def open_stream(self):
        try:
            self.stream = self.p.open(format=pyaudio.paInt16, channels=2, rate=self.rate, input=True, frames_per_buffer=self.frames, stream_callback=lambda *args, **kwargs: self.callback(*args, **kwargs))

        except Exception as e:
            logging.error(f"Audio device missing? {e}")
            self.stream = None

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()

    def callback(self, data, frame_count, time_info, status_flags):
        data = np.array(np.frombuffer(data, dtype=np.int16), dtype=float, copy=True)
        data = data.reshape((-1, 2))

        self.process_audio(data)

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
        
        self.frames = 8*1024

        self.f_range = [60, 15000]
        self.db_range = [-20, 50]

        self.new_f_range = [60, 15000]
        self.new_db_range = [-20, 50]
        
        self.spacing = 1

        self.bin_width = 2
        self.bins = self.width//self.bin_width

        assets = (Path(__file__).parent / '../../assets').resolve()
        self.colors = load_img(assets/'Bands-Colors.png')
        
    def set_a_max(self, a_max):
        self.new_db_range[1] = a_max
        
        if self.new_db_range[1] > self.new_db_range[0]:
            self.db_range = self.new_db_range.copy()
        
    def set_a_min(self, a_min):
        self.new_db_range[0] = a_min

        if self.new_db_range[1] > self.new_db_range[0]:
            self.db_range = self.new_db_range.copy()

    def set_f_max(self, f_max):
        self.new_f_range[1] = min(f_max, self.rate//2)
        
        if self.new_f_range[1] > self.new_f_range[0]:
            self.f_range = self.new_f_range.copy()
        
    def set_f_min(self, f_min):
        self.new_f_range[0] = f_min

        if self.new_f_range[1] > self.new_f_range[0]:
            self.f_range = self.new_f_range.copy()
        
    def set_bin_width(self, width):
        self.bin_width = width
        self.bins = int(np.ceil(self.width / (self.bin_width+self.spacing)))
        
    def set_spacing(self, spacing):
        self.spacing = spacing
        self.set_bin_width(self.bin_width)
        
    def log_frequency_bands(self, fft):
        # Create log-spaced frequency band edges
        band_edges = np.logspace(np.log10(self.f_range[0]), np.log10(self.f_range[1]), self.bins + 1)
        
        N = len(fft)
        
        # Convert to bin indices
        bands = []
        for i in range(self.bins):
            idx_start = round(band_edges[i]/self.rate*N)
            idx_end = round(band_edges[i+1]/self.rate*N)
            bands = fft[idx_start:idx_end]

        return bands

    def process_audio(self, data):
        N = data.shape[0]
        X = 20*np.log10(np.abs(np.fft.fft(data[:,0])) / N + 1e-6)
        
        bands = self.log_frequency_bands(X)
        intensities = np.array([np.mean(band) for band in bands])

        # clip and normalize to 0 - 1
        intensities = np.clip(intensities, *self.db_range)
        intensities = (intensities - self.db_range[0]) / (self.db_range[1] - self.db_range[0])
        
        for i, intensity in enumerate(intensities):
            self.draw_bin(i, intensity)
        
    def draw_bin(self, index: int, value: float):
        width = self.bin_width+self.spacing

        y_start =  self.height - int(value * self.height)
        x_start = width*index
        x_end = min(x_start+self.bin_width, self.width)

        self.framebuffer[y_start:, x_start:x_end] = self.colors[y_start:, x_start:x_end]
        self.framebuffer[:y_start, x_start:x_end] = (0,0,0)
        
        if x_end < self.width:
            spacing_start = x_end
            spacing_end = min(spacing_start + self.spacing, self.width)
            self.framebuffer[:, spacing_start:spacing_end] = (0,0,0)

    def render(self):
        return self.framebuffer