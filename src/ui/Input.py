from PySide6.QtCore import QObject, Signal, QTimer

from controller.Controller import Controller, ButtonEvent, ButtonState, JoystickEvent, JoystickState 

class InputDevice(QObject):
    btn_pressed = Signal()
    btn_released = Signal()

    joystick_changed = Signal(JoystickState)

    poti_moved = Signal(int, float)

    btn_state: ButtonState
    btn_event: ButtonEvent
    stick_state: JoystickState
    stick_event: JoystickEvent
    poti_0: float
    poti_1: float

    def __init__(self, controller: Controller, parent = None):
        super().__init__(parent)
        
        self.controller = Controller
        self.timer = QTimer()
        self.timer.timeout.connect(self.poll)
        self.timer.start(16)

    def poll(self):
        # read
        self.btn_state = self.controller.get_btn_state()
        self.btn_event = self.controller.get_btn_event()

        self.stick_state = self.controller.get_joystick_state()
        self.stick_event = self.controller.get_joystick_event()

        new_poti_0 = self.controller.get_poti_pos(0)
        new_poti_1 = self.controller.get_poti_pos(1)

        # check if hardware states have changed
        if abs(new_poti_0-self.poti_0) > 0.5:
            self.poti_moved.emit(0, new_poti_0)

        if abs(new_poti_1-self.poti_1) > 0.5:
            self.poti_moved.emit(1, new_poti_1)

        self.poti_0 = new_poti_0
        self.poti_1 = new_poti_1

        if self.btn_event == ButtonEvent.Press:
            self.btn_pressed.emit()

        if self.btn_event == ButtonEvent.Release:
            self.btn_released.emit()

        if self.stick_event != JoystickEvent.No:
            self.joystick_changed.emit(self.stick_state)
