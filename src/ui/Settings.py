# QT-Lib
from PySide6.QtWidgets import QWidget, QSlider, QLabel,QScroller
from PySide6.QtGui import QStandardItem, QIcon
from PySide6.QtCore import QSize, Qt

from pathlib import Path
from typing import Literal
import json

from matrix.Matrix import Matrix
from ui.Input import InputDevice
from rendering.RenderManager import RenderManager
from rendering.TestMode import TestGammaMode, ColorChannel, TestScaleMode

# genrated ui
from qt.generated.UI_settings import Ui_TabSettings

class TabSettings(QWidget, Ui_TabSettings):
    matrix_connected = False
    controller_connected = False

    def __init__(self, parent, matrix, input_dev, renderer: RenderManager, width, height):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.matrix: Matrix = matrix
        self.input: InputDevice  = input_dev
        self.renderer = renderer
        
        # widget grid
        self.widgets_grid = [[self.cb_matrix_ports, self.btn_refresh_ports, self.btn_matrix_connect],
                             [self.cb_controller_ports, self.btn_refresh_ports, self.btn_controller_connect],
                             [self.sb_gamma_red, None, self.btn_test_gamma_red],
                             [self.sb_gamma_green, None, self.btn_test_gamma_green],
                             [self.sb_gamma_blue, None, self.btn_test_gamma_blue],
                             [self.sld_scale_red, None, self.btn_test_scale],
                             [self.sld_scale_green, None, self.btn_test_scale],
                             [self.sld_scale_blue, None, self.btn_test_scale],
                             [self.btn_cal_poti_left_min, None, self.btn_cal_poti_left_max],
                             [self.btn_cal_poti_right_min, None, self.btn_cal_poti_right_max]]

        # title
        self.lbl_matrix_conn.setProperty('class', 'title')
        self.lbl_gamma_corr.setProperty('class', 'title')
        self.lbl_calibration.setProperty('class', 'title')
        self.lbl_color_scale.setProperty('class', 'title')

        QScroller.grabGesture(self.scrollArea.viewport(), QScroller.TouchGesture)

        # icons
        icon_path = Path(__file__).parent / '../../assets/rotate-left-solid.svg'
        icon = QIcon(str(icon_path))

        # load settings
        self.load_settings()

        # serial connection
        self.load_ports()
        self.btn_refresh_ports.setIcon(icon)
        self.btn_refresh_ports.setIconSize(QSize(30,30))
        self.btn_refresh_ports.clicked.connect(self.load_ports)
        self.btn_refresh_ports.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.btn_matrix_connect.clicked.connect(self.handle_matrix_connect)
        self.btn_controller_connect.clicked.connect(self.handle_controller_connect)

        # try to connect
        self.btn_matrix_connect.clicked.emit()
        self.btn_controller_connect.clicked.emit()

        # calibration
        self.btn_cal_poti_left_min.clicked.connect(lambda: self.calibrate_poti(0, 'min'))
        self.btn_cal_poti_left_max.clicked.connect(lambda: self.calibrate_poti(0, 'max'))
        self.btn_cal_poti_right_min.clicked.connect(lambda: self.calibrate_poti(1, 'min'))
        self.btn_cal_poti_right_max.clicked.connect(lambda: self.calibrate_poti(1, 'max'))

        # gamma correction
        self.gamma_mode = TestGammaMode(width, height)
        self.gamma_mode_name = 'Gamma-Correction'
        self.renderer.AddMode(self.gamma_mode_name, self.gamma_mode)

        self.btn_test_gamma_red.clicked.connect(lambda: self.displayGammaTest('red'))
        self.btn_test_gamma_green.clicked.connect(lambda: self.displayGammaTest('green'))
        self.btn_test_gamma_blue.clicked.connect(lambda: self.displayGammaTest('blue'))

        self.sb_gamma_red.setValue(self.gamma['red'])
        self.sb_gamma_green.setValue(self.gamma['green'])
        self.sb_gamma_blue.setValue(self.gamma['blue'])

        self.sb_gamma_red.valueChanged.connect(lambda: self.gammaChanged('red'))
        self.sb_gamma_green.valueChanged.connect(lambda: self.gammaChanged('green'))
        self.sb_gamma_blue.valueChanged.connect(lambda: self.gammaChanged('blue'))

        self.gamma_channel: ColorChannel = 'red'

        self.matrix.gamma_red = self.gamma['red']
        self.matrix.gamma_green = self.gamma['green']
        self.matrix.gamma_blue = self.gamma['blue']

        self.gamma_mode.set_color(self.gamma_channel)
        self.gamma_mode.set_gamma(self.gamma[self.gamma_channel])

        # color scaling
        self.scale_mode = TestScaleMode(width, height)
        self.scale_mode_name = 'Color-Scale'
        self.renderer.AddMode(self.scale_mode_name, self.scale_mode)

        self.sld_scale_red.setValue(self.color_scale['red']*100)
        self.sld_scale_green.setValue(self.color_scale['green']*100)
        self.sld_scale_blue.setValue(self.color_scale['blue']*100)

        self.connect_param(self.sld_scale_red, self.lbl_scale_red, lambda v: self.scaleChanged('red', v), fmt='{:.2f}', transform=lambda v: v/100)
        self.connect_param(self.sld_scale_green, self.lbl_scale_green, lambda v: self.scaleChanged('green', v), fmt='{:.2f}',transform=lambda v: v/100)
        self.connect_param(self.sld_scale_blue, self.lbl_scale_blue, lambda v: self.scaleChanged('blue', v), fmt='{:.2f}', transform=lambda v: v/100)
        
        self.btn_test_scale.clicked.connect(self.displayScaleTest)
        
    def get_widget_map(self):
        return self.widgets_grid

    def calibrate_poti(self, poti: int, what: Literal['min', 'max']):
        raw = self.input.poti_states[poti]['raw']

        self.poti_calib[poti][what] = raw
        self.input.controller.calibrate_poti(poti, self.poti_calib[poti]['max'], self.poti_calib[poti]['min'])

        self.save_settings()

    def displayGammaTest(self, channel: ColorChannel):
        self.gamma_channel = channel

        self.gamma_mode.set_color(channel)
        self.gamma_mode.set_gamma(self.gamma[channel])

        self.renderer.SelectMode(self.gamma_mode_name)
        self.renderer.PreviewMode(self.gamma_mode_name)
        
    def displayScaleTest(self):
        self.renderer.SelectMode(self.scale_mode_name)
        self.renderer.PreviewMode(self.scale_mode_name)
    
    def scaleChanged(self, channel: ColorChannel, scale):
        self.color_scale[channel] = scale
        self.scale_mode.set_scale(self.color_scale)
        self.save_settings()

    def gammaChanged(self, channel: ColorChannel):
        self.gamma[channel] = self.sb_gamma_blue.value()
        self.matrix.set_gamma(self.gamma)

        if channel == self.gamma_channel:
            self.gamma_mode.set_gamma(self.gamma[channel])

        self.save_settings()

    def connect_param(self, slider: QSlider, label: QLabel, setter: callable, fmt: str ="{}", transform: callable = None):
        slider.sliderMoved.connect(lambda val: self.param_changed(slider, val, label, setter, fmt, transform))
        slider.valueChanged.connect(lambda val: self.param_changed(slider, val, label, setter, fmt, transform))
        self.param_changed(slider, slider.value(), label, setter, fmt, transform)
        
    def param_changed(self, slider: QSlider, val: any, label: QLabel, setter: callable, fmt: str, transform: callable = None):
        minimum = slider.minimum()
        step = slider.singleStep()

        val = round((val - minimum)/step) * step + minimum
        slider.setValue(val)
        
        if transform is not None:
            val = transform(val)

        label.setText(fmt.format(val))
        setter(val)

    def load_ports(self):
        devices = self.matrix.list_devices()
        print(devices)
        matrices = self.matrix.list_matrices(devices)
        controllers = self.input.controller.list_controllers(devices)

        if self.matrix_connected:
            matrices.append(self.matrix.port())

        if self.controller_connected:
            controllers.append(self.input.controller.port())

        self.cb_matrix_ports.clear()
        self.cb_matrix_ports.addItems(matrices)

        self.cb_controller_ports.clear()
        self.cb_controller_ports.addItems(controllers)

    def handle_matrix_connect(self):
        if self.matrix_connected:
            self.renderer.DisableMarixOutput()
            self.matrix.disconnect()
            self.matrix_connected = False
            self.btn_matrix_connect.setText("Connect")
            self.parent.lbl_matrix_status.setText("Disconnected")

        else:
            dev = self.cb_matrix_ports.currentText()
            if dev == "":
                return

            self.matrix.connect(dev)
            self.renderer.EnableMatrixOutput()
            self.matrix_connected = True
            self.btn_matrix_connect.setText("Disconnect")
            self.parent.lbl_matrix_status.setText("Connected")

    def handle_controller_connect(self):
        if self.controller_connected:
            self.input.stop()
            self.controller_connected = False
            self.btn_controller_connect.setText("Connect")
            self.parent.lbl_controller_status.setText("Disconnected")

        else:
            dev = self.cb_controller_ports.currentText()
            if dev == "":
                return

            self.input.start(dev)
            self.controller_connected = True
            self.btn_controller_connect.setText("Disconnect")
            self.parent.lbl_controller_status.setText("Connected")

    def load_default_settings(self):
        self.poti_calib = [
            {
                "min": 0,
                "max": 4095,
            },
            {
                "min": 0,
                "max": 4095,
            }
        ]

        self.gamma = {
            'red':      2.2,
            'green':    2.2,
            'blue':     2.2
        }

        self.color_scale = {
            'red':      1.0,
            'green':    1.0,
            'blue':     1.0
        }

    def load_settings(self):
        self.load_default_settings()

        path = Path(__file__).parent / '../../settings.json'
        
        if path.exists():
            with open(path) as json_file:
                json_data: dict = json.load(json_file)
                print(json_data)

                self.gamma          = json_data.get('gamma', self.gamma)
                self.poti_calib     = json_data.get('poti_calib', self.poti_calib) 
                self.color_scale    = json_data.get('color_scale', self.color_scale)

    def save_settings(self):
        path = Path(__file__).parent / '../../settings.json'

        with open(path, 'w+t') as json_file:
            json_data = {
                'gamma': self.gamma,
                'poti_calib': self.poti_calib,
                'color_scale': self.color_scale
            }

            json.dump(json_data, json_file, indent=4)
