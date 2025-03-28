# QT-Lib
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
import PySide6.QtCore as QtCore

from pathlib import Path

from rendering.RenderManager import RenderManager
from rendering.ImageMode import ImageMode, GifMode

# genrated ui
from qt.generated.UI_image import Ui_TabImage

class TabImage(QWidget, Ui_TabImage):
    def __init__(self, renderer: RenderManager, width, height):
        super().__init__()
        self.setupUi(self)
        self.renderer = renderer

        # button callbacks
        self.btn_open_file_dialog.clicked.connect(self.openFileDialog)
        self.btn_display.clicked.connect(self.displayImage)
        self.btn_preview.clicked.connect(self.previewImage)

        self.selected_file = None
        self.img = None

        self.mode = GifMode(width, height)
        self.mode_name = 'Image'
        self.renderer.AddMode(self.mode_name, self.mode)

    def openFileDialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        dialog.setNameFilter("Images (*.png *.jpg *.svg *.gif)")

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if len(filenames) > 0:
                self.selected_file = Path(filenames[0])
                print(f'selected file: "{self.selected_file}"')

                self.img_path.setText(str(self.selected_file))
                self.img = QPixmap(self.selected_file)
                self.update_pixmap_size()
                self.mode.open_img(str(self.selected_file))

    def displayImage(self):
        self.renderer.SelectMode(self.mode_name)

    def previewImage(self):
        self.renderer.PreviewMode(self.mode_name)

    def resizeEvent(self, event):
        # Resize the pixmap when the window resizes
        if self.img:
            self.update_pixmap_size()
        super().resizeEvent(event)

    def update_pixmap_size(self):
        # Scale the pixmap to fit the label
        scaled_img = self.img.scaled(
            self.img_container.size(),
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation,
        )
        self.img_container.setPixmap(scaled_img)
