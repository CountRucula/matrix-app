# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem
import PySide6.QtCore as QtCore

# genrated ui
from qt.generated.UI_music import Ui_TabMusic

class TabMusic(QWidget, Ui_TabMusic):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.populate_combo_box()

    self.btn_start_stop.clicked.connect(self.onStartStop)
    self.lbl_status.setText('stopped')
    self.running = False

  def populate_combo_box(self):
    modes = ['Timeline', 'Timeline Dual', 'Circle']

    self.visualisation_mode.addItems(modes)

  def onStartStop(self):
    if self.running:
      self.running = False
      self.lbl_status.setText('stopped')
      self.btn_start_stop.setText('Start')

    else:
      self.running = True
      self.lbl_status.setText('running')
      self.btn_start_stop.setText('Stop')