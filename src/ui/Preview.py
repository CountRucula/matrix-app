# QT-Lib
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem
import PySide6.QtCore as QtCore

from colorsys import hsv_to_rgb
import numpy as np

# genrated ui
from qt.generated.UI_preview import Ui_TabPreview

# custom widget
from ui.LEDMatrix import LEDMatrixWidget

class TabPreview(QWidget, Ui_TabPreview):
    def __init__(self, width, height):
        super().__init__()
        self.setupUi(self)

        self.preview_matrix = LEDMatrixWidget(height, width, 20, self)
        self.verticalLayout.addWidget(self.preview_matrix)

        led_data = TabPreview.create_rainbow_matrix()

        self.preview_matrix.display(led_data)
        
    def get_widget_map(self):
        return []

    def resizeEvent(self, event):
        self.preview_matrix.update_led_size()
        return super().resizeEvent(event)
    
    def create_rainbow_matrix(rows=20, cols=50):
        """Create a rainbow gradient on an LED matrix with RGB values."""
        matrix = np.zeros((rows, cols, 3), dtype=np.uint8)

        for row in range(rows):
            for col in range(cols):
                # Map the column position to the hue (0-1)
                hue = col / cols  
                # Full saturation and brightness for vibrant colors
                rgb = hsv_to_rgb(hue, 1.0, 1.0)
                # Convert float (0-1) to 8-bit color (0-255)
                matrix[row, col] = (np.array(rgb) * 255).astype(np.uint8)

        return matrix
