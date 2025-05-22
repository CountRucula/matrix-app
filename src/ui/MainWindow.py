from pathlib import Path
import numpy as np
from typing import Literal
from functools import partial

# QT-Lib
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabBar, QLabel, QListWidget, QToolButton, QAbstractButton, QSlider, QDoubleSpinBox,QComboBox
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt, QPoint, QObject, QSize, QTimer, QPropertyAnimation, QRect

# genrated ui
from qt.generated.UI_MainWindow import Ui_MainWindow

# tabs
from ui.Settings import TabSettings
from ui.Image import TabImage
from ui.Music import TabMusic
from ui.Animation import TabAnimation
from ui.Preview import TabPreview
from ui.Game import TabGame
from ui.Input import InputDevice, JoystickState

from ui.Sidebar import Sidebar

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
        self.input_dev.btn_clicked.connect(self.handle_btns)
        self.input_dev.btn_clicked.connect(self.switch_input_mode)
        self.input_dev.joystick_changed.connect(self.handle_joystick)
        self.input_dev.poti_moved.connect(self.handle_poti)

        # render manager
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
        self.btn_close.setIconSize(QSize(40,40))
        self.btn_close.clicked.connect(self.close)
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        
        self.btn_sidebar.hide()
        
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
        
        # tab-bar
        self.btn_tab_settings.setProperty('class', 'tab-btn')
        self.btn_tab_anim.setProperty('class', 'tab-btn')
        self.btn_tab_game.setProperty('class', 'tab-btn')
        self.btn_tab_music.setProperty('class', 'tab-btn')
        self.btn_tab_image.setProperty('class', 'tab-btn')
        self.btn_tab_preview.setProperty('class', 'tab-btn')
        self.tab_bar = [
            self.btn_tab_settings,
            self.btn_tab_anim,
            self.btn_tab_game,
            self.btn_tab_music,
            self.btn_tab_image,
            self.btn_tab_preview
        ]
        for i, btn in enumerate(self.tab_bar):
            btn.clicked.connect(partial(self.show_tab, i))
        self.show_tab(0)

        # add preview matrix & hardware matrix to renderer
        self.renderer.SetVirtualMatrix(self.tab_preview.preview_matrix)
        self.renderer.SetMatrix(self.matrix)
        self.renderer.Start()
        
        # fps timer
        self.fps_timer = QTimer(self)
        self.fps_timer.timeout.connect(self.updateFPS)
        self.fps_timer.setSingleShot(False)
        self.fps_timer.start(1000)

        # page navigation
        self.buildWidgetMap()
        self.input_mode: Literal['ui', 'game'] = 'ui'
        self.focus_coord = (0,0)
        self.focus_widget = self.get_widget(self.focus_coord)
        self.focus_widget.setFocus()
        self.widget_activated = False

        # show main window
        self.showFullScreen()
        
    def show_tab(self, tab: int):
        for i, btn in enumerate(self.tab_bar):
            btn.setChecked(i == tab)
            
        print(f"show tab {tab}")
        self.stack.setCurrentIndex(tab)
        
    def switch_input_mode(self, *args):
        if self.input_mode == 'game':
            self.input_mode = 'ui'
            self.lbl_input_mode.setText('UI')
            self.widget_activated = False
            
        else:
            self.input_mode = 'game'
            self.lbl_input_mode.setText('Game')
        
        
    def handle_btns(self, btn: int) :
        # forward to game mode
        if self.input_mode == 'game':
            self.tab_game.handle_button(btn)
            return
        
        # click button
        if isinstance(self.focus_widget, QAbstractButton):
            self.focus_widget.click()
            return    

        # toggle widget activation
        self.widget_activated = not self.widget_activated
        
    def handle_joystick(self, stick: int, state: JoystickState):
        # forward to game mode
        if self.input_mode == 'game':
            self.tab_game.handle_joystick(stick, state)
            return

        # manipulate widget
        if self.widget_activated:
            if isinstance(self.focus_widget, QSlider):
                match state:
                    case JoystickState.Left:
                        self.focus_widget.keyPressEvent(QKeyEvent(QKeyEvent.Type.KeyPress, Qt.Key.Key_Left, Qt.KeyboardModifier.NoModifier, text="l", autorep=True, count=100))
                        
                    case JoystickState.Right:
                        self.focus_widget.keyPressEvent(QKeyEvent(QKeyEvent.Type.KeyPress, Qt.Key.Key_Right, Qt.KeyboardModifier.NoModifier, text="r", autorep=True, count=100))
                        
                    case _:
                        self.focus_widget.keyReleaseEvent(QKeyEvent(QKeyEvent.Type.KeyRelease, Qt.Key.Key_Left, Qt.KeyboardModifier.NoModifier, text="l", autorep=False, count=0))
                        self.focus_widget.keyReleaseEvent(QKeyEvent(QKeyEvent.Type.KeyRelease, Qt.Key.Key_Right, Qt.KeyboardModifier.NoModifier, text="r", autorep=False, count=0))
                        
            elif isinstance(self.focus_widget, (QDoubleSpinBox, QComboBox)):
                match state:
                    case JoystickState.Top:
                        self.focus_widget.keyPressEvent(QKeyEvent(QKeyEvent.Type.KeyPress, Qt.Key.Key_Up, Qt.KeyboardModifier.NoModifier, text="l", autorep=True, count=100))
                        
                    case JoystickState.Bottom:
                        self.focus_widget.keyPressEvent(QKeyEvent(QKeyEvent.Type.KeyPress, Qt.Key.Key_Down, Qt.KeyboardModifier.NoModifier, text="l", autorep=True, count=100))
                        
                    case _:
                        self.focus_widget.keyReleaseEvent(QKeyEvent(QKeyEvent.Type.KeyRelease, Qt.Key.Key_Up, Qt.KeyboardModifier.NoModifier, text="l", autorep=False, count=0))
                        self.focus_widget.keyReleaseEvent(QKeyEvent(QKeyEvent.Type.KeyRelease, Qt.Key.Key_Down, Qt.KeyboardModifier.NoModifier, text="l", autorep=False, count=0))
                
            return

        if state == JoystickState.Middle:
            return

        # navigate
        print()
        print(f"current: {self.focus_coord}, {self.focus_widget.objectName()}")
        x,y = self.focus_coord
        
        old_widget = self.get_widget(self.focus_coord)
        new_widget = None
        limited = False

        while (new_widget == old_widget or new_widget is None) and not limited:
            match state:
                case JoystickState.Left:   x -= 1
                case JoystickState.Right:  x += 1
                case JoystickState.Top:    y -= 1
                case JoystickState.Bottom: y += 1
                case _: break
                
            (x,y), limited = self.limit_coords((x,y))
            new_widget = self.get_widget((x,y))
            
            if limited:
                print("coord limited")
            
        # new widget found
        if new_widget is not None:
            self.focus_widget.clearFocus()

            self.focus_coord = (x,y)
            self.focus_widget = new_widget
            self.focus_widget.setFocus()

            self.tab_settings.scrollArea.ensureWidgetVisible(self.focus_widget)
            self.tab_animation.scrollArea.ensureWidgetVisible(self.focus_widget)
            self.tab_music.scrollArea.ensureWidgetVisible(self.focus_widget)
        
        print(f"new: {self.focus_coord}, {self.focus_widget.objectName()}")


    def handle_poti(self, poti: int, pos: float):
        self.tab_game.handle_poti(poti, pos)
    
    def get_widget(self, coord):
        x,y = coord
        
        # get row
        if y >= len(self.widgets):
            row_idx = y - len(self.widgets)
            tab_widgets = self.tab_widgets[self.stack.currentIndex()]()
            row = tab_widgets[row_idx]
        else:
            row = self.widgets[y]
            
        # get widget
        return row[x]
    
    def limit_coords(self, coord):
        x,y = coord
        
        # limit x
        tab_widgets = self.tab_widgets[self.stack.currentIndex()]()
        y = max(0, min(len(self.widgets)+len(tab_widgets)-1, y))
        
        # get row
        if y >= len(self.widgets):
            row_idx = y - len(self.widgets)
            row = tab_widgets[row_idx]
        else:
            row = self.widgets[y]
            
        # limit x
        x = max(0, min(len(row)-1, x))
        
        new_coord = (x,y)
        
        return new_coord, new_coord != coord


    def buildWidgetMap(self):
        self.widgets = [[self.btn_close, self.btn_tab_settings, self.btn_tab_anim, self.btn_tab_game, self.btn_tab_music, self.btn_tab_image, self.btn_tab_preview]]
        
        self.tab_widgets = [
            self.tab_settings.get_widget_map,
            self.tab_animation.get_widget_map,
            self.tab_game.get_widget_map,
            self.tab_music.get_widget_map,
            self.tab_image.get_widget_map,
            self.tab_preview.get_widget_map,
        ]
        
    def toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar.hide_with_animation()
        else:
            self.sidebar.show_with_animation(self.stack.currentIndex())

    def loadTab(self, name: str, content: QWidget) -> None:
        # self.sidebar.tabs.addItem(name)
        # self.tab_bar.addTab(name)
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
        match event.key():
            case Qt.Key.Key_W:
                self.handle_joystick(0, JoystickState.Top)
                
            case Qt.Key.Key_S:
                self.handle_joystick(0, JoystickState.Bottom)
                
            case Qt.Key.Key_A:
                self.handle_joystick(0, JoystickState.Left)
                
            case Qt.Key.Key_D:
                self.handle_joystick(0, JoystickState.Right)
                
            case Qt.Key.Key_P:
                self.handle_btns(0)
                
            case Qt.Key.Key_G:
                self.switch_input_mode()
            
        if self.input_mode == 'game':
            self.tab_game.keyPressEvent(event)
        # super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if self.input_mode == 'game':
            self.tab_game.keyReleaseEvent(event)

        # return super().keyReleaseEvent(event)

    def closeEvent(self, event):
        self.renderer.DisableMarixOutput()
        self.matrix.disconnect()
        event.accept() # let the window close