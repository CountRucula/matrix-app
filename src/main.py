from PySide6.QtWidgets import QApplication, QWidget
from pathlib import Path
import sys
from qt_material import apply_stylesheet

# Import custom ui-modules
from ui.MainWindow import MainWindow

# import matrix
from matrix.Matrix import Matrix

def main():
  # You need one (and only one) QApplication instance per application.
  # Pass in sys.argv to allow command line arguments for your app.
  # If you know you won't use command line arguments QApplication([]) works too.
  app = QApplication(sys.argv)

  # load stylesheet
  #app.setStyleSheet(Path('./qt/design/MainWindow.qss').read_text())
  stylesheet = (Path(__file__).parent / 'ui/style.css').resolve()
  apply_stylesheet(app, theme='dark_teal.xml', css_file=str(stylesheet))

  # create Matrix
  matrix = Matrix()

  # Create a Qt widget, which will be our window.
  window = MainWindow(matrix)

  # Start the event loop.
  app.exec()

  # Your application won't reach here until you exit and the event
  # loop has stopped.

if __name__ == '__main__':
  main()