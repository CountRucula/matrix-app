from rendering.RenderMode import RenderMode
from typing import Literal
import numpy as np

ColorChannel = Literal['red', 'green', 'blue']

class TestGammaMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.gamma = 2.2
        self.set_color('red')

    def set_gamma(self, gamma: float):
        self.gamma = gamma
        self.draw()

    def set_color(self, channel: ColorChannel):
        if channel == 'red':
            self.color = np.array((255,0,0))
        elif channel == 'green':
            self.color = np.array((0,255,0))
        elif channel == 'blue':
            self.color = np.array((0,0,255))

        self.draw()

    def draw(self):
        brightness = np.linspace(0, 1, self.width, dtype=float)

        self.framebuffer[:self.height//2, :] = np.outer(brightness, self.color)
        self.framebuffer[self.height//2:, :] = np.outer(brightness**self.gamma, self.color)

    def render(self):
        return self.framebuffer

    def start_mode(self):
        pass

class TestScaleMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.set_scale(dict())

    def set_scale(self, scale: dict):
        self.scale = np.array((scale.get('red', 1.0), scale.get('green', 1.0), scale.get('blue', 1.0)), float)
        self.draw()

    def draw(self):
        brightness = np.linspace(0, 1, self.width, dtype=float)
        self.framebuffer[:, :] = np.outer(brightness, self.scale * np.array((255,255,255)))

    def render(self):
        return self.framebuffer

    def start_mode(self):
        self.draw()