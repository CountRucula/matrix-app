# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem, QIcon, QKeyEvent
from PySide6.QtCore import QSize, Qt

from pathlib import Path
from typing import Literal

# genrated ui
from qt.generated.UI_game import Ui_TabGame
from ui.Input import InputDevice, JoystickState

from rendering.RenderManager import RenderManager
from rendering.GameMode import SnakeMode, Direction, PongMode, PacManMode

class TabGame(QWidget, Ui_TabGame):
    def __init__(self, input_dev, renderer: RenderManager, width: int, height: int):
        super().__init__()
        self.setupUi(self)

        self.input: InputDevice = input_dev
        self.input.joystick_changed.connect(self.handle_joystick)
        self.input.btn_clicked.connect(self.handle_button)
        self.input.poti_moved.connect(self.handle_poti)
        
        self.buildWidgetMap()

        # load game icons
        self.load_icons()

        # create game modes
        self.snake_mode = SnakeMode(width, height)
        self.pong_mode = PongMode(width, height)
        self.pacman_mode = PacManMode(width, height)

        # register modes 
        self.renderer = renderer
        self.renderer.AddMode('Snake', self.snake_mode)
        self.renderer.AddMode('Pong', self.pong_mode)
        self.renderer.AddMode('Pacman', self.pacman_mode)
        self.select_game('Snake')

        # register callbacks
        self.btn_snake.clicked.connect(lambda: self.select_game('Snake'))
        self.btn_pong.clicked.connect(lambda: self.select_game('Pong'))
        self.btn_pacman.clicked.connect(lambda: self.select_game('Pacman'))
        self.btn_start.clicked.connect(self.start_game)
        self.btn_preview.clicked.connect(self.preview_game)

    def buildWidgetMap(self):
        self.widget_map = [[self.btn_snake, self.btn_pong, self.btn_pacman],
                           [self.btn_preview, self.btn_start]]
        
    def get_widget_map(self):
        return self.widget_map

    def load_icons(self):
        assets = (Path(__file__).parent / '../../assets').resolve()
        
        # snake icon
        icon = QIcon(str(assets / 'snake-icon.png'))
        self.btn_snake.setIcon(icon)
        self.btn_snake.setProperty('class', 'mode-btn')

        # pong icon
        icon = QIcon(str(assets / 'pong-icon.png'))
        self.btn_pong.setIcon(icon)
        self.btn_pong.setProperty('class', 'mode-btn')

        # pacman icon
        icon = QIcon(str(assets / 'pacman-icon.png'))
        self.btn_pacman.setIcon(icon)
        self.btn_pacman.setProperty('class', 'mode-btn')

    def select_game(self, mode: Literal['Snake', 'Pong']):
        self.btn_pong.setChecked(False)
        self.btn_snake.setChecked(False)
        self.btn_pacman.setChecked(False)

        if mode == 'Snake':
            self.btn_snake.setChecked(True)
        
        elif mode == 'Pong':
            self.btn_pong.setChecked(True)

        elif mode == 'Pacman':
            self.btn_pacman.setChecked(True)

        self.selected_game = mode

    def start_game(self):
        self.renderer.SelectMode(self.selected_game)

    def preview_game(self):
        self.renderer.PreviewMode(self.selected_game)

    def handle_joystick(self, stick: int, state: JoystickState):
        match state:
            case JoystickState.Left:
                self.snake_mode.change_direction(Direction.LEFT)
                self.pacman_mode.set_player_dir(Direction.LEFT)

            case JoystickState.Right:
                self.snake_mode.change_direction(Direction.RIGHT)
                self.pacman_mode.set_player_dir(Direction.RIGHT)

            case JoystickState.Top:
                self.snake_mode.change_direction(Direction.UP)
                self.pacman_mode.set_player_dir(Direction.UP)

            case JoystickState.Bottom:
                self.snake_mode.change_direction(Direction.DOWN)
                self.pacman_mode.set_player_dir(Direction.DOWN)

    def handle_button(self, btn: int):
        print("game btn press")
        self.snake_mode.start_pause()
        self.pacman_mode.start_stop()
        self.pong_mode.game_start()

    def handle_poti(self, poti: int, pos: float):
        self.pong_mode.set_player_pos(poti+1, pos)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Up:
            self.snake_mode.change_direction(Direction.UP)
            self.pong_mode.set_player_dir(2, -1)
            self.pacman_mode.set_player_dir(Direction.UP)

        elif event.key() == Qt.Key_Down:
            self.snake_mode.change_direction(Direction.DOWN)
            self.pong_mode.set_player_dir(2, 1)
            self.pacman_mode.set_player_dir(Direction.DOWN)

        elif event.key() == Qt.Key_Left:
            self.snake_mode.change_direction(Direction.LEFT)
            self.pacman_mode.set_player_dir(Direction.LEFT)
            
        elif event.key() == Qt.Key_Right:
            self.snake_mode.change_direction(Direction.RIGHT)
            self.pacman_mode.set_player_dir(Direction.RIGHT)

        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.snake_mode.start_pause()
            self.pong_mode.game_start()
            self.pacman_mode.start_stop()

        elif event.key() == Qt.Key_W:
            self.pong_mode.set_player_dir(1, -1)

        elif event.key() == Qt.Key_S:
            self.pong_mode.set_player_dir(1, 1)

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.pong_mode.set_player_dir(2, 0)
            # self.pacman_mode.set_player_dir(None)

        elif event.key() == Qt.Key_Down:
            self.pong_mode.set_player_dir(2, 0)
            # self.pacman_mode.set_player_dir(None)
            
        elif event.key() == Qt.Key_Left:
            # self.pacman_mode.set_player_dir(None)
            pass

        elif event.key() == Qt.Key_Right:
            # self.pacman_mode.set_player_dir(None)
            pass

        elif event.key() == Qt.Key_W:
            self.pong_mode.set_player_dir(1, 0)

        elif event.key() == Qt.Key_S:
            self.pong_mode.set_player_dir(1, 0)

        return super().keyReleaseEvent(event)


        