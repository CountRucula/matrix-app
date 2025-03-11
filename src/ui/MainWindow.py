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

from rendering.RenderManager import RenderManager
from rendering.AnimationMode import SineWaveMode, SawtoothMode, RectangularMode, RaindropsMode, RainbowMode
from rendering.ImageMode import ImageMode, GifMode

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, matrix):
        super().__init__()
        self.setupUi(self)

        self.matrix_width = 50
        self.matrix_height = 30

        self.setWindowTitle("Matrix-App")

        self.matrix = matrix

        self.renderer       = RenderManager(self.matrix_width, self.matrix_height, 30)
        self.sine_mode      = SineWaveMode(self.matrix_width,self.matrix_height)
        self.saw_mode       = SawtoothMode(self.matrix_width,self.matrix_height)
        self.rect_mode      = RectangularMode(self.matrix_width,self.matrix_height)
        self.rain_mode      = RaindropsMode(self.matrix_width,self.matrix_height)
        self.rainbow_mode   = RainbowMode(self.matrix_width,self.matrix_height)
        self.img_mode       = GifMode(self.matrix_width,self.matrix_height)

        self.renderer.AddMode('sine', self.sine_mode)
        self.renderer.AddMode('sawtooth', self.saw_mode)
        self.renderer.AddMode('rectangular', self.rect_mode)
        self.renderer.AddMode('rain', self.rain_mode)
        self.renderer.AddMode('rainbow', self.rainbow_mode)
        self.renderer.AddMode('image', self.img_mode)

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
        self.loadTab(TabImage(self.img_mode))
        tab_preview = TabPreview(self.matrix_width, self.matrix_height)
        self.loadTab(tab_preview)

        self.tab_bar.currentChanged.connect(self.stack.setCurrentIndex)

        self.renderer.SetVirtualMatrix(tab_preview.preview_matrix)
        self.renderer.Start()

        #print(self.renderer.GetModes())
        self.cb_mode_selection.addItems(self.renderer.GetModes())
        self.cb_mode_selection.currentIndexChanged.connect(self.selectPreviewMode)
        self.selectPreviewMode()

        # show main window
        self.show()

    def loadTab(self, content: QWidget) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(content)
        self.stack.addWidget(page)

    def selectPreviewMode(self):
        mode = self.cb_mode_selection.currentText()
        self.renderer.PreviewMode(mode)


