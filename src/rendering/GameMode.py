from rendering.RenderMode import RenderMode
import numpy as np

class SnakeMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

    def render(self):
        return self.framebuffer