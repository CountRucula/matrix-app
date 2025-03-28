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
