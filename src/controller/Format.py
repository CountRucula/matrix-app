from construct import Struct, Byte, Array, PrefixedArray, Int16ul, Float32l, Enum, Switch
import numpy as np
import enum
from typing import Literal

from com.Format import SerialFormat, EnumAdapter

class ControllerCommands(enum.Enum):
    GetPotiPos          = 0x10
    GetPotiRaw          = 0x11
    GetBtnState         = 0x12
    GetJoystickState    = 0x13

    GetEvents           = 0x20
    CalibratePoti       = 0x21

class ButtonState(enum.Enum):
    Pressed  = 0x01
    Released = 0x02

class JoystickState(enum.Enum):
    Middle  = 0x01
    Left    = 0x02
    Right   = 0x03
    Top     = 0x04
    Bottom  = 0x05

class Event(enum.Enum):
    No                  = 0x00
    BtnPressed          = 0x01
    BtnReleased         = 0x02
    JoystickChanged     = 0x03
    PotiChanged         = 0x04

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
            self.commands.GetPotiRaw: Struct(
                "poti_nr" / Byte
            ),
            self.commands.CalibratePoti: Struct(
                "poti_nr" / Byte,
                "min" / Int16ul,
                "max" / Int16ul
            ),
            self.commands.GetBtnState: Struct(
                "btn_id" / Byte,
            ),
            self.commands.GetJoystickState: Struct(
                "stick_id" / Byte,
            ),
            self.commands.GetEvents: Struct(),
        })

        self.response_table.update({
            self.commands.GetPotiPos: Struct(
                "poti_pos" / Float32l
            ),
            self.commands.GetPotiRaw: Struct(
                "poti_raw" / Int16ul
            ),
            self.commands.CalibratePoti: Struct(),
            self.commands.GetBtnState: Struct(
                "state" / EnumAdapter(Enum(Byte, ButtonState), ButtonState)
            ),
            self.commands.GetJoystickState: Struct(
                "state" / EnumAdapter(Enum(Byte, JoystickState), JoystickState)
            ),
            self.commands.GetEvents: Struct(
                "events" / PrefixedArray(Int16ul, Struct(
                    "id" / EnumAdapter(Enum(Byte, Event), Event),
                    "data" / Switch(lambda this: this.id, {
                        Event.BtnPressed : Struct(
                            "btn_id" / Byte
                        ),
                        Event.BtnReleased: Struct(
                            "btn_id" / Byte
                        ),
                        Event.JoystickChanged : Struct(
                            "stick_id" / Byte,
                            "state" / EnumAdapter(Enum(Byte, JoystickState), JoystickState) 
                        ),
                        Event.PotiChanged: Struct(
                            "poti_id" / Byte,
                            "pos" / Float32l,
                            "raw" / Int16ul
                        ),
                    })
                ))
            ),
        })

    def build_cmd_get_poti_pos(self, poti_nr: POTI_NRS) -> bytes:
        return self.command_builder.build( self.commands.GetPotiPos, dict(poti_nr = poti_nr))

    def build_cmd_get_poti_raw(self, poti_nr: POTI_NRS) -> bytes:
        return self.command_builder.build( self.commands.GetPotiRaw, dict(poti_nr = poti_nr))

    def build_cmd_calibrate_poti(self, poti_nr: POTI_NRS, raw_max: int = 4095, raw_min: int = 0) -> bytes:
        return self.command_builder.build( self.commands.CalibratePoti, dict(poti_nr = poti_nr, max=raw_max, min=raw_min))

    def build_cmd_get_btn_state(self, btn: int) -> bytes:
        return self.command_builder.build(self.commands.GetBtnState, dict(btn_id=btn))

    def build_cmd_get_events(self) -> bytes:
        return self.command_builder.build(self.commands.GetEvents)

    def build_cmd_get_joystick_state(self, stick: int) -> bytes:
        return self.command_builder.build(self.commands.GetJoystickState, dict(stick_id=stick))

    def get_poti_pos(self, data: dict) -> tuple[int, float]:
        return data.poti_pos

    def get_poti_raw(self, data: dict) -> tuple[int, int]:
        return data.poti_raw

    def get_btn_state(self, data: dict) -> ButtonState:
        return data.state

    def get_joystick_state(self, data: dict) -> JoystickState:
        return data.state

    def get_events(self, data: dict) -> list[Event]:
        def merge(d: dict, event_id: Event):
            d.update(dict(id=event_id))
            return d

        return [merge(e.data, e.id) for e in data.events]

    def get_btn_event_data(self, event: dict) -> int:
        return event.btn_id

    def get_joystick_event_data(self, event: dict) -> tuple[int, JoystickState]:
        return event.stick_id, JoystickState
