from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabBar, QLabel, QListWidget, QSizePolicy
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt, QPoint, QObject, QSize, QTimer, QPropertyAnimation, QRect

from qt.generated.UI_sidebar import Ui_sidebar

class Sidebar(QWidget, Ui_sidebar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # self.setFixedWidth(width)
        self.setWindowFlags(Qt.SubWindow)
        self.setProperty('class', 'transparent-bg')

        # Ensure it overlays
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()
        
        self.btn_toggle.clicked.connect(self.hide_with_animation)
        self.btn_toggle.setProperty('class', 'transparent-bg')

    def show_with_animation(self, index:int = 0):
        self.tabs.setCurrentRow(index)
        
        self.setGeometry(-self.width(), 0, self.width(), self.parent().height())
        self.show()
        self.raise_()

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(300)
        self.anim.setStartValue(QRect(-self.width(), 0, self.parent().width(), self.parent().height()))
        self.anim.setEndValue(QRect(0, 0, self.parent().width(), self.parent().height()))
        self.anim.start()

    def hide_with_animation(self):
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(300)
        self.anim.setStartValue(QRect(0, 0, self.parent().width(), self.parent().height()))
        self.anim.setEndValue(QRect(-self.width(), 0, self.parent().width(), self.parent().height()))
        self.anim.finished.connect(self.hide)
        self.anim.start()
