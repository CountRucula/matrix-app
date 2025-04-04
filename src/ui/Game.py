# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem, QIcon, QKeyEvent
from PySide6.QtCore import QSize, Qt

from pathlib import Path
from typing import Literal

# genrated ui
from qt.generated.UI_game import Ui_TabGame

from rendering.RenderManager import RenderManager
from rendering.GameMode import SnakeMode, Direction, PongMode

class TabGame(QWidget, Ui_TabGame):
    def __init__(self, renderer: RenderManager, width: int, height: int):
        super().__init__()
        self.setupUi(self)

        # load game icons
        self.load_icons()

        # create game modes
        self.snake_mode = SnakeMode(width, height)
        self.pong_mode = PongMode(width, height)

        # register modes 
        self.renderer = renderer
        self.renderer.AddMode('Snake', self.snake_mode)
        self.renderer.AddMode('Pong', self.pong_mode)

        # register callbacks
        self.btn_snake.clicked.connect(lambda: self.select_game('Snake'))
        self.btn_pong.clicked.connect(lambda: self.select_game('Pong'))
        self.btn_start.clicked.connect(self.start_game)
        self.btn_preview.clicked.connect(self.preview_game)

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

    def select_game(self, mode: Literal['Snake', 'Pong']):
        self.btn_pong.setChecked(False)
        self.btn_snake.setChecked(False)

        if mode == 'Snake':
            self.btn_snake.setChecked(True)
        
        elif mode == 'Pong':
            self.btn_pong.setChecked(True)

        self.selected_game = mode

    def start_game(self):
        self.renderer.SelectMode(self.selected_game)

    def preview_game(self):
        self.renderer.PreviewMode(self.selected_game)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Up:
            self.snake_mode.change_direction(Direction.UP)
            self.pong_mode.set_player_dir(2, -1)

        elif event.key() == Qt.Key_Down:
            self.snake_mode.change_direction(Direction.DOWN)
            self.pong_mode.set_player_dir(2, 1)

        elif event.key() == Qt.Key_Left:
            self.snake_mode.change_direction(Direction.LEFT)
            
        elif event.key() == Qt.Key_Right:
            self.snake_mode.change_direction(Direction.RIGHT)

        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.snake_mode.start_pause()
            self.pong_mode.game_start()

        elif event.key() == Qt.Key_W:
            self.pong_mode.set_player_dir(1, -1)

        elif event.key() == Qt.Key_S:
            self.pong_mode.set_player_dir(1, 1)

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.pong_mode.set_player_dir(2, 0)

        elif event.key() == Qt.Key_Down:
            self.pong_mode.set_player_dir(2, 0)

        elif event.key() == Qt.Key_W:
            self.pong_mode.set_player_dir(1, 0)

        elif event.key() == Qt.Key_S:
            self.pong_mode.set_player_dir(1, 0)

        return super().keyReleaseEvent(event)


        