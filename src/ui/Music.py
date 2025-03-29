# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem, QIcon
import PySide6.QtCore as QtCore

from pathlib import Path
from typing import Literal

from rendering.RenderManager import RenderManager
from rendering.MusicMode import FrequencyBandsMode, TimelineMode

# genrated ui
from qt.generated.UI_music import Ui_TabMusic

class TabMusic(QWidget, Ui_TabMusic):
    def __init__(self, renderer: RenderManager, width, height):
        super().__init__()
        self.setupUi(self)
        self.renderer = renderer
        
        self.load_icons()

        self.timeline_mode  = TimelineMode(width, height)
        self.bands_mode     = FrequencyBandsMode(width, height)

        self.renderer.AddMode('Timeline', self.timeline_mode)
        self.renderer.AddMode('Timeline-Dual', self.timeline_mode)
        self.renderer.AddMode('Freq-Bands', self.bands_mode)

        # register callbacks
        self.btn_mode_timeline.clicked.connect(lambda: self.select_animation('Timeline'))
        self.btn_mode_timeline_dual.clicked.connect(lambda: self.select_animation('Timeline-Dual'))
        self.btn_mode_bands.clicked.connect(lambda: self.select_animation('Freq-Bands'))

        self.btn_display.clicked.connect(self.start_animation)
        self.btn_preview.clicked.connect(self.preview_animation)

    def load_icons(self):
        assets = (Path(__file__).parent / '../../assets').resolve()
        
        # timeline icon
        icon = QIcon(str(assets / 'timeline-icon.png'))
        self.btn_mode_timeline.setIcon(icon)
        self.btn_mode_timeline.setProperty('class', 'mode-btn')

        # timeline dual icon
        icon = QIcon(str(assets / 'timeline-dual-icon.png'))
        self.btn_mode_timeline_dual.setIcon(icon)
        self.btn_mode_timeline_dual.setProperty('class', 'mode-btn')

        # frequency bands dual icon
        icon = QIcon(str(assets / 'bands-icon.png'))
        self.btn_mode_bands.setIcon(icon)
        self.btn_mode_bands.setProperty('class', 'mode-btn')

    def select_animation(self, mode: Literal['Timeline', 'Timeline-Dual', 'Freq-Bands']):
        self.btn_mode_timeline.setChecked(False)
        self.btn_mode_timeline_dual.setChecked(False)
        self.btn_mode_bands.setChecked(False)

        if mode == 'Timeline':
            self.btn_mode_timeline.setChecked(True)
        
        elif mode == 'Timeline-Dual':
            self.btn_mode_timeline_dual.setChecked(True)

        elif mode == 'Freq-Bands':
            self.btn_mode_bands.setChecked(True)

        self.selected_animation = mode

    def start_animation(self):
        self.renderer.SelectMode(self.selected_animation)

    def preview_animation(self):
        self.renderer.PreviewMode(self.selected_animation)

