from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QSize
import numpy as np

class LEDMatrixWidget(QWidget):
    def __init__(self, rows=8, cols=8, led_size=20, parent=None):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols

        self.update_led_size()

        self.setMinimumSize(10,10)

        # Initialize all LEDs as off
        self.led_colors = np.zeros((rows, cols, 3), np.uint8)

        # Set minimum size to fit the matrix
        self.setMinimumSize(cols * led_size, rows * led_size)

    def sizeHint(self):
        return QSize(self.cols * self.led_size, self.rows * self.led_size)

    def set_led_color(self, row, col, color):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.led_colors[row, col] = color
            self.update()

    def display(self, colors):
        self.led_colors = colors
        self.update()

    def update_led_size(self):
        size    = self.parentWidget().size()
        width   = size.width() - 20
        height  = size.height() - 20

        self.led_size = max(1, min(width // self.cols, height // self.rows))

        self.offset_x = (width  - self.led_size*self.cols) // 2
        self.offset_y = (height - self.led_size*self.rows) // 2

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.led_size + self.offset_x
                y = row * self.led_size + self.offset_y

                # Choose color based on LED state
                color = QColor(*self.led_colors[row, col])
                painter.setBrush(color)

                # Draw LED circle
                painter.drawEllipse(x + 2, y + 2, self.led_size - 4, self.led_size - 4)

    def clear_matrix(self):
        """Turn off all LEDs."""
        self.led_states = np.zeros_like(self.led_colors)
        self.update()
