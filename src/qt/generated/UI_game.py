# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_TabGame(object):
    def setupUi(self, TabGame):
        if not TabGame.objectName():
            TabGame.setObjectName(u"TabGame")
        TabGame.resize(963, 623)
        self.verticalLayout = QVBoxLayout(TabGame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_snake = QToolButton(TabGame)
        self.btn_snake.setObjectName(u"btn_snake")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_snake.sizePolicy().hasHeightForWidth())
        self.btn_snake.setSizePolicy(sizePolicy)
        self.btn_snake.setMinimumSize(QSize(150, 200))
        self.btn_snake.setIconSize(QSize(128, 128))
        self.btn_snake.setCheckable(True)
        self.btn_snake.setAutoRepeat(False)
        self.btn_snake.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.btn_snake, 0, 0, 1, 1)

        self.btn_pong = QToolButton(TabGame)
        self.btn_pong.setObjectName(u"btn_pong")
        sizePolicy.setHeightForWidth(self.btn_pong.sizePolicy().hasHeightForWidth())
        self.btn_pong.setSizePolicy(sizePolicy)
        self.btn_pong.setMinimumSize(QSize(150, 200))
        self.btn_pong.setIconSize(QSize(128, 128))
        self.btn_pong.setCheckable(True)
        self.btn_pong.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.btn_pong, 0, 1, 1, 1)

        self.btn_pacman = QToolButton(TabGame)
        self.btn_pacman.setObjectName(u"btn_pacman")
        sizePolicy.setHeightForWidth(self.btn_pacman.sizePolicy().hasHeightForWidth())
        self.btn_pacman.setSizePolicy(sizePolicy)
        self.btn_pacman.setMinimumSize(QSize(150, 200))
        self.btn_pacman.setIconSize(QSize(128, 128))
        self.btn_pacman.setCheckable(True)
        self.btn_pacman.setAutoRepeat(False)
        self.btn_pacman.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.btn_pacman, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_preview = QPushButton(TabGame)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout_2.addWidget(self.btn_preview)

        self.btn_start = QPushButton(TabGame)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_2.addWidget(self.btn_start)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TabGame)

        QMetaObject.connectSlotsByName(TabGame)
    # setupUi

    def retranslateUi(self, TabGame):
        TabGame.setWindowTitle(QCoreApplication.translate("TabGame", u"Form", None))
        self.btn_snake.setText(QCoreApplication.translate("TabGame", u"Snake", None))
        self.btn_pong.setText(QCoreApplication.translate("TabGame", u"Pong", None))
        self.btn_pacman.setText(QCoreApplication.translate("TabGame", u"PacMan", None))
        self.btn_preview.setText(QCoreApplication.translate("TabGame", u"Preview", None))
        self.btn_start.setText(QCoreApplication.translate("TabGame", u"Start", None))
    # retranslateUi

