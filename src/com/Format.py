from construct import Struct, Byte, RawCopy, Checksum, Int32ul, Enum, Switch, Adapter
import zlib
import enum
from itertools import chain
    
HEADER = 0x7E
FOOTER = 0x7E
ESCAPE = 0x7D

class FrameType(enum.Enum):
    Command     = 0x00
    Response    = 0x01

class GenericCommands(enum.Enum):
    GetFwVersion    = 0x00
    GetDeviceType   = 0x01

class DeviceType(enum.Enum):
    Basic       = 0x00
    Controller  = 0x01
    Matrix      = 0x02

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

class FrameBuilder:
    def __init__(self):
        self.payload_table = {
            FrameType.Command   : Struct(),
            FrameType.Response  : Struct()
        }
        self.create_structs()

    def set_command_struct(self, struct: Struct) -> None:
        self.payload_table[FrameType.Command] = struct
        self.create_structs()

    def set_response_struct(self, struct: Struct) -> None:
        self.payload_table[FrameType.Response] = struct
        self.create_structs()

    def create_structs(self) -> None:
        # frames
        self.content_t = Struct(
            'type' / EnumAdapter(Enum(Byte, FrameType), FrameType),
            'payload' / Switch(lambda this: this.type, self.payload_table),
        )

        # wrap frame with crc
        self.frame_t = Struct(
            'content' / RawCopy(self.content_t),
            'crc' / Checksum(Int32ul, lambda data: zlib.crc32(data), lambda this: this.content.data)
        )

    def escape(self, data) -> bytearray:
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

    def unescape(self, data) -> bytearray:
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

    def build(self, ftype: FrameType, payload: dict) -> bytes:
        frame = self.frame_t.build(dict(
            content=dict(value=dict(
                type=ftype,
                payload=payload
            ))
        ))

        return bytes([HEADER]) + self.escape(frame) + bytes([FOOTER])

    def parse(self, raw: bytes) -> dict:
        return self.frame_t.parse(self.unescape(raw[1:-1]))

    def get_frame_type(self, frame: dict) -> int:
        return frame.content.value.type

    def get_frame_payload(self, frame: dict) -> dict:
        return frame.content.value.payload

class CommandBuilder:
    def __init__(self, frame_builder: FrameBuilder, commands: enum.Enum, command_table: dict):
        self.frame_builder = frame_builder
        self.commands = commands
        self.command_table = command_table

        self.create_structs()

    def create_structs(self) -> None:
        self.command_t = Struct(
            'cmd' / EnumAdapter(Enum(Byte, self.commands), self.commands),
            'args' / Switch(lambda this: this.cmd, self.command_table)
        )

        self.frame_builder.set_command_struct(self.command_t)

    def parse(self, raw: bytes) -> dict:
        return self.frame_builder.parse(raw)

    def build(self, cmd: enum.Enum, args: dict = None) -> bytes:
        return self.frame_builder.build(FrameType.Command, dict(cmd=cmd, args=args))

    def get(self, payload: dict) -> tuple[int, dict]:
        return payload.cmd, payload.args
    
class ResponseBuilder:
    def __init__(self, frame_builder: FrameBuilder, commands: enum.Enum, response_table: dict):
        self.frame_builder = frame_builder
        self.commands = commands
        self.response_table = response_table

        self.create_structs()

    def create_structs(self) -> None:
        self.response_t = Struct(
            'cmd' / EnumAdapter(Enum(Byte, self.commands), self.commands),
            'data' / Switch(lambda this: this.cmd, self.response_table)
        )

        self.frame_builder.set_response_struct(self.response_t)

    def build(self, cmd: enum.Enum, args: dict = None) -> bytes:
        return self.frame_builder.build(FrameType.Command, dict(cmd=cmd, args=args))

    def get(self, payload: dict) -> tuple[int, dict]:
        return payload.cmd, payload.data

class SerialFormat:
    def __init__(self):
        if hasattr(self, 'commands'):
            self.commands = self.merge_commands(GenericCommands)
        else:
            self.commands = GenericCommands

        self.create_tables()
        self.create_builders()

    def merge_commands(self, additional_commands):
        return enum.Enum('Commands', [(i.name, i.value) for i in chain(self.commands, additional_commands)])
        
    def create_tables(self) -> None:
        self.command_table = {
            self.commands.GetFwVersion  : Struct(),
            self.commands.GetDeviceType : Struct()
        } 
    
        self.response_table = {
            self.commands.GetFwVersion  : Struct(
                "major" / Byte,
                "minor" / Byte
            ),

            self.commands.GetDeviceType : Struct(
                "type" / EnumAdapter(Enum(Byte, DeviceType), DeviceType)
            )
        }

    def create_builders(self) -> None:
        self.frame_builder = FrameBuilder()
        self.command_builder = CommandBuilder(self.frame_builder, self.commands, self.command_table)
        self.response_builder = ResponseBuilder(self.frame_builder, self.commands, self.response_table)

    def build_cmd_get_fw_version(self) -> bytes:
        return self.command_builder.build(self.commands.GetFwVersion)

    def build_cmd_get_device_type(self) -> bytes:
        return self.command_builder.build(self.commands.GetDeviceType)

    def parse(self, raw: bytes) -> tuple[int, dict]:
        frame = self.frame_builder.parse(raw)
        
        ftype = self.frame_builder.get_frame_type(frame)
        payload = self.frame_builder.get_frame_payload(frame)

        return ftype, payload

    def get_response(self, payload: dict) -> tuple[GenericCommands, dict]:
        return self.response_builder.get(payload)

    def get_command(self, payload: dict) -> tuple[GenericCommands, dict]:
        return self.command_builder.get(payload)

    def get_fw_version(self, data: dict) -> tuple[int, int]:
        return data.major, data.minor

    def get_device_type(self, data: dict) -> int:
        return data.type