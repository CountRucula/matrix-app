from rendering.RenderMode import RenderMode
import time
import numpy as np
import random
from colorsys import hsv_to_rgb
from abc import abstractmethod

class WaveMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.f = 0.2
        self.waves = 2
        
        self.A = 0.8*self.height/2
        self.offset = self.height/2

        self.z = np.arange(width)

        self.update()

    def render(self):
        t = time.time() % self.window
        x, y = self.evaluate(self.k*self.z + self.b*t)
        y = self.A*y + self.offset

        self.clear()

        old_x = x[0]
        old_y = y[0]

        for x,y in zip(x[1:],y[1:]):
            self.draw_line(old_x, old_y, x, y, np.array((255,255,255), np.uint8))
            old_x = x
            old_y = y

        return self.framebuffer

    def update(self):
        self.wavelength = self.width / self.waves

        self.k = 2*np.pi/self.wavelength
        self.b = 2*np.pi*self.f

        self.window = self.width / self.f

    @abstractmethod
    def evaluate(self, phi) -> tuple[np.ndarray, np.ndarray]:
        pass

class SineWaveMode(WaveMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.f = 0.5
        self.update()

        self.x = np.arange(self.width)
        
    def evaluate(self, phi) -> tuple[np.ndarray, np.ndarray]:
        return self.x, np.sin(phi)


class SawtoothMode(WaveMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.f = 0.5
        self.update()
        
    def eval(self, phi):
        return phi/np.pi if phi < np.pi else phi/np.pi-2

    def evaluate(self, phi) -> tuple[np.ndarray, np.ndarray]:
        phi = phi[0] % (2*np.pi)

        y = [self.eval(phi)]
        x = [0]
        
        dphi = np.pi - phi if phi < np.pi else 3*np.pi - phi

        while x[-1] < self.width:
            x_new = x[-1] + dphi/self.k

            y.append(1) 
            x.append(x_new)
            y.append(-1) 
            x.append(x_new)
        
            dphi = 2*np.pi

        y = np.array(y)
        x = np.array(x)
        return x, y

class RectangularMode(WaveMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.f = 0.5
        self.update()

    def evaluate(self, phi) -> tuple[np.ndarray, np.ndarray]:
        phi = phi[0] % (2*np.pi)

        y = [-1 if phi < np.pi else 1]
        x = [0]
        
        while x[-1] < self.width:
            dphi = np.pi - (phi % np.pi)
            x_new = x[-1] + dphi/self.k

            y.append(y[-1]) 
            x.append(x_new)
            y.append(-y[-1]) 
            x.append(x_new)

            phi += dphi
        
        y = np.array(y)
        x = np.array(x)

        return x, y

class RaindropsMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.n = 20
        self.color = (30,145,206)
        self.f = 20

        self.start = time.time()

    def render(self):
        width = self.width
        height = self.height

        elapsed = time.time() - self.start

        if elapsed > (1.0 / self.f):
            self.start = time.time()
            for i in range(self.n):
                x = int(width * random.random())
                y = int(height * random.random())
                self.set_pixel(x, y, self.color)
                # turn off a random pixel
                x = int(width * random.random())
                y = int(height * random.random())
                self.set_pixel(x, y, (0,0,0))

        return self.framebuffer

class RainbowMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

    def render(self):
        width = self.width
        height = self.height

        t = time.time() / 2
        
        # move rainbow colors in 2d matrix
        for x in range(0, width):
            for y in range(0, height):
                hue = (float(x) / width) + (float(y) / height) + t
                hue = hue - int(hue)

                # Full saturation and brightness for vibrant colors
                rgb = np.array(hsv_to_rgb(hue, 1.0, 1.0)) * 255

                #r = int(127 * (np.sin(0.3 * (x + t)) + 1))
                #g = int(127 * (np.sin(0.3 * (y + t)) + 1))
                #b = int(127 * (np.sin(0.3 * (x + y + 2*t)) + 1))
                self.set_pixel(x, y, rgb)
        
        return self.framebuffer
