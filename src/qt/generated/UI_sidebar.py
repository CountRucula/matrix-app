# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        if not sidebar.objectName():
            sidebar.setObjectName(u"sidebar")
        sidebar.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sidebar.sizePolicy().hasHeightForWidth())
        sidebar.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(sidebar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.btn_toggle = QPushButton(sidebar)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy1)
        self.btn_toggle.setAutoFillBackground(False)
        self.btn_toggle.setFlat(True)

        self.gridLayout.addWidget(self.btn_toggle, 0, 1, 4, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.tabs = QListWidget(sidebar)
        self.tabs.setObjectName(u"tabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy2)
        self.tabs.setMinimumSize(QSize(400, 0))

        self.gridLayout.addWidget(self.tabs, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        QWidget.setTabOrder(self.tabs, self.btn_toggle)

        self.retranslateUi(sidebar)

        QMetaObject.connectSlotsByName(sidebar)
    # setupUi

    def retranslateUi(self, sidebar):
        sidebar.setWindowTitle(QCoreApplication.translate("sidebar", u"Form", None))
        self.btn_toggle.setText("")
    # retranslateUi

