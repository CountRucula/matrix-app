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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setBaseSize(QSize(800, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.lbl_matrix_status = QLabel(self.centralwidget)
        self.lbl_matrix_status.setObjectName(u"lbl_matrix_status")
        sizePolicy.setHeightForWidth(self.lbl_matrix_status.sizePolicy().hasHeightForWidth())
        self.lbl_matrix_status.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_matrix_status)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.lbl_controller_status = QLabel(self.centralwidget)
        self.lbl_controller_status.setObjectName(u"lbl_controller_status")
        sizePolicy.setHeightForWidth(self.lbl_controller_status.sizePolicy().hasHeightForWidth())
        self.lbl_controller_status.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_controller_status)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.lbl_input_mode = QLabel(self.centralwidget)
        self.lbl_input_mode.setObjectName(u"lbl_input_mode")
        sizePolicy.setHeightForWidth(self.lbl_input_mode.sizePolicy().hasHeightForWidth())
        self.lbl_input_mode.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_input_mode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.header_layout = QHBoxLayout()
        self.header_layout.setSpacing(20)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(-1, -1, -1, 0)
        self.btn_sidebar = QToolButton(self.centralwidget)
        self.btn_sidebar.setObjectName(u"btn_sidebar")
        self.btn_sidebar.setMinimumSize(QSize(40, 40))
        self.btn_sidebar.setAutoFillBackground(False)

        self.header_layout.addWidget(self.btn_sidebar)

        self.btn_close = QToolButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(40, 40))
        self.btn_close.setAutoFillBackground(False)

        self.header_layout.addWidget(self.btn_close)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.btn_tab_settings = QPushButton(self.centralwidget)
        self.btn_tab_settings.setObjectName(u"btn_tab_settings")
        self.btn_tab_settings.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_tab_settings)

        self.btn_tab_anim = QPushButton(self.centralwidget)
        self.btn_tab_anim.setObjectName(u"btn_tab_anim")
        self.btn_tab_anim.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_tab_anim)

        self.btn_tab_game = QPushButton(self.centralwidget)
        self.btn_tab_game.setObjectName(u"btn_tab_game")
        self.btn_tab_game.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_tab_game)

        self.btn_tab_music = QPushButton(self.centralwidget)
        self.btn_tab_music.setObjectName(u"btn_tab_music")
        self.btn_tab_music.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_tab_music)

        self.btn_tab_image = QPushButton(self.centralwidget)
        self.btn_tab_image.setObjectName(u"btn_tab_image")
        self.btn_tab_image.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_tab_image)

        self.btn_tab_preview = QPushButton(self.centralwidget)
        self.btn_tab_preview.setObjectName(u"btn_tab_preview")
        self.btn_tab_preview.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_tab_preview)


        self.header_layout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_layout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.header_layout)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.stack)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setObjectName(u"footer_layout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.footer_layout.addWidget(self.label_2)

        self.lbl_preview_mode = QLabel(self.centralwidget)
        self.lbl_preview_mode.setObjectName(u"lbl_preview_mode")

        self.footer_layout.addWidget(self.lbl_preview_mode)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.footer_layout.addWidget(self.line_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.footer_layout.addWidget(self.label_4)

        self.lbl_current_mode = QLabel(self.centralwidget)
        self.lbl_current_mode.setObjectName(u"lbl_current_mode")

        self.footer_layout.addWidget(self.lbl_current_mode)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.footer_layout.addWidget(self.line_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.footer_layout.addWidget(self.label_3)

        self.lbl_fps = QLabel(self.centralwidget)
        self.lbl_fps.setObjectName(u"lbl_fps")

        self.footer_layout.addWidget(self.lbl_fps)


        self.verticalLayout.addLayout(self.footer_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Matrix Status:", None))
        self.lbl_matrix_status.setText(QCoreApplication.translate("MainWindow", u"disconnected", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Controller Status:", None))
        self.lbl_controller_status.setText(QCoreApplication.translate("MainWindow", u"disconnected", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input Mode", None))
        self.lbl_input_mode.setText(QCoreApplication.translate("MainWindow", u"UI", None))
        self.btn_sidebar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_tab_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_tab_anim.setText(QCoreApplication.translate("MainWindow", u"Animation", None))
        self.btn_tab_game.setText(QCoreApplication.translate("MainWindow", u"Game", None))
        self.btn_tab_music.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.btn_tab_image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.btn_tab_preview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Preview Mode: ", None))
        self.lbl_preview_mode.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Current Mode:", None))
        self.lbl_current_mode.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.lbl_fps.setText("")
    # retranslateUi

