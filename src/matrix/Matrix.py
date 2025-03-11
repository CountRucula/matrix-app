from matrix.MatrixLink import MatrixLink
from matrix.MatrixFormat import MatrixFormat, MatrixCommands
from ui.LEDMatrix import LEDMatrixWidget
import numpy as np
import time

class Matrix:
    def __init__(self):
        self.width = None
        self.heigth = None

        self.preview = None

        self.fw_version = ""

        self.link = MatrixLink()

    def SetPreview(self, preview: LEDMatrixWidget):
        self.preview = preview

    def ListMatrices(self) -> list[str]:
        devices = self.link.ListDevices()
        matrices = []

        for dev in devices:
            valid = self.TestConnection(dev)

            if valid:
                matrices.append(dev)

        return matrices

    def TestConnection(self, dev: str) -> bool:
        try:
            self.link.Connect(dev)

            version = self.GetFwVersion(0.05)

            self.link.Disconnect()

            return version is not None

        except Exception:
            return False


    def Connect(self, dev: str):
        self.link.Connect(dev)

    def Disconnect(self):
        self.link.Disconnect()

    def SendAndWait(self, raw: bytes, timeout: float | None = None) -> tuple[MatrixCommands, dict]:
        start = time.time()

        self.link.SendFrame(raw)

        if timeout:
            while ((time.time() - start) < timeout) and not self.link.Available():
                time.sleep(0.01)

        else:
            while not self.link.Available():
                time.sleep(0.01)

        raw = self.link.GetFrame()

        if raw is None:
            return None, None

        frame = MatrixFormat.ParseFrame(raw)
        return MatrixFormat.GetResponseCmd(frame), MatrixFormat.GetResponseData(frame)

    def GetSize(self) -> tuple[int, int]:
        if self.link.connected:
            raw = MatrixFormat.BuildCmd_GetSize()
            cmd, data = self.SendAndWait(raw)

            self.width = data.width
            self.heigth = data.height

            return self.width, self.heigth

    def GetFwVersion(self, timeout: float | None = None) -> str:
        if self.link.connected:
            raw = MatrixFormat.BuildCmd_GetFwVersion()
            cmd, data = self.SendAndWait(raw, timeout)

            if cmd is None or data is None:
                return None

            self.fw_version = f'{data.major}.{data.minor}'

            return self.fw_version

    def ClearFrame(self) -> None:
        if self.link.connected:
            raw = MatrixFormat.BuildCmd_ClrFrame()
            self.link.SendFrame(raw)

    def SetBaudrate(self, baudrate: int) -> None:
        if self.link.connected:
            raw = MatrixFormat.BuildCmd_SetBaudrate(baudrate)
            self.link.SendFrame(raw)

            time.sleep(0.05)

            self.link.SetBaudRate(baudrate)

    def SendData(self, data: np.ndarray):
        if self.link.connected:
            raw = MatrixFormat.BuildData(data)
            self.link.SendFrame(raw)
