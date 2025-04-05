from construct import Struct, Byte, Array, PrefixedArray, Int16ul, Float32b, Enum
import numpy as np
import enum
from typing import Literal

from com.Format import SerialFormat, EnumAdapter

class ControllerCommands(enum.Enum):
    GetPotiPos          = 0x10
    CalibratePoti       = 0x11

    GetBtnState         = 0x20
    GetBtnEvent         = 0x21

    GetJoystickState    = 0x30
    GetJoystickEvent    = 0x31

class ButtonState(enum.Enum):
    Pressed  = 0x00
    Released = 0x02

class ButtonEvent(enum.Enum):
    No      = 0x00
    Press   = 0x01
    Release = 0x02

class JoystickState(enum.Enum):
    Middle  = 0x01
    Left    = 0x02
    Right   = 0x03
    Top     = 0x04
    Bottom  = 0x05

class JoystickEvent(enum.Enum):
    No          = 0x00
    ToMiddle    = 0x01
    ToLeft      = 0x02
    ToRight     = 0x03
    ToTop       = 0x04
    ToBottom    = 0x05

POTI_NRS = Literal[0, 1]

class ControllerFormat(SerialFormat):
    def __init__(self):
        self.commands = ControllerCommands
        super().__init__()

    def create_tables(self) -> None:
        super().create_tables()

        self.command_table.update({
            self.commands.GetPotiPos: Struct(
                "poti_nr" / Byte
            ),
            self.commands.CalibratePoti: Struct(
                "poti_nr" / Byte,
                "cal_type" / Byte
            ),
            self.commands.GetBtnState: Struct(),
            self.commands.GetBtnEvent: Struct(),
            self.commands.GetJoystickState: Struct(),
            self.commands.GetJoystickEvent: Struct(),
        })

        self.response_table.update({
            self.commands.GetPotiPos: Struct(
                "poti_nr" / Byte,
                "poti_pos" / Float32b
            ),
            self.commands.CalibratePoti: Struct(),
            self.commands.GetBtnState: Struct(
                "state" / EnumAdapter(Enum(Byte, ButtonState), ButtonState)
            ),
            self.commands.GetBtnEvent: Struct(
                "event" / EnumAdapter(Enum(Byte, ButtonEvent), ButtonEvent)
            ),
            self.commands.GetJoystickState: Struct(
                "state" / EnumAdapter(Enum(Byte, JoystickState), JoystickState)
            ),
            self.commands.GetJoystickEvent: Struct(
                "event" / EnumAdapter(Enum(Byte, JoystickEvent), JoystickEvent)
            ),
        })

    def build_cmd_get_poti_pos(self, poti_nr: POTI_NRS) -> bytes:
        return self.command_builder.build( self.commands.GetPotiPos, dict(poti_nr = poti_nr))

    def build_cmd_calibrate_poti_max(self, poti_nr: POTI_NRS) -> bytes:
        return self.command_builder.build( self.commands.CalibratePoti, dict(poti_nr = poti_nr, cal_type=0))

    def build_cmd_calibrate_poti_min(self, poti_nr: POTI_NRS) -> bytes:
        return self.command_builder.build( self.commands.CalibratePoti, dict(poti_nr = poti_nr, cal_type=1))
    
    def build_cmd_get_btn_state(self) -> bytes:
        return self.command_builder.build(self.commands.GetBtnState)

    def build_cmd_get_btn_event(self) -> bytes:
        return self.command_builder.build(self.commands.GetBtnEvent)

    def build_cmd_get_joystick_event(self) -> bytes:
        return self.command_builder.build(self.commands.GetJoystickEvent)

    def build_cmd_get_joystick_state(self) -> bytes:
        return self.command_builder.build(self.commands.GetJoystickState)

    def get_poti_pos(self, data: dict) -> tuple[int, float]:
        return data.poti_nr, data.poti_pos

    def get_btn_state(self, data: dict) -> ButtonState:
        return data.state

    def get_btn_event(self, data: dict) -> ButtonEvent:
        return data.event

    def get_joystick_state(self, data: dict) -> JoystickState:
        return data.state

    def get_joystick_event(self, data: dict) -> JoystickEvent:
        return data.event 
