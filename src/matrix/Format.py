from construct import Struct, Byte, Array, PrefixedArray, Int16ul
import numpy as np
import enum

from com.Format import SerialFormat

class MatrixCommands(enum.Enum):
    GetSize         = 0x10
    ClrFrame        = 0x11
    SetFrame        = 0x12

class MatrixFormat(SerialFormat):
    def __init__(self):
        self.commands = MatrixCommands
        super().__init__()

    def create_tables(self) -> None:
        super().create_tables()

        self.command_table.update({
            self.commands.GetSize: Struct(),
            self.commands.ClrFrame: Struct(),
            self.commands.SetFrame: Struct(
                'data' / PrefixedArray(Int16ul, Array(3, Byte))
            )
        })

        self.response_table.update({
            self.commands.GetSize: Struct(
                "width" / Byte,
                "height" / Byte
            ),
            self.commands.ClrFrame: Struct(),
            self.commands.SetFrame: Struct()
        })

    def build_cmd_get_size(self) -> bytes:
        return self.command_builder.build(self.commands.GetSize)

    def build_cmd_clr_frame(self) -> bytes:
        return self.command_builder.build(self.commands.ClrFrame)

    def build_cmd_set_frame(self, data: np.ndarray) -> bytes:
        return self.command_builder.build(self.commands.SetFrame, dict(data=data))

    def get_size(self, payload: dict) -> tuple[int, int]:
        data = self.response_builder.get_data(payload)
        return data.width, data.height
