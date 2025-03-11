import sys
from pathlib import Path

src_path = (Path(__file__).parent / '../src').resolve()
sys.path.append(str(src_path))

from matrix.Matrix import Matrix
from matrix.MatrixFormat import MatrixFormat, MatrixCommands
import numpy as np
import time
import serial

def create_rainbow_effect(num_leds: int = 10):
    def wheel(pos):
        pos = pos % 256
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)

    rainbow = np.array([
        wheel((i * 256 // num_leds) + (int(time.time() * 100) % 256))
        for i in range(num_leds)
    ], dtype=np.uint8)

    return rainbow

def create_chase_effect(num_leds: int = 10):
    def wheel(pos):
        pos = pos % 256
        if pos < 62:
            brightness = 255 - pos*4
        elif pos < 193:
            brightness = 0
        else:
            pos -= 193
            brightness = pos*4
        return (brightness, brightness, brightness)


    chase = np.array([
        wheel((i * 256 // (2*num_leds)) + (int(time.time() * 100) % 256))
        for i in range(num_leds)
    ], dtype=np.uint8)

    return chase

if __name__ == '__main__':
    try:
        matrix = Matrix()

        devices = matrix.ListMatrices()
        print(devices)

        time.sleep(1)

        if len(devices):
            matrix.Connect(devices[0])

            width, height = matrix.GetSize()
            print(f'width = {width}, height = {height}')

            matrix.SetBaudrate(1000000)

            version = matrix.GetFwVersion()
            print(f'matrix v{version}')

            start = time.time()
            duration = 1000
            while (time.time() - start) < duration:
                led_data = create_rainbow_effect()
                matrix.SendData(led_data) 
                time.sleep(0.05)

            time.sleep(1)

            matrix.ClearFrame()

            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        matrix.Disconnect()