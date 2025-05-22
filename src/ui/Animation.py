# QT-Lib
from PySide6.QtWidgets import QWidget, QSlider, QLabel, QScroller
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

        QScroller.grabGesture(self.scrollArea.viewport(), QScroller.TouchGesture)
        
        # widgets
        self.widgets_grid_sine = [[self.btn_mode_sine, self.btn_mode_rect, self.btn_mode_sawtooth, self.btn_mode_rainbow],
                                  [self.sld_sine_f]*4,
                                  [self.sld_sine_waves]*4,
                                  [self.sld_sine_a]*4,
                                  [self.sld_sine_offset]*4,
                                  [self.sld_sine_phase]*4,
                                  [self.btn_preview, self.btn_preview, self.btn_preview, self.btn_display]]

        self.widgets_grid_rect = [[self.btn_mode_sine, self.btn_mode_rect, self.btn_mode_sawtooth, self.btn_mode_rainbow],
                                  [self.sld_rect_f]*4,
                                  [self.sld_rect_waves]*4,
                                  [self.sld_rect_a]*4,
                                  [self.sld_rect_offset]*4,
                                  [self.sld_rect_phase]*4,
                                  [self.sld_rect_duty]*4,
                                  [self.btn_preview, self.btn_preview, self.btn_preview, self.btn_display]]

        self.widgets_grid_saw  = [[self.btn_mode_sine, self.btn_mode_rect, self.btn_mode_sawtooth, self.btn_mode_rainbow],
                                  [self.sld_saw_f]*4,
                                  [self.sld_saw_waves]*4,
                                  [self.sld_saw_a]*4,
                                  [self.sld_saw_offset]*4,
                                  [self.sld_saw_phase]*4,
                                  [self.sld_saw_symmetry]*4,
                                  [self.btn_preview, self.btn_preview, self.btn_preview, self.btn_display]]

        self.widgets_grid_rain = [[self.btn_mode_sine, self.btn_mode_rect, self.btn_mode_sawtooth, self.btn_mode_rainbow],
                                  [self.btn_preview, self.btn_preview, self.btn_preview, self.btn_display]]

        self.active_widgets_grid = self.widgets_grid_sine
        
        # register callbacks
        self.btn_mode_sine.clicked.connect(lambda: self.select_animation('Sine'))
        self.btn_mode_rect.clicked.connect(lambda: self.select_animation('Rectangle'))
        self.btn_mode_sawtooth.clicked.connect(lambda: self.select_animation('Sawtooth'))
        self.btn_mode_rainbow.clicked.connect(lambda: self.select_animation('Rainbow'))

        self.btn_preview.clicked.connect(self.preview_animation)
        self.btn_display.clicked.connect(self.start_animation)
        
        # mode settings
        # sine mode settings
        self.connect_param(self.sld_sine_f, self.lbl_sine_f, self.sine_mode.set_f, transform=lambda v: v/10)
        self.connect_param(self.sld_sine_a, self.lbl_sine_a, self.sine_mode.set_a)
        self.connect_param(self.sld_sine_offset, self.lbl_sine_offset, self.sine_mode.set_offset)
        self.connect_param(self.sld_sine_phase, self.lbl_sine_phase, self.sine_mode.set_phase)
        self.connect_param(self.sld_sine_waves, self.lbl_sine_waves, self.sine_mode.set_waves)

        # rectangle mode settings
        self.connect_param(self.sld_rect_f, self.lbl_rect_f, self.rect_mode.set_f, transform=lambda v: v/10)
        self.connect_param(self.sld_rect_a, self.lbl_rect_a, self.rect_mode.set_a)
        self.connect_param(self.sld_rect_offset, self.lbl_rect_offset, self.rect_mode.set_offset)
        self.connect_param(self.sld_rect_phase, self.lbl_rect_phase, self.rect_mode.set_phase)
        self.connect_param(self.sld_rect_waves, self.lbl_rect_waves, self.rect_mode.set_waves)
        self.connect_param(self.sld_rect_duty, self.lbl_rect_duty, self.rect_mode.set_duty)

        # sawtooth mode settings
        self.connect_param(self.sld_saw_f, self.lbl_saw_f, self.saw_mode.set_f, transform=lambda v: v/10)
        self.connect_param(self.sld_saw_a, self.lbl_saw_a, self.saw_mode.set_a)
        self.connect_param(self.sld_saw_offset, self.lbl_saw_offset, self.saw_mode.set_offset)
        self.connect_param(self.sld_saw_phase, self.lbl_saw_phase, self.saw_mode.set_phase)
        self.connect_param(self.sld_saw_waves, self.lbl_saw_waves, self.saw_mode.set_waves)
        self.connect_param(self.sld_saw_symmetry, self.lbl_saw_symmetry, self.saw_mode.set_symmetry)
        
        # Default Selection
        self.select_animation('Sine')
        
    def get_widget_map(self):
        match self.selected_animation:
            case 'Sine':
                return self.widgets_grid_sine
            
            case 'Rectangle':
                return self.widgets_grid_rect
            
            case 'Sawtooth':
                return self.widgets_grid_saw
            
            case 'Rainbow':
                return self.widgets_grid_rain
            
            case _:
                return [[]]

    def connect_param(self, slider: QSlider, label: QLabel, setter: callable, fmt: str ="{}", transform: callable = None):
        slider.sliderMoved.connect(lambda val: self.param_changed(slider, val, label, setter, fmt, transform))
        slider.valueChanged.connect(lambda val: self.param_changed(slider, val, label, setter, fmt, transform))
        self.param_changed(slider, slider.value(), label, setter, fmt, transform)
        
    def param_changed(self, slider: QSlider, val: any, label: QLabel, setter: callable, fmt: str, transform: callable = None):
        minimum = slider.minimum()
        step = slider.singleStep()

        val = round((val - minimum)/step) * step + minimum
        slider.setValue(val)
        
        if transform is not None:
            val = transform(val)

        label.setText(fmt.format(val))
        setter(val)

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
            self.mode_settings.setCurrentIndex(0)
        
        elif mode == 'Rectangle':
            self.btn_mode_rect.setChecked(True)
            self.mode_settings.setCurrentIndex(1)

        elif mode == 'Sawtooth':
            self.btn_mode_sawtooth.setChecked(True)
            self.mode_settings.setCurrentIndex(2)

        elif mode == 'Rainbow':
            self.btn_mode_rainbow.setChecked(True)
            self.mode_settings.setCurrentIndex(3)

        self.selected_animation = mode

    def start_animation(self):
        self.renderer.SelectMode(self.selected_animation)

    def preview_animation(self):
        self.renderer.PreviewMode(self.selected_animation)

