from com.Format import SerialFormat, GenericCommands, DeviceType
from com.Link import SerialLink
import time

class Device:
    def __init__(self):
        self.fw_version = ""

        self.format = SerialFormat()
        self.link = SerialLink()
    
    def list_devices(self) -> list[tuple[str, DeviceType]]:
        devices = self.link.ListDevices()
        valid_devices = []

        for dev in devices:
            devtype = self.test_connection(dev)

            if devtype is not None:
                valid_devices.append((dev, devtype))

        return valid_devices

    def test_connection(self, dev: str) -> DeviceType:
        try:
            self.link.Connect(dev)

            devtype = self.get_device_type(0.2)
            
            self.link.Disconnect()

            return devtype

        except Exception:
            return None

    def port(self):
        if self.link.connected:
            return self.link.serial.port
        
        return None

    def connected(self):
        return self.link.connected
    
    def connect(self, dev: str):
        self.link.Connect(dev)

    def disconnect(self):
        self.link.Disconnect()

    def send_and_receive(self, raw: bytes, timeout: float | None = None) -> tuple[GenericCommands, dict]:
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

        _, payload = self.format.parse(raw)

        return self.format.get_response(payload)

    def get_fw_version(self, timeout: float | None = None) -> str:
        if self.link.connected:
            raw = self.format.build_cmd_get_fw_version()
            cmd, data = self.send_and_receive(raw, timeout)

            if cmd is None or data is None:
                return None

            major, minor = self.format.get_fw_version(data)
            return f'{major}.{minor}'
        
        return None

    def get_device_type(self, timeout: float | None = None) -> str:
        if self.link.connected:
            raw = self.format.build_cmd_get_device_type()
            cmd, data = self.send_and_receive(raw, timeout)

            if cmd is None or data is None:
                return None

            return self.format.get_device_type(data)

        return None


