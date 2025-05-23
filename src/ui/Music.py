# QT-Lib
from PySide6.QtWidgets import QWidget, QSlider, QLabel, QScroller
from PySide6.QtGui import QStandardItem, QIcon
import PySide6.QtCore as QtCore

from pathlib import Path
from typing import Literal

from rendering.RenderManager import RenderManager
from rendering.MusicMode import FrequencyBandsMode, TimelineMode, TimelineDualMode

# genrated ui
from qt.generated.UI_music import Ui_TabMusic

class TabMusic(QWidget, Ui_TabMusic):
    def __init__(self, renderer: RenderManager, width, height):
        super().__init__()
        self.setupUi(self)
        self.renderer = renderer
        
        self.load_icons()

        self.timeline_mode       = TimelineMode(width, height)
        self.timeline_dual_mode  = TimelineDualMode(width, height)
        self.bands_mode          = FrequencyBandsMode(width, height)

        self.renderer.AddMode('Timeline', self.timeline_mode)
        self.renderer.AddMode('Timeline-Dual', self.timeline_dual_mode)
        self.renderer.AddMode('Spectrum', self.bands_mode)
        
        QScroller.grabGesture(self.scrollArea.viewport(), QScroller.TouchGesture)
        self.buildWidgetMap()

        # register callbacks
        self.btn_mode_timeline.clicked.connect(lambda: self.select_animation('Timeline'))
        self.btn_mode_timeline_dual.clicked.connect(lambda: self.select_animation('Timeline-Dual'))
        self.btn_mode_bands.clicked.connect(lambda: self.select_animation('Spectrum'))

        self.btn_display.clicked.connect(self.start_animation)
        self.btn_preview.clicked.connect(self.preview_animation)
        
        # mode settings
        self.select_animation(mode='Timeline')

        # bands settings
        self.connect_param(self.sld_bands_bin_width, self.lbl_bands_bin_width, self.bands_mode.set_bin_width)
        self.connect_param(self.sld_bands_spacing, self.lbl_bands_spacing, self.bands_mode.set_spacing)
        self.connect_param(self.sld_bands_a_max, self.lbl_bands_a_max, self.bands_mode.set_a_max)
        self.connect_param(self.sld_bands_a_min, self.lbl_bands_a_min, self.bands_mode.set_a_min)
        self.connect_param(self.sld_bands_f_max, self.lbl_bands_f_max, self.bands_mode.set_f_max)
        self.connect_param(self.sld_bands_f_min, self.lbl_bands_f_min, self.bands_mode.set_f_min)
        
        # timeline settings
        self.connect_param(self.sld_timeline_sensitivity, self.lbl_timeline_sensitivity, self.timeline_mode.set_sensitivity)
        
        # timeline dual settings
        self.connect_param(self.sld_timelinedual_sensitivity, self.lbl_timelinedual_sensitivity, self.timeline_dual_mode.set_sensitivity)
        
    def buildWidgetMap(self):
        self.widget_map_timeline = [[self.btn_mode_timeline, self.btn_mode_timeline_dual, self.btn_mode_bands],
                                    [self.sld_timeline_sensitivity]*3,
                                    [self.btn_preview, self.btn_preview, self.btn_display]]

        self.widget_map_timeline_dual = [[self.btn_mode_timeline, self.btn_mode_timeline_dual, self.btn_mode_bands],
                                    [self.sld_timelinedual_sensitivity]*3,
                                    [self.btn_preview, self.btn_preview, self.btn_display]]
        
        self.widget_map_spectrum = [[self.btn_mode_timeline, self.btn_mode_timeline_dual, self.btn_mode_bands],
                                    [self.sld_bands_bin_width]*3,
                                    [self.sld_bands_spacing]*3,
                                    [self.sld_bands_a_max]*3,
                                    [self.sld_bands_a_min]*3, 
                                    [self.sld_bands_f_max]*3,
                                    [self.sld_bands_f_min]*3,
                                    [self.btn_preview, self.btn_preview, self.btn_display]]
        
    def get_widget_map(self):
        match self.selected_animation:
            case 'Timeline':
                return self.widget_map_timeline
            
            case 'Timeline-Dual':
                return self.widget_map_timeline_dual
            
            case 'Spectrum':
                return self.widget_map_spectrum
        
    def connect_param(self, slider: QSlider, label: QLabel, setter: callable, fmt: str ="{}"):
        slider.sliderMoved.connect(lambda val: self.param_changed(slider, val, label, setter, fmt))
        slider.valueChanged.connect(lambda val: self.param_changed(slider, val, label, setter, fmt))
        self.param_changed(slider, slider.value(), label, setter, fmt)
        
    def param_changed(self, slider: QSlider, val: any, label: QLabel, setter: callable, fmt: str):
        minimum = slider.minimum()
        step = slider.singleStep()

        val = round((val - minimum)/step) * step + minimum
        slider.setValue(val)
        label.setText(fmt.format(val))
        setter(val)
        
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

    def select_animation(self, mode: Literal['Timeline', 'Timeline-Dual', 'Spectrum']):
        self.btn_mode_timeline.setChecked(False)
        self.btn_mode_timeline_dual.setChecked(False)
        self.btn_mode_bands.setChecked(False)

        if mode == 'Timeline':
            self.btn_mode_timeline.setChecked(True)
            self.mode_settings.setCurrentIndex(0)
        
        elif mode == 'Timeline-Dual':
            self.btn_mode_timeline_dual.setChecked(True)
            self.mode_settings.setCurrentIndex(1)

        elif mode == 'Spectrum':
            self.btn_mode_bands.setChecked(True)
            self.mode_settings.setCurrentIndex(2)

        self.selected_animation = mode

    def start_animation(self):
        self.renderer.SelectMode(self.selected_animation)

    def preview_animation(self):
        self.renderer.PreviewMode(self.selected_animation)

