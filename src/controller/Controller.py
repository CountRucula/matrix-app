from com.Link import SerialLink
from com.Device import Device
from com.Format import DeviceType

from controller.Format import ControllerFormat, POTI_NRS, ButtonState, JoystickState, Event

class Controller(Device):
    def __init__(self):
        self.fw_version = ""

        self.format = ControllerFormat()
        self.link = SerialLink()

    def list_controllers(self, devices: list[tuple[str, DeviceType]] = None) -> list[str]:
        if devices is None:
            devices = self.list_devices()

        return [dev[0] for dev in devices if dev[1] == DeviceType.Controller]

    def calibrate_poti(self, poti_nr: POTI_NRS, poti_max: int, poti_min: int):
        if self.link.connected:
            raw = self.format.build_cmd_calibrate_poti(poti_nr, raw_max=poti_max, raw_min=poti_min)
            self.link.SendFrame(raw)

    def get_poti_pos(self, poti_nr: POTI_NRS) -> float:
        if self.link.connected:
            raw = self.format.build_cmd_get_poti_pos(poti_nr)
            cmd, data = self.send_and_receive(raw, 1.0)

            if cmd is None or data is None:
                return None

            return self.format.get_poti_pos(data)

    def get_poti_raw(self, poti_nr: POTI_NRS) -> int:
        if self.link.connected:
            raw = self.format.build_cmd_get_poti_raw(poti_nr)
            cmd, data = self.send_and_receive(raw, 1.0)

            if cmd is None or data is None:
                return None

            return self.format.get_poti_raw(data)
    
    def get_btn_state(self, btn: int) -> ButtonState:
        if self.link.connected:
            raw = self.format.build_cmd_get_btn_state(btn)
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_btn_state(data)

    def get_events(self) -> list[Event]:
        if self.link.connected:
            raw = self.format.build_cmd_get_events()
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_events(data)

    def get_joystick_state(self, stick: int) -> JoystickState:
        if self.link.connected:
            raw = self.format.build_cmd_get_joystick_state(stick)
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_joystick_state(data)