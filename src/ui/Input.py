from PySide6.QtCore import QObject, Signal, QTimer
from threading import Thread
import time

from controller.Controller import Controller, ButtonState, JoystickState, Event
import logging

logging.basicConfig(level=logging.INFO)

class InputDevice(QObject):
    btn_clicked = Signal(int)
    btn_double_clicked = Signal(int)
    joystick_changed = Signal(int, JoystickState)
    poti_moved = Signal(int, float)

    btn_states = [ButtonState.Released, ButtonState.Released]
    stick_states = [JoystickState]
    poti_states = [{'pos': 0.0, 'raw': 0}, {'pos': 0.0, 'raw': 0}]

    def __init__(self, controller: Controller, parent = None):
        super().__init__(parent)
        
        self.controller = controller
        self.running = False
    
    def __del__(self):
        if self.running:
            self.stop()

    def start(self, dev: str):
        self.controller.connect(dev)

        # read initial values
        self.read_values()

        self.poll_thread = Thread(target=self.loop, daemon=True)
        self.running = True
        self.poll_thread.start()

    def stop(self):
        self.running = False
        self.poll_thread.join()
        self.controller.disconnect()

    def read_values(self):
        self.btn_states[0]          = self.controller.get_btn_state(0)
        self.btn_states[1]          = self.controller.get_btn_state(1)
        self.stick_states[0]        = self.controller.get_joystick_state(0)
        self.poti_states[0]['raw']  = self.controller.get_poti_raw(0)
        self.poti_states[1]['raw']  = self.controller.get_poti_raw(1)
        self.poti_states[0]['pos']  = self.controller.get_poti_pos(0)
        self.poti_states[1]['pos']  = self.controller.get_poti_pos(1)

    def poll(self):
        if not self.controller.connected():
            return
        
        # # if self.stick_states[0] != self.ctro
        # new_stick_state = self.controller.get_joystick_state(0)
        # if self.stick_states[0] != new_stick_state:
        #     logging.info(f"joystick state changed to {new_stick_state}")
        #     self.stick_states[0] = new_stick_state
        #     self.joystick_changed.emit(0, new_stick_state)

        # handle events
        events = self.controller.get_events()

        for e in events:
            match e.id:
                case Event.BtnClick:
                    btn = e.btn_id
                    logging.info(f"btn {btn} clicked")

                    self.btn_states[btn] = self.controller.get_btn_state(btn)
                    self.btn_clicked.emit(btn)

                case Event.BtnDoubleClick:
                    btn = e.btn_id
                    logging.info(f"btn {btn} double clicked")

                    self.btn_states[btn] = self.controller.get_btn_state(btn)
                    self.btn_double_clicked.emit(btn)

                case Event.JoystickChanged:
                    stick = e.stick_id
                    state = e.state
                    logging.info(f"joystick {stick} moved: {state}")

                    self.stick_states[stick] = state
                    self.joystick_changed.emit(stick, state)

                case Event.PotiChanged:
                    poti = e.poti_id
                    pos = e.pos
                    raw = e.raw
                    # logging.info(f"poti {poti} moved: {pos:.1f} , {raw}")

                    self.poti_states[poti]['raw'] = raw
                    self.poti_states[poti]['pos'] = pos
                    self.poti_moved.emit(poti, pos)

    def loop(self):
        while self.running:
            self.poll()
            time.sleep(0.020)
