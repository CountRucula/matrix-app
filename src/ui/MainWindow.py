from pathlib import Path
import numpy as np

# QT-Lib
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabBar
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt, QPoint, QObject, QSize, QTimer

# genrated ui
from qt.generated.UI_MainWindow import Ui_MainWindow

# tabs
from ui.Settings import TabSettings
from ui.Image import TabImage
from ui.Music import TabMusic
from ui.Animation import TabAnimation
from ui.Preview import TabPreview
from ui.Game import TabGame
from ui.Input import InputDevice

from rendering.RenderManager import RenderManager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, matrix, controller):
        super().__init__()
        self.setupUi(self)

        # matrix dimensions
        self.matrix_width = 50
        self.matrix_height = 20

        # window attributes
        self.setWindowTitle("Matrix-App")
        self.setMinimumSize(800,480)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # serial connections
        self.matrix = matrix
        self.controller = controller
        self.input_dev = InputDevice(self.controller)

        # register render modes
        self.renderer = RenderManager(
            self.matrix_width,
            self.matrix_height,
            30,
            on_mode_changed=self.lbl_current_mode.setText,
            on_preview_mode_changed=self.lbl_preview_mode.setText,
        )

        # set icon
        icon_path = Path(__file__).parent / "../../assets/top-hat.svg"
        icon = QIcon(str(icon_path))
        self.setWindowIcon(icon)

        # close button
        icon_path = Path(__file__).parent / "../../assets/xmark.svg"
        icon = QIcon(str(icon_path))
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(20,20))
        self.btn_close.clicked.connect(self.close)
        self.btn_close.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # create tab bar
        self.tab_bar = QTabBar()
        self.tab_bar.setFocusPolicy(Qt.NoFocus)
        self.title_layout.insertWidget(0, self.tab_bar)

        # add tab content 
        self.tab_settings   = TabSettings(self, self.matrix, self.input_dev, self.renderer, self.matrix_width, self.matrix_height)
        self.tab_animation  = TabAnimation(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_game       = TabGame(self.input_dev, self.renderer, self.matrix_width, self.matrix_height)
        self.tab_music      = TabMusic(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_image      = TabImage(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_preview    = TabPreview(self.matrix_width, self.matrix_height)

        self.loadTab('Settings', self.tab_settings)
        self.loadTab('Animation', self.tab_animation)
        self.loadTab('Game', self.tab_game)
        self.loadTab('Music', self.tab_music)
        self.loadTab('Image', self.tab_image)
        self.loadTab('Preview', self.tab_preview)
        self.tab_bar.currentChanged.connect(self.stack.setCurrentIndex)

        # add preview matrix & hardware matrix to renderer
        self.renderer.SetVirtualMatrix(self.tab_preview.preview_matrix)
        self.renderer.SetMatrix(self.matrix)
        self.renderer.Start()
        
        # fps timer
        self.fps_timer = QTimer(self)
        self.fps_timer.timeout.connect(self.updateFPS)
        self.fps_timer.setSingleShot(False)
        self.fps_timer.start(1000)

        # show main window
        # self.showMaximized()
        self.show()

    def loadTab(self, name: str, content: QWidget) -> None:
        self.tab_bar.addTab(name)
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(content)
        self.stack.addWidget(page)

    def selectPreviewMode(self):
        mode = self.cb_mode_selection.currentText()
        self.renderer.PreviewMode(mode)

    def selectMode(self):
        mode = self.cb_mode_selection.currentText()
        self.renderer.SelectMode(mode)
        self.lbl_current_mode.setText(mode)
    
    def updateFPS(self):
        fps = self.renderer.GetFPS()
        self.lbl_fps.setText(f"{fps:4.2f}")

    def keyPressEvent(self, event: QKeyEvent):
        self.tab_game.keyPressEvent(event)
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        self.tab_game.keyReleaseEvent(event)
        return super().keyReleaseEvent(event)

    def closeEvent(self, event):
        self.renderer.DisableMarixOutput()
        self.matrix.disconnect()
        event.accept() # let the window close