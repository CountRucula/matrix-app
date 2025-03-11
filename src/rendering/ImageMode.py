from rendering.RenderMode import RenderMode
import numpy as np
from PIL import Image
import logging
import time

class ImageMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width,height)

        super().reset()

    def render(self):
        return self.framebuffer

    def open_image(self, path: str):
        try:
            with Image.open(path) as img:
                self.set_image(img)
        except Exception as e:
            logging.error(f"can't load image: {e}")

    def reset(self):
        pass

    def set_image(self, img: Image.Image):
        img_ratio = img.height / img.width
        matrix_ratio = self.height / self.width

        # img_ratio
        # bigger  -> more of a portrait  (scale to matrix height)
        # smaller -> more of a landscape (scale to matrix width)
        if img_ratio > matrix_ratio:
            height = self.height
            width = int(height / img_ratio)
        else:
            width = self.width
            height = int(img_ratio * width)

        # resize & convert to RGB mode
        img = img.resize((width, height), resample=Image.Resampling.BICUBIC).convert("RGB")
        pixels = np.array(img)

        x_offset = self.width  // 2
        y_offset = self.height // 2

        x_start = x_offset-width//2
        y_start = y_offset-height//2

        super().reset()
        self.framebuffer[y_start:y_start+height, x_start:x_start+width] = pixels

class GifMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width,height)
        super().reset()

        self.start = time.time()
        self.idx = 0
        self.n_frames = 0

    def render(self):
        if self.n_frames == 0:
            return np.zeros((self.height, self.width, 3), np.uint8)

        if self.n_frames == 1:
            return self.frames[0][0]

        elapsed = (time.time() - self.start) * 1000

        if elapsed >= self.frames[self.idx][1]:
            self.idx = (self.idx + 1) % self.n_frames
            self.start = time.time()

        return self.frames[self.idx][0]

    def open_img(self, path: str):
        try:
            with Image.open(path) as img:
                self.set_img(img)
        except Exception as e:
            logging.error(f"can't load image: {e}")

    def reset(self):
        self.idx = 0
        self.start = time.time()

    def set_img(self, img: Image.Image):
        self.n_frames = 0
        new_frames = []

        x_offset = self.width  // 2
        y_offset = self.height // 2

        while True:
            resized_img = self.resize_frame(img)
            pixels = np.array(resized_img)

            duration = img.info.get('duration', 50)  # Duration in milliseconds

            x_start = x_offset-resized_img.width//2
            y_start = y_offset-resized_img.height//2

            frame = np.zeros((self.height, self.width, 3), np.uint8)
            frame[y_start:y_start+resized_img.height, x_start:x_start+resized_img.width] = pixels

            new_frames.append((frame, duration))

            try:
                img.seek(img.tell() + 1)
            except EOFError:
                break

        self.frames = new_frames
        self.n_frames = len(self.frames)
        self.reset()


    def resize_frame(self, img: Image.Image) -> Image.Image:
        img_ratio = img.height / img.width
        matrix_ratio = self.height / self.width

        # img_ratio
        # bigger  -> more of a portrait  (scale to matrix height)
        # smaller -> more of a landscape (scale to matrix width)
        if img_ratio > matrix_ratio:
            height = self.height
            width = int(height / img_ratio)
        else:
            width = self.width
            height = int(img_ratio * width)

        # resize & convert to RGB mode
        img = img.resize((width, height), resample=Image.Resampling.BICUBIC).convert("RGB")

        return img
