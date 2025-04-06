from PySide6.QtCore import QObject, Signal, QTimer
from threading import Thread
import time

from controller.Controller import Controller, ButtonState, JoystickState, Event
import logging

logging.basicConfig(level=logging.INFO)

class InputDevice(QObject):
    btn_pressed = Signal(int)
    btn_released = Signal(int)

    joystick_changed = Signal(int, JoystickState)

    poti_moved = Signal(int, float)

    btn_state: ButtonState
    stick_state: JoystickState
    poti_0: float = 0
    poti_1: float = 0

    poti_0_raw: int = 0
    poti_1_raw: int = 0

    def __init__(self, controller: Controller, parent = None):
        super().__init__(parent)
        
        self.controller = controller
        self.running = False
    
    def __del__(self):
        if self.running:
            self.stop()

    def start(self, dev: str):
        self.controller.connect(dev)
        self.poll_thread = Thread(target=self.loop, daemon=True)
        self.running = True
        self.poll_thread.start()

    def stop(self):
        self.running = False
        self.poll_thread.join()
        self.controller.disconnect()

    def poll(self):
        if not self.controller.connected():
            return

        # read states
        self.btn_state = self.controller.get_btn_state()
        self.stick_state = self.controller.get_joystick_state()
        self.poti_0_raw = self.controller.get_poti_raw(0)
        self.poti_1_raw = self.controller.get_poti_raw(1)
        new_poti_0 = self.controller.get_poti_pos(0)
        new_poti_1 = self.controller.get_poti_pos(1)

        # handle events
        events = self.controller.get_events()

        for e in events:
            match e.id:
                case Event.BtnPressed:
                    btn = e.btn_id
                    logging.info(f"btn {btn} pressed")
                    self.btn_pressed.emit(btn)

                case Event.BtnReleased:
                    btn = e.btn_id
                    logging.info(f"btn {btn} released")
                    self.btn_released.emit(btn)

                case Event.JoystickChanged:
                    stick = e.stick_id
                    state = e.state
                    logging.info(f"joystick {stick} moved: {state}")
                    self.joystick_changed.emit(stick, state)

        # check if potis have moved
        if abs(new_poti_0-self.poti_0) > 0.5:
            logging.info(f"poti 0 moved: {new_poti_0:.1f}")
            self.poti_moved.emit(0, new_poti_0)

        if abs(new_poti_1-self.poti_1) > 0.5:
            logging.info(f"poti 1 moved: {new_poti_1:.1f}")
            self.poti_moved.emit(1, new_poti_1)

        self.poti_0 = new_poti_0
        self.poti_1 = new_poti_1

    def loop(self):
        while self.running:
            self.poll()
            time.sleep(0.020)
