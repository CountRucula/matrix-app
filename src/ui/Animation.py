# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem
import PySide6.QtCore as QtCore

# genrated ui
from qt.generated.UI_animation import Ui_TabAnimation

class TabAnimation(QWidget, Ui_TabAnimation):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    self.populate_animation_types()

  def populate_animation_types(self):
    animations = ['sine', 'rectangle', 'sawtooth', 'rainbow', 'raindrops', 'fire']

    self.cb_animation_type.addItems(animations)
