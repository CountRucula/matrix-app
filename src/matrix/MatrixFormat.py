from construct import Struct, Byte, RawCopy, Checksum, Int32ul, Enum, Switch, Array, PrefixedArray, Adapter, Const, Int16ul
import zlib
import numpy as np
import enum
    
HEADER = 0x7E
FOOTER = 0x7E
ESCAPE = 0x7D

class MatrixCommands(enum.Enum):
    GetFwVersion    = 0x00
    GetSize         = 0x01
    ClrFrame        = 0x02
    SetBaudrate     = 0x03

class MatrixFrameType(enum.Enum):
    Command     = 0x00
    Response    = 0x01
    Data        = 0x02

class EnumAdapter(Adapter):
    def __init__(self, subcon, py_enum):
        super().__init__(subcon)
        self.py_enum = py_enum

    def _decode(self, obj, context, path):
        # Convert Construct Enum to Python Enum
        return self.py_enum(int(obj))

    def _encode(self, obj, context, path):
        # Convert Python Enum to raw value
        return obj.value

# commands
cmd_set_baudrate = Struct(
    "baudrate" / Int32ul
)

matrix_command = Struct(
    'cmd' / EnumAdapter(Enum(Byte, MatrixCommands), MatrixCommands),
    'args' / Switch(lambda this: this.cmd,
    {
        MatrixCommands.SetBaudrate   : cmd_set_baudrate,
    }
    )
)

# responses
rsp_get_fw_version = Struct(
    "major" / Byte,
    "minor" / Byte
)

rsp_get_size = Struct(
    "width" / Byte,
    "height" / Byte
)

matrix_response = Struct(
    'cmd' / EnumAdapter(Enum(Byte, MatrixCommands), MatrixCommands),
    'data' / Switch(lambda this: this.cmd,
    {
        MatrixCommands.GetFwVersion  : rsp_get_fw_version,
        MatrixCommands.GetSize       : rsp_get_size,
    }
    )
)

# data
matrix_data = Struct(
    'data' / PrefixedArray(Int16ul, Array(3, Byte))
)

# frames
matrix_frame_data = Struct(
    'type' / EnumAdapter(Enum(Byte, MatrixFrameType), MatrixFrameType),
    'payload' / Switch(lambda this: this.type,
    {
        MatrixFrameType.Command   : matrix_command,
        MatrixFrameType.Response  : matrix_response,
        MatrixFrameType.Data      : matrix_data
    }),
)

# wrap frame with crc
matrix_frame = Struct(
    'content' / RawCopy(matrix_frame_data),
    'crc' / Checksum(Int32ul, lambda data: zlib.crc32(data), lambda this: this.content.data)
)

class MatrixFormat:
    @staticmethod
    def EscapeFrame(data) -> bytearray:
        escaped = bytearray()
        for byte in data:
            if byte == HEADER:
                escaped.extend([ESCAPE, HEADER ^ 0x20])
            elif byte == FOOTER:
                escaped.extend([ESCAPE, FOOTER ^ 0x20])
            elif byte == ESCAPE:
                escaped.extend([ESCAPE, ESCAPE ^ 0x20])
            else:
                escaped.append(byte)

        return escaped

    @staticmethod
    def UnescapeFrame(data) -> bytearray:
        unescaped = bytearray()
        escaped = False
        for byte in data:
            if escaped:
                escaped = False
                unescaped.append(byte ^ 0x20)
            else:
                if byte == ESCAPE:
                    escaped = True
                else:
                    unescaped.append(byte)

        return unescaped

    @staticmethod
    def BuildFrame(type: MatrixFrameType, payload: dict) -> bytes:
        frame = matrix_frame.build(dict(
            content=dict(value=dict(
                type=type,
                payload=payload
            ))
        ))

        return bytes([HEADER]) + MatrixFormat.EscapeFrame(frame) + bytes([FOOTER])

    @staticmethod
    def ParseFrame(raw: bytes) -> dict:
        frame = matrix_frame.parse(MatrixFormat.UnescapeFrame(raw[1:-1]))
        return frame

    @staticmethod
    def BuildResponse(cmd: str, data: dict) -> bytes:
        return MatrixFormat.BuildFrame(MatrixFrameType.Response, dict(cmd=cmd, data=data))

    def BuildResponse_GetSize(width: int, height: int) -> bytes:
        return MatrixFormat.BuildResponse(MatrixCommands.GetSize, dict(width=width, height=height))

    def BuildResponse_GetFwVersion(major: int, minor: int) -> bytes:
        return MatrixFormat.BuildResponse(MatrixCommands.GetFwVersion, dict(major=major, minor=minor))

    @staticmethod
    def BuildData(data: np.ndarray) -> bytes:
        return MatrixFormat.BuildFrame(MatrixFrameType.Data, dict(data=data))

    @staticmethod
    def BuildCmd(cmd: str, args: dict = None) -> bytes:
        return MatrixFormat.BuildFrame(MatrixFrameType.Command, dict(cmd=cmd, args=args))

    @staticmethod
    def BuildCmd_SetBaudrate(baudrate:int = 115200) -> bytes:
        return MatrixFormat.BuildCmd(MatrixCommands.SetBaudrate, args=dict(baudrate=baudrate))

    @staticmethod
    def BuildCmd_GetFwVersion() -> bytes:
        return MatrixFormat.BuildCmd(MatrixCommands.GetFwVersion)

    @staticmethod
    def BuildCmd_GetSize() -> bytes:
        return MatrixFormat.BuildCmd(MatrixCommands.GetSize)

    @staticmethod
    def BuildCmd_ClrFrame() -> bytes:
        return MatrixFormat.BuildCmd(MatrixCommands.ClrFrame)


    @staticmethod
    def GetFrameType(frame: dict) -> int:
        return frame.content.value.type

    def GetFrameContent(frame: dict) -> dict:
        return frame.content.value.payload

    @staticmethod
    def GetResponseCmd(frame: dict) -> int:
        content = MatrixFormat.GetFrameContent(frame)
        return content.cmd

    @staticmethod
    def GetResponseData(frame: dict) -> dict:
        content = MatrixFormat.GetFrameContent(frame)
        return content.data

    @staticmethod
    def GetCommand(frame: dict) -> int:
        content = MatrixFormat.GetFrameContent(frame)
        return content.cmd

    @staticmethod
    def GetCommandArgs(frame: dict) -> dict:
        content = MatrixFormat.GetFrameContent(frame)
        return content.args

    @staticmethod
    def GetData(frame: dict) -> np.ndarray:
        content = MatrixFormat.GetFrameContent(frame)
        return np.array(content.data, dtype=np.uint8)

