# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem, QIcon
import PySide6.QtCore as QtCore

from pathlib import Path
from typing import Literal

from rendering.RenderManager import RenderManager
from rendering.AnimationMode import SineWaveMode, RectangularMode, SawtoothMode, RaindropsMode, RainbowMode

# genrated ui
from qt.generated.UI_animation import Ui_TabAnimation

class TabAnimation(QWidget, Ui_TabAnimation):
    def __init__(self, renderer: RenderManager, width, height):
        super().__init__()
        self.setupUi(self)

        self.renderer = renderer

        self.sine_mode      = SineWaveMode(width, height)
        self.saw_mode       = SawtoothMode(width, height)
        self.rect_mode      = RectangularMode(width, height)
        self.rain_mode      = RaindropsMode(width, height)
        self.rainbow_mode   = RainbowMode(width, height)

        self.renderer.AddMode('Sine', self.sine_mode)
        self.renderer.AddMode('Sawtooth', self.saw_mode)
        self.renderer.AddMode('Rectangle', self.rect_mode)
        self.renderer.AddMode('Rain', self.rain_mode)
        self.renderer.AddMode('Rainbow', self.rainbow_mode)
        self.load_icons()

        # register callbacks
        self.btn_mode_sine.clicked.connect(lambda: self.select_animation('Sine'))
        self.btn_mode_rect.clicked.connect(lambda: self.select_animation('Rectangle'))
        self.btn_mode_sawtooth.clicked.connect(lambda: self.select_animation('Sawtooth'))
        self.btn_mode_rainbow.clicked.connect(lambda: self.select_animation('Rainbow'))

        self.btn_preview.clicked.connect(self.preview_animation)
        self.btn_display.clicked.connect(self.start_animation)


    def load_icons(self):
        assets = (Path(__file__).parent / '../../assets').resolve()
        
        # sine icon
        icon = QIcon(str(assets / 'sine-icon.png'))
        self.btn_mode_sine.setIcon(icon)
        self.btn_mode_sine.setProperty('class', 'mode-btn')

        # rect icon
        icon = QIcon(str(assets / 'rect-icon.png'))
        self.btn_mode_rect.setIcon(icon)
        self.btn_mode_rect.setProperty('class', 'mode-btn')

        # sawtooth icon
        icon = QIcon(str(assets / 'saw-icon.png'))
        self.btn_mode_sawtooth.setIcon(icon)
        self.btn_mode_sawtooth.setProperty('class', 'mode-btn')

        # rainbow icon
        icon = QIcon(str(assets / 'rainbow-icon.png'))
        self.btn_mode_rainbow.setIcon(icon)
        self.btn_mode_rainbow.setProperty('class', 'mode-btn')

    def select_animation(self, mode: Literal['Sine', 'Rectangle', 'Sawtooth', 'Rainbow']):
        self.btn_mode_sine.setChecked(False)
        self.btn_mode_rect.setChecked(False)
        self.btn_mode_sawtooth.setChecked(False)
        self.btn_mode_rainbow.setChecked(False)

        if mode == 'Sine':
            self.btn_mode_sine.setChecked(True)
        
        elif mode == 'Rectangle':
            self.btn_mode_rect.setChecked(True)

        elif mode == 'Sawtooth':
            self.btn_mode_sawtooth.setChecked(True)

        elif mode == 'Rainbow':
            self.btn_mode_rainbow.setChecked(True)

        self.selected_animation = mode

    def start_animation(self):
        self.renderer.SelectMode(self.selected_animation)

    def preview_animation(self):
        self.renderer.PreviewMode(self.selected_animation)

