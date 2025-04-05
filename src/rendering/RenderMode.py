from abc import ABC, abstractmethod
import numpy as np

class RenderMode(ABC):
    def __init__(self, width, height):
        self.params = {}

        self.width = width
        self.height = height

        self.clear()

    @abstractmethod
    def render(self):
        pass

    def set_pixel(self, col, row, color: np.ndarray, buffer: np.ndarray | None = None):
        buffer = buffer if buffer is not None else self.framebuffer

        if 0 <= col < buffer.shape[1] and 0 <= row < buffer.shape[0]:
            buffer[row, col] = np.array(color, np.uint8)

    def add_pixel(self, col ,row, color: np.ndarray, buffer: np.ndarray | None = None):
        buffer = buffer if buffer is not None else self.framebuffer

        if 0 <= col < buffer.shape[1] and 0 <= row < buffer.shape[0]:
            buffer[row,col] = np.clip(buffer[row, col] + np.array(color, np.uint8), a_max=255, a_min=0)

    def draw_line(self, x0, y0, x1, y1, color, buffer: np.ndarray | None = None):
        """Draw an antialiased line using Xiaolin Wu's algorithm."""
        steep = abs(y1 - y0) > abs(x1 - x0)
        
        # Swap x and y if the line is steep
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        # Swap start and end points if necessary
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        
        dx = x1 - x0
        dy = y1 - y0
        m = dy / dx if dx != 0 else 1.0

        # handle start point
        overlap = 1 - ((x0 + 0.5) - int(x0 + 0.5))
        dist_start = y0 - int(y0)

        if steep:
            self.add_pixel(int(y0), int(x0 + 0.5), (1-dist_start)*overlap*color, buffer)
            self.add_pixel(int(y0) + 1, int(x0 + 0.5), dist_start*overlap*color, buffer)
        else:
            self.add_pixel(int(x0 + 0.5), int(y0), (1-dist_start)*overlap*color, buffer)
            self.add_pixel(int(x0 + 0.5), int(y0) + 1, dist_start*overlap*color, buffer)

        # handle end point
        overlap = (x1 - 0.5) - int(x1 - 0.5)
        dist_end = y1 - int(y1)

        if steep:
            self.add_pixel(int(y1), int(x1 + 0.5), (1-dist_end)*overlap*color, buffer)
            self.add_pixel(int(y1) + 1, int(x1 + 0.5), dist_end*overlap*color, buffer)
        else:
            self.add_pixel(int(x1 + 0.5), int(y1), (1-dist_end)*overlap*color, buffer)
            self.add_pixel(int(x1 + 0.5), int(y1) + 1, dist_end*overlap*color, buffer)
        
        # points inbetween
        y = y0
        for x in range(int(x0+1), int(x1)):
            y_lower = int(y)
            y_upper = int(y) + 1

            c_lower = color*(y_upper-y)
            c_upper = color*(y-y_lower)

            if steep:
                self.add_pixel(y_lower, x, c_lower, buffer)
                self.add_pixel(y_upper, x, c_upper, buffer)
            else:
                self.add_pixel(x, y_lower, c_lower, buffer)
                self.add_pixel(x, y_upper, c_upper, buffer)

            y += m

    def set_param(self, **kwargs):
        for key, val in kwargs.items():
            self.params[key] = val

    def set_size(self, width, height):
        self.width = width
        self.height = height

        self.clear()

    def reset(self):
        self.clear()

    def clear(self):
        self.framebuffer = np.zeros((self.height, self.width, 3))