import serial
import serial.tools
import serial.tools.list_ports
from enum import Enum
import logging
from queue import Queue, Empty
from threading import Thread
import time

from matrix.MatrixFormat import HEADER, FOOTER, ESCAPE

class State(Enum):
    IDLE = 0
    DATA = 1

class MatrixLink:
    def __init__(self):
        self.serial = None
        self.baudrate = 9600
        self.stopbits = 1.0
        self.parity = serial.PARITY_NONE
        self.bits = 8
        self.timeout = 0.01

        self.connected = False

        self.send_queue  = Queue()
        self.recv_queue  = Queue()

        self.recv_buffer = bytearray()
        self.state = State.IDLE
        self.data_escaped = False

    def __del__(self):
        self.Disconnect()

    def Start(self):
        self.running = True
        self.send_thread = Thread(target=self.SendLoop, daemon=True)
        self.recv_thread = Thread(target=self.ReceiveLoop, daemon=True)
        self.send_thread.start()
        self.recv_thread.start()

    def Stop(self):
        self.running = False
        self.send_thread.join()
        self.recv_thread.join()

    def SetBaudRate(self, baudrate: int):
        self.baudrate = baudrate
        self.serial.baudrate = self.baudrate


    def ListDevices(self) -> list[str]:
        ports = serial.tools.list_ports.comports()
        self.available_devices = [info.device for info in ports]

        return self.available_devices

    def Connect(self, dev: str) -> None:
        self.ListDevices()

        if dev not in self.available_devices:
            logging.error(f"could not connect to {dev}; not a com-port!")
            return

        self.serial = serial.Serial(
            dev,
            baudrate=self.baudrate,
            bytesize=self.bits,
            parity=self.parity,
            stopbits=self.stopbits,
            timeout=self.timeout,
        )
        self.serial.flush()
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()

        self.connected = True

        self.Start()

        logging.info(f"connected to {dev}")

    def Disconnect(self) -> None:
        if self.serial is None:
            logging.info("already disconnected")
            return

        self.Stop()

        self.serial.close()
        self.serial = None
        self.connected = False

    def ReadByte(self, byte) -> None:
        match self.state:
            case State.IDLE:
                if byte == HEADER:
                    self.data_escaped = False
                    self.recv_buffer = bytearray([byte])
                    self.state = State.DATA

            case State.DATA:
                self.recv_buffer.append(byte)

                if self.data_escaped:
                    self.data_escaped = False
                    return

                if byte == ESCAPE:
                    self.data_escaped = True

                if byte == FOOTER:
                    self.recv_queue.put(self.recv_buffer)
                    self.state = State.IDLE

    def Available(self) -> bool:
        return not self.recv_queue.empty()

    def SendFrame(self, frame: bytes):
        self.send_queue.put(frame)

    def GetFrame(self, timeout: float = 0.01):
        try:
            return self.recv_queue.get(block=True, timeout=timeout)
        except Empty:
            return None

    def ReceiveLoop(self):
        while self.running:
            try:
                data = self.serial.read_all()

                for byte in data:
                    self.ReadByte(byte)

                time.sleep(0.01)
            except Exception:
                self.running = False

    def SendLoop(self):
        while self.running:
            try:
                frame = self.send_queue.get(timeout=0.01)
                self.serial.write(frame)
            except Empty:
                pass
            except Exception:
                self.running = False