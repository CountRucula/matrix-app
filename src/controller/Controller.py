from com.Link import SerialLink
from com.Device import Device
from com.Format import DeviceType

from controller.Format import ControllerFormat, POTI_NRS, ButtonEvent, ButtonState, JoystickState, JoystickEvent

class Controller(Device):
    def __init__(self):
        self.fw_version = ""

        self.format = ControllerFormat()
        self.link = SerialLink()
    
    def list_controllers(self) -> list[str]:
        device = self.list_devices()
        return [dev for dev in device if dev[1] == DeviceType.Controller]

    def calibrate_poti_min(self, poti_nr: POTI_NRS):
        if self.link.connected:
            raw = self.format.build_cmd_calibrate_poti_min(poti_nr)
            self.link.SendFrame(raw)

    def calibrate_poti_max(self, poti_nr: POTI_NRS):
        if self.link.connected:
            raw = self.format.build_cmd_calibrate_poti_max(poti_nr)
            self.link.SendFrame(raw)

    def get_poti_pos(self, poti_nr: POTI_NRS) -> tuple[int, float]:
        if self.link.connected:
            raw = self.format.build_cmd_get_poti_pos(poti_nr)
            cmd, data = self.send_and_receive(raw, 1.0)

            if cmd is None or data is None:
                return None

            return self.format.get_poti_pos(data)[1]
    
    def get_btn_state(self) -> ButtonState:
        if self.link.connected:
            raw = self.format.build_cmd_get_btn_state()
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_btn_state(data)

    def get_btn_event(self) -> ButtonEvent:
        if self.link.connected:
            raw = self.format.build_cmd_get_btn_event()
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_btn_event(data)

    def get_joystick_state(self) -> JoystickState:
        if self.link.connected:
            raw = self.format.build_cmd_get_joystick_state()
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_joystick_state(data)

    def get_joystick_event(self) -> JoystickEvent:
        if self.link.connected:
            raw = self.format.build_cmd_get_joystick_event()
            cmd, data = self.send_and_receive(raw)

            if cmd is None or data is None:
                return None

            return self.format.get_joystick_event(data)