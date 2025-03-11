# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem, QIcon
import PySide6.QtCore as QtCore

from pathlib import Path
from matrix.Matrix import Matrix

# genrated ui
from qt.generated.UI_settings import Ui_TabSettings

class TabSettings(QWidget, Ui_TabSettings):
    def __init__(self, matrix):
        super().__init__()
        self.setupUi(self)

        self.matrix = matrix

        self.populate_combo_boxes()
        self.load_ports()

        self.lbl_frackstock_conn.setProperty('class', 'title')
        self.lbl_matrix_conn.setProperty('class', 'title')


        icon_path = Path(__file__).parent / '../../assets/rotate-left-solid.svg'
        icon = QIcon(str(icon_path))
        self.btn_refresh_ports.setIcon(icon)
        self.btn_refresh_ports.setIconSize(QtCore.QSize(30,30))
        self.btn_refresh_ports.clicked.connect(self.load_ports)

    def populate_combo_boxes(self):
        baud_rates = [9600, 19200, 38400, 115200, 256000, 1000000]

        self.cb_matrix_baudrates.addItems([str(rate) for rate in baud_rates])

    def load_ports(self):
        devices = self.matrix.ListMatrices()

        self.cb_matrix_ports.clear()
        self.cb_matrix_ports.addItems(devices)
