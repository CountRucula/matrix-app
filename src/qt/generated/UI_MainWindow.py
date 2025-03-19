# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.title_layout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.horizontalSpacer)

        self.btn_close = QToolButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setAutoFillBackground(False)

        self.title_layout.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.title_layout)

        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")

        self.verticalLayout.addWidget(self.stack)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setObjectName(u"footer_layout")
        self.lbl_fps = QLabel(self.centralwidget)
        self.lbl_fps.setObjectName(u"lbl_fps")

        self.footer_layout.addWidget(self.lbl_fps)

        self.lbl_text_current_mode = QLabel(self.centralwidget)
        self.lbl_text_current_mode.setObjectName(u"lbl_text_current_mode")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_text_current_mode.sizePolicy().hasHeightForWidth())
        self.lbl_text_current_mode.setSizePolicy(sizePolicy)

        self.footer_layout.addWidget(self.lbl_text_current_mode)

        self.lbl_current_mode = QLabel(self.centralwidget)
        self.lbl_current_mode.setObjectName(u"lbl_current_mode")

        self.footer_layout.addWidget(self.lbl_current_mode)

        self.lbl_new_mode = QLabel(self.centralwidget)
        self.lbl_new_mode.setObjectName(u"lbl_new_mode")
        self.lbl_new_mode.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.footer_layout.addWidget(self.lbl_new_mode)

        self.cb_mode_selection = QComboBox(self.centralwidget)
        self.cb_mode_selection.setObjectName(u"cb_mode_selection")

        self.footer_layout.addWidget(self.cb_mode_selection)

        self.btn_activate_mode = QPushButton(self.centralwidget)
        self.btn_activate_mode.setObjectName(u"btn_activate_mode")

        self.footer_layout.addWidget(self.btn_activate_mode)


        self.verticalLayout.addLayout(self.footer_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_fps.setText("")
        self.lbl_text_current_mode.setText(QCoreApplication.translate("MainWindow", u"Current Mode:", None))
        self.lbl_current_mode.setText("")
        self.lbl_new_mode.setText(QCoreApplication.translate("MainWindow", u"New Mode:", None))
        self.btn_activate_mode.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
    # retranslateUi

