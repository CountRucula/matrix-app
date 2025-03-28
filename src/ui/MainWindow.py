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
from ui.Text import TabText
from ui.Preview import TabPreview
from ui.Game import TabGame

from rendering.RenderManager import RenderManager
from rendering.AnimationMode import SineWaveMode, SawtoothMode, RectangularMode, RaindropsMode, RainbowMode
from rendering.MusicMode import TimelineMode, FrequencyBandsMode

class KeyFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == event.KeyPress:
            if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right, Qt.Key_Return):
                print(f"Key pressed: {event.text() or event.key()}")
                return True  # Mark as handled, block propagation
        return super().eventFilter(obj, event)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, matrix):
        super().__init__()
        self.setupUi(self)

        # matrix dimensions
        self.matrix_width = 50
        self.matrix_height = 20

        # window attributes
        self.setWindowTitle("Matrix-App")
        self.setMinimumSize(100,100)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # matrix connection
        self.matrix = matrix

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
        self.tab_settings   = TabSettings(self, self.matrix, self.renderer, self.matrix_width, self.matrix_height)
        self.tab_animation  = TabAnimation(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_game       = TabGame(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_music      = TabMusic(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_text       = TabText()
        self.tab_image      = TabImage(self.renderer, self.matrix_width, self.matrix_height)
        self.tab_preview    = TabPreview(self.matrix_width, self.matrix_height)

        self.loadTab('Settings', self.tab_settings)
        self.loadTab('Animation', self.tab_animation)
        self.loadTab('Game', self.tab_game)
        self.loadTab('Music', self.tab_music)
        self.loadTab('Text', self.tab_text)
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
        self.showMaximized()

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