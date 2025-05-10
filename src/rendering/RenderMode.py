from abc import ABC, abstractmethod
import numpy as np
from fonts import font_5x7
from PIL import Image
import logging

def load_img(path):
    try:
        with Image.open(path) as img:
            return np.array(img.convert('RGB'))
    except Exception as e:
        logging.error(f"can't load image: {e}")

def load_gif(path):
    try:
        with Image.open(path) as img:
            frames = []
            
            while True:
                duration = img.info.get('duration', 50)  # Duration in milliseconds
                
                frames.append((np.array(img.convert('RGB')), duration))
                try:
                    img.seek(img.tell() + 1)
                except EOFError:
                    break

            return frames
    except Exception as e:
        logging.error(f"can't load gif: {e}")

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
        for x in range(int(x0+1), int(x1+0.5)):
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
            
    def draw_text(self, text: str, pos: tuple[int, int], fg: np.ndarray, bg: np.ndarray = (0,0,0), font = font_5x7.Characters, hcenter = False, vcenter = False):
        x,y = pos
        
        # text -> bitmaps
        if text is not str:
            text = str(text)
            
        text = text.upper()
        bitmaps = np.array([font[c] for c in text])
        n, cH, cW = bitmaps.shape[:3]
        
        width = n*(cW+1)-1
        heigth = cH
        
        # center text if necessary
        if hcenter:
            x = (self.width - width)//2

        if vcenter:
            y = (self.height - heigth)//2
        
        # draw background
        if bg is not None:
            x1 = max(0, x-1)
            y1 = max(0, y-1)
            
            x2 = min(self.width-1,  x + width + 1)
            y2 = min(self.height-1, y + heigth + 1)
            
            self.framebuffer[y1:y2, x1:x2] = bg
        
        # draw text
        for bitmap in bitmaps:
            # stop if there is not enough space
            if not (0 <= x <= self.width-cW) or not (0 <= y <= self.height-cH):
                continue

            # draw onto framebuffer
            self.framebuffer[y:y+cH, x:x+cW] = np.einsum('ik,j->ikj', bitmap, fg)
            
            # new position
            x += cW + 1
 
    def set_param(self, **kwargs):
        for key, val in kwargs.items():
            self.params[key] = val

    def set_size(self, width, height):
        self.width = width
        self.height = height

        self.clear()

    def start_mode(self):
        self.clear()
        
    def stop_mode(self):
        self.clear()

    def clear(self):
        self.framebuffer = np.zeros((self.height, self.width, 3))