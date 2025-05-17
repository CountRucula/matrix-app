# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TabImage(object):
    def setupUi(self, TabImage):
        if not TabImage.objectName():
            TabImage.setObjectName(u"TabImage")
        TabImage.resize(490, 343)
        self.verticalLayout = QVBoxLayout(TabImage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_open_file_dialog = QPushButton(TabImage)
        self.btn_open_file_dialog.setObjectName(u"btn_open_file_dialog")

        self.horizontalLayout.addWidget(self.btn_open_file_dialog)

        self.img_path = QLabel(TabImage)
        self.img_path.setObjectName(u"img_path")
        self.img_path.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.img_path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.img_container = QLabel(TabImage)
        self.img_container.setObjectName(u"img_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_container.sizePolicy().hasHeightForWidth())
        self.img_container.setSizePolicy(sizePolicy)
        self.img_container.setMinimumSize(QSize(10, 10))
        self.img_container.setAutoFillBackground(False)
        self.img_container.setFrameShape(QFrame.Shape.NoFrame)
        self.img_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.img_container)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_preview = QPushButton(TabImage)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout_2.addWidget(self.btn_preview)

        self.btn_display = QPushButton(TabImage)
        self.btn_display.setObjectName(u"btn_display")

        self.horizontalLayout_2.addWidget(self.btn_display)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TabImage)

        QMetaObject.connectSlotsByName(TabImage)
    # setupUi

    def retranslateUi(self, TabImage):
        TabImage.setWindowTitle(QCoreApplication.translate("TabImage", u"Form", None))
        self.btn_open_file_dialog.setText(QCoreApplication.translate("TabImage", u"Open File", None))
        self.img_path.setText("")
        self.img_container.setText("")
        self.btn_preview.setText(QCoreApplication.translate("TabImage", u"Preview", None))
        self.btn_display.setText(QCoreApplication.translate("TabImage", u"Display", None))
    # retranslateUi

