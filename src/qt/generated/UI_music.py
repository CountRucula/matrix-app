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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_TabMusic(object):
    def setupUi(self, TabMusic):
        if not TabMusic.objectName():
            TabMusic.setObjectName(u"TabMusic")
        TabMusic.resize(400, 300)
        self.gridLayout = QGridLayout(TabMusic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.visualisation_mode = QComboBox(TabMusic)
        self.visualisation_mode.setObjectName(u"visualisation_mode")

        self.gridLayout.addWidget(self.visualisation_mode, 0, 1, 1, 1)

        self.label_3 = QLabel(TabMusic)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label = QLabel(TabMusic)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lbl_status = QLabel(TabMusic)
        self.lbl_status.setObjectName(u"lbl_status")

        self.gridLayout.addWidget(self.lbl_status, 1, 1, 1, 1)

        self.btn_start_stop = QPushButton(TabMusic)
        self.btn_start_stop.setObjectName(u"btn_start_stop")

        self.gridLayout.addWidget(self.btn_start_stop, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.retranslateUi(TabMusic)

        QMetaObject.connectSlotsByName(TabMusic)
    # setupUi

    def retranslateUi(self, TabMusic):
        TabMusic.setWindowTitle(QCoreApplication.translate("TabMusic", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("TabMusic", u"Visualisations-Mode", None))
        self.label.setText(QCoreApplication.translate("TabMusic", u"Status", None))
        self.lbl_status.setText("")
        self.btn_start_stop.setText(QCoreApplication.translate("TabMusic", u"Start", None))
    # retranslateUi

