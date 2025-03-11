from pathlib import Path

# QT-Lib
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QPoint

# genrated ui
from qt.generated.UI_MainWindow import Ui_MainWindow

# tabs
from ui.Settings import TabSettings
from ui.Image import TabImage
from ui.Music import TabMusic
from ui.Animation import TabAnimation
from ui.Text import TabText
from ui.Preview import TabPreview

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, matrix):
        super().__init__()
        self.setupUi(self)

        self.matrix_width = 50
        self.matrix_height = 30

        self.setWindowTitle("Matrix-App")

        self.matrix = matrix

        # set icon
        icon_path = Path(__file__).parent / "../../assets/top-hat.svg"
        icon = QIcon(str(icon_path))
        self.setWindowIcon(icon)

        # create tabs bar
        self.tab_bar = QTabBar()
        self.tab_bar.addTab("Settings")
        self.tab_bar.addTab("Animation")
        self.tab_bar.addTab("Music")
        self.tab_bar.addTab("Text")
        self.tab_bar.addTab("Image")
        self.tab_bar.addTab("Preview")
        self.title_layout.addWidget(self.tab_bar)
        self.title_layout.addStretch()

        # add tab content
        self.loadTab(TabSettings(self.matrix))
        self.loadTab(TabAnimation())
        self.loadTab(TabMusic())
        self.loadTab(TabText())
        self.loadTab(TabImage())
        tab_preview = TabPreview(self.matrix_width, self.matrix_height)
        self.loadTab(tab_preview)

        self.tab_bar.currentChanged.connect(self.stack.setCurrentIndex)

        # show main window
        self.show()

    def loadTab(self, content: QWidget) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(content)
        self.stack.addWidget(page)