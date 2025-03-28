# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_TabAnimation(object):
    def setupUi(self, TabAnimation):
        if not TabAnimation.objectName():
            TabAnimation.setObjectName(u"TabAnimation")
        TabAnimation.resize(843, 563)
        self.gridLayout = QGridLayout(TabAnimation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_mode_sine = QToolButton(TabAnimation)
        self.btn_mode_sine.setObjectName(u"btn_mode_sine")
        self.btn_mode_sine.setMinimumSize(QSize(150, 200))
        self.btn_mode_sine.setIconSize(QSize(128, 128))
        self.btn_mode_sine.setCheckable(True)
        self.btn_mode_sine.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_sine, 0, 0, 1, 1)

        self.btn_mode_rect = QToolButton(TabAnimation)
        self.btn_mode_rect.setObjectName(u"btn_mode_rect")
        self.btn_mode_rect.setMinimumSize(QSize(150, 200))
        self.btn_mode_rect.setIconSize(QSize(128, 128))
        self.btn_mode_rect.setCheckable(True)
        self.btn_mode_rect.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_rect, 0, 1, 1, 1)

        self.btn_mode_sawtooth = QToolButton(TabAnimation)
        self.btn_mode_sawtooth.setObjectName(u"btn_mode_sawtooth")
        self.btn_mode_sawtooth.setMinimumSize(QSize(150, 200))
        self.btn_mode_sawtooth.setIconSize(QSize(128, 128))
        self.btn_mode_sawtooth.setCheckable(True)
        self.btn_mode_sawtooth.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_sawtooth, 0, 2, 1, 1)

        self.btn_mode_rainbow = QToolButton(TabAnimation)
        self.btn_mode_rainbow.setObjectName(u"btn_mode_rainbow")
        self.btn_mode_rainbow.setMinimumSize(QSize(150, 200))
        self.btn_mode_rainbow.setIconSize(QSize(128, 128))
        self.btn_mode_rainbow.setCheckable(True)
        self.btn_mode_rainbow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_rainbow, 0, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_preview = QPushButton(TabAnimation)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout.addWidget(self.btn_preview)

        self.btn_display = QPushButton(TabAnimation)
        self.btn_display.setObjectName(u"btn_display")

        self.horizontalLayout.addWidget(self.btn_display)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(TabAnimation)

        QMetaObject.connectSlotsByName(TabAnimation)
    # setupUi

    def retranslateUi(self, TabAnimation):
        TabAnimation.setWindowTitle(QCoreApplication.translate("TabAnimation", u"Form", None))
        self.btn_mode_sine.setText(QCoreApplication.translate("TabAnimation", u"Sine", None))
        self.btn_mode_rect.setText(QCoreApplication.translate("TabAnimation", u"Rectangle", None))
        self.btn_mode_sawtooth.setText(QCoreApplication.translate("TabAnimation", u"Sawtooth", None))
        self.btn_mode_rainbow.setText(QCoreApplication.translate("TabAnimation", u"Rainbow", None))
        self.btn_preview.setText(QCoreApplication.translate("TabAnimation", u"Preview", None))
        self.btn_display.setText(QCoreApplication.translate("TabAnimation", u"Display", None))
    # retranslateUi

