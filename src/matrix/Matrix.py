from com.Link import SerialLink
from com.Device import Device
from com.Format import DeviceType

from matrix.Format import MatrixFormat, MatrixCommands
import numpy as np

class Matrix(Device):
    def __init__(self):
        self.width = None
        self.heigth = None

        self.fw_version = ""

        self.set_gamma({})
        self.set_color_scale({})

        self.format = MatrixFormat()
        self.link = SerialLink()
        
    def set_gamma(self, gamma: dict):
        self.gamma_red = gamma.get('red', 2.2)
        self.gamma_green = gamma.get('green', 2.2)
        self.gamma_blue = gamma.get('blue', 2.2)
        
    def set_color_scale(self, scale: dict):
        self.scale = np.array((scale.get('red', 1.0), scale.get('green', 1.0), scale.get('blue', 1.0)), float)
    
    def list_matrices(self, devices: list[tuple[str, DeviceType]] = None) -> list[str]:
        if devices is None:
            devices = self.list_devices()

        return [dev[0] for dev in devices if dev[1] == DeviceType.Matrix]

    def disconnect(self):
        self.link.ClearSendQueue()
        self.clear_frame()
        return super().disconnect()

    def get_size(self) -> tuple[int, int]:
        if self.link.connected:
            raw = self.format.build_cmd_get_size()
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            self.width, self.heigth = self.format.get_size(data)

            return self.width, self.heigth

    def clear_frame(self) -> None:
        if self.link.connected:
            raw = self.format.build_cmd_clr_frame()
            self.link.SendFrame(raw)

    def apply_gamma_correction(self, data: np.ndarray):
        data = data.astype(dtype=float)

        data[..., 0] = np.array((data[..., 0]/255.0)**self.gamma_red   * 255)
        data[..., 1] = np.array((data[..., 1]/255.0)**self.gamma_green * 255)
        data[..., 2] = np.array((data[..., 2]/255.0)**self.gamma_blue  * 255)

        return data

    def display(self, data: np.ndarray):
        """Displays a frame on the matrix
        
        The data get gamma corrected to allow for somewhat correct colors. 

        Also the data gets reorganised from

        0======================> <br>
        =======================> <br>
        =======================> <br>
        =======================> <br>
        
        to 

        =======================> <br>
        <======================= <br>
        =======================> <br>
        <======================0 <br>

        Args:
            data (np.ndarray): led data with shape (height, width, 3)
        """
        if self.link.connected:
            data = self.apply_gamma_correction(data) * self.scale
            data[::2] = data[::2, ::-1] # flip every 2nd row
            data[:] = data[::-1] # flip y

            data = data.reshape(-1, data.shape[-1])  # flatten data (rows, cols, 3) => (rows*cols, 3)
            raw = self.format.build_cmd_set_frame(data.astype(dtype=np.uint8))
            self.link.SendFrame(raw)
