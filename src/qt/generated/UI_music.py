# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

class Ui_TabMusic(object):
    def setupUi(self, TabMusic):
        if not TabMusic.objectName():
            TabMusic.setObjectName(u"TabMusic")
        TabMusic.resize(663, 449)
        self.gridLayout = QGridLayout(TabMusic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_status = QLabel(TabMusic)
        self.lbl_status.setObjectName(u"lbl_status")

        self.gridLayout.addWidget(self.lbl_status, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.btn_mode_bands = QToolButton(TabMusic)
        self.btn_mode_bands.setObjectName(u"btn_mode_bands")
        self.btn_mode_bands.setMinimumSize(QSize(150, 200))
        self.btn_mode_bands.setIconSize(QSize(128, 128))
        self.btn_mode_bands.setCheckable(True)
        self.btn_mode_bands.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.btn_mode_bands, 0, 2, 1, 1)

        self.btn_mode_timeline_dual = QToolButton(TabMusic)
        self.btn_mode_timeline_dual.setObjectName(u"btn_mode_timeline_dual")
        self.btn_mode_timeline_dual.setMinimumSize(QSize(150, 200))
        self.btn_mode_timeline_dual.setIconSize(QSize(128, 128))
        self.btn_mode_timeline_dual.setCheckable(True)
        self.btn_mode_timeline_dual.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.btn_mode_timeline_dual, 0, 1, 1, 1)

        self.btn_mode_timeline = QToolButton(TabMusic)
        self.btn_mode_timeline.setObjectName(u"btn_mode_timeline")
        self.btn_mode_timeline.setMinimumSize(QSize(150, 200))
        self.btn_mode_timeline.setIconSize(QSize(128, 128))
        self.btn_mode_timeline.setCheckable(True)
        self.btn_mode_timeline.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.btn_mode_timeline, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_preview = QPushButton(TabMusic)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout.addWidget(self.btn_preview)

        self.btn_display = QPushButton(TabMusic)
        self.btn_display.setObjectName(u"btn_display")

        self.horizontalLayout.addWidget(self.btn_display)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(TabMusic)

        QMetaObject.connectSlotsByName(TabMusic)
    # setupUi

    def retranslateUi(self, TabMusic):
        TabMusic.setWindowTitle(QCoreApplication.translate("TabMusic", u"Form", None))
        self.lbl_status.setText("")
        self.btn_mode_bands.setText(QCoreApplication.translate("TabMusic", u"Frequency Bands", None))
        self.btn_mode_timeline_dual.setText(QCoreApplication.translate("TabMusic", u"Timeline Dual", None))
        self.btn_mode_timeline.setText(QCoreApplication.translate("TabMusic", u"Timeline", None))
        self.btn_preview.setText(QCoreApplication.translate("TabMusic", u"Preview", None))
        self.btn_display.setText(QCoreApplication.translate("TabMusic", u"Display", None))
    # retranslateUi

