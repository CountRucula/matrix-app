# QT-Lib
from PySide6.QtWidgets import QWidget

# genrated ui
from qt.generated.UI_text import Ui_TabText

class TabText(QWidget, Ui_TabText):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
