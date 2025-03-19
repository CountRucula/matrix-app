from pathlib import Path

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

from rendering.RenderManager import RenderManager
from rendering.AnimationMode import SineWaveMode, SawtoothMode, RectangularMode, RaindropsMode, RainbowMode
from rendering.ImageMode import ImageMode, GifMode
from rendering.MusicMode import TimelineMode
from rendering.GameMode import SnakeMode, Direction

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

        self.matrix_width = 50
        self.matrix_height = 20

        self.setWindowTitle("Matrix-App")
        self.setMinimumSize(100,100)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.matrix = matrix

        self.renderer       = RenderManager(self.matrix_width, self.matrix_height, 30)
        self.sine_mode      = SineWaveMode(self.matrix_width,self.matrix_height)
        self.saw_mode       = SawtoothMode(self.matrix_width,self.matrix_height)
        self.rect_mode      = RectangularMode(self.matrix_width,self.matrix_height)
        self.rain_mode      = RaindropsMode(self.matrix_width,self.matrix_height)
        self.rainbow_mode   = RainbowMode(self.matrix_width,self.matrix_height)
        self.img_mode       = GifMode(self.matrix_width,self.matrix_height)
        self.timeline_mode  = TimelineMode(self.matrix_width, self.matrix_height)
        self.snake_mode     = SnakeMode(self.matrix_width, self.matrix_height)

        self.renderer.AddMode('Sine', self.sine_mode)
        self.renderer.AddMode('Sawtooth', self.saw_mode)
        self.renderer.AddMode('Rectangular', self.rect_mode)
        self.renderer.AddMode('Rain', self.rain_mode)
        self.renderer.AddMode('Rainbow', self.rainbow_mode)
        self.renderer.AddMode('Image', self.img_mode)
        self.renderer.AddMode('Timeline', self.timeline_mode)
        self.renderer.AddMode('Snake', self.snake_mode)

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

        # create tabs bar
        self.tab_bar = QTabBar()
        self.tab_bar.addTab("Settings")
        self.tab_bar.addTab("Animation")
        self.tab_bar.addTab("Music")
        self.tab_bar.addTab("Text")
        self.tab_bar.addTab("Image")
        self.tab_bar.addTab("Preview")
        self.tab_bar.setFocusPolicy(Qt.NoFocus)
        self.title_layout.insertWidget(0, self.tab_bar)

        # add tab content
        self.loadTab(TabSettings(self.matrix))
        self.loadTab(TabAnimation())
        self.loadTab(TabMusic())
        self.loadTab(TabText())
        self.loadTab(TabImage(self.img_mode))
        tab_preview = TabPreview(self.matrix_width, self.matrix_height)
        self.loadTab(tab_preview)

        self.tab_bar.currentChanged.connect(self.stack.setCurrentIndex)

        self.renderer.SetVirtualMatrix(tab_preview.preview_matrix)
        self.renderer.Start()

        #print(self.renderer.GetModes())
        self.cb_mode_selection.addItems(self.renderer.GetModes())
        self.cb_mode_selection.currentIndexChanged.connect(self.selectPreviewMode)
        self.cb_mode_selection.setFocusPolicy(Qt.NoFocus)
        self.selectPreviewMode()

        self.timeline_mode.open_stream()

        # fps timer
        self.fps_timer = QTimer(self)
        self.fps_timer.timeout.connect(self.updateFPS)
        self.fps_timer.setSingleShot(False)
        self.fps_timer.start(1000)

        # show main window
        self.showMaximized()

    def loadTab(self, content: QWidget) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(content)
        self.stack.addWidget(page)

    def selectPreviewMode(self):
        mode = self.cb_mode_selection.currentText()
        self.renderer.PreviewMode(mode)

    def updateFPS(self):
        fps = self.renderer.GetFPS()
        self.lbl_fps.setText(f"{fps:4.2f} FPS")

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Up:
            self.snake_mode.change_direction(Direction.UP)
        elif event.key() == Qt.Key_Down:
            self.snake_mode.change_direction(Direction.DOWN)
        elif event.key() == Qt.Key_Left:
            self.snake_mode.change_direction(Direction.LEFT)
        elif event.key() == Qt.Key_Right:
            self.snake_mode.change_direction(Direction.RIGHT)
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.snake_mode.start_pause()
            print("Game Start / Restart!")

        super().keyPressEvent(event)

        print(f"Direction: {self.snake_mode.new_dir}")

