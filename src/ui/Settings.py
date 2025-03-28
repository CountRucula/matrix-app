# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem, QIcon
from PySide6.QtCore import QSize, Qt

from pathlib import Path
from typing import Literal

from matrix.Matrix import Matrix
from rendering.RenderManager import RenderManager
from rendering.TestMode import TestGammaMode, ColorChannel

# genrated ui
from qt.generated.UI_settings import Ui_TabSettings

class TabSettings(QWidget, Ui_TabSettings):
    def __init__(self, parent, matrix, renderer: RenderManager, width, height):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.matrix: Matrix = matrix
        self.renderer = renderer

        # title
        self.lbl_frackstock_conn.setProperty('class', 'title')
        self.lbl_matrix_conn.setProperty('class', 'title')
        self.lbl_gamma_corr.setProperty('class', 'title')

        # icons
        icon_path = Path(__file__).parent / '../../assets/rotate-left-solid.svg'
        icon = QIcon(str(icon_path))

        # matrix connection
        self.load_ports()
        self.btn_refresh_ports.setIcon(icon)
        self.btn_refresh_ports.setIconSize(QSize(30,30))
        self.btn_refresh_ports.clicked.connect(self.load_ports)
        self.btn_refresh_ports.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.btn_matrix_connect.clicked.connect(self.connect_callback)
        self.connected = False

        self.baudrates = [9600, 19200, 38400, 115200, 256000, 1000000]
        self.baudrate: int = 115200
        self.populate_combo_boxes()
        self.cb_matrix_baudrates.currentTextChanged.connect(self.baudrate_changed)

        # gamma correction
        self.gamma_mode = TestGammaMode(width, height)
        self.gamma_mode_name = 'Gamma-Correction'
        self.renderer.AddMode(self.gamma_mode_name, self.gamma_mode)

        self.btn_test_gamma_red.clicked.connect(lambda: self.displayGammaTest('red'))
        self.btn_test_gamma_green.clicked.connect(lambda: self.displayGammaTest('green'))
        self.btn_test_gamma_blue.clicked.connect(lambda: self.displayGammaTest('blue'))

        self.sb_gamma_red.valueChanged.connect(lambda: self.gammaChanged('red'))
        self.sb_gamma_green.valueChanged.connect(lambda: self.gammaChanged('green'))
        self.sb_gamma_blue.valueChanged.connect(lambda: self.gammaChanged('blue'))

        self.gamma = {
            'red':      2.2,
            'green':    2.2,
            'blue':     2.2
        }
        self.gamma_channel: ColorChannel = 'red'

        self.gamma_mode.set_color(self.gamma_channel)
        self.gamma_mode.set_gamma(self.gamma[self.gamma_channel])

    def displayGammaTest(self, channel: ColorChannel):
        self.gamma_channel = channel

        self.gamma_mode.set_color(channel)
        self.gamma_mode.set_gamma(self.gamma[channel])

        self.renderer.SelectMode(self.gamma_mode_name)
        self.renderer.PreviewMode(self.gamma_mode_name)

    def gammaChanged(self, channel: ColorChannel):
        if channel == 'red':
            self.gamma[channel] = self.sb_gamma_red.value()
    
        elif channel == 'green':
            self.gamma[channel] = self.sb_gamma_green.value()

        elif channel == 'blue':
            self.gamma[channel] = self.sb_gamma_blue.value()

        if channel == self.gamma_channel:
            self.gamma_mode.set_gamma(self.gamma[channel])

    def populate_combo_boxes(self):
        self.cb_matrix_baudrates.addItems([str(rate) for rate in self.baudrates])
        self.cb_matrix_baudrates.setCurrentIndex(self.baudrates.index(self.baudrate))

    def baudrate_changed(self):
        self.baudrate = int(self.cb_matrix_baudrates.currentText(), 10)
        self.matrix.SetBaudrate(self.baudrate)

    def load_ports(self):
        devices = self.matrix.ListMatrices()

        self.cb_matrix_ports.clear()
        self.cb_matrix_ports.addItems(devices)
