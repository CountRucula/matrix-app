# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QToolButton,
    QVBoxLayout, QWidget)

class Ui_TabSettings(object):
    def setupUi(self, TabSettings):
        if not TabSettings.objectName():
            TabSettings.setObjectName(u"TabSettings")
        TabSettings.resize(800, 559)
        self.verticalLayout = QVBoxLayout(TabSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.scrollArea = QScrollArea(TabSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -13, 741, 946))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QSize(0, 10))
        self.line_3.setBaseSize(QSize(0, 10))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 14, 1, 1, 4)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(0, 70))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 8, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(0, 70))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 12, 1, 1, 1)

        self.btn_refresh_ports = QToolButton(self.scrollAreaWidgetContents)
        self.btn_refresh_ports.setObjectName(u"btn_refresh_ports")
        self.btn_refresh_ports.setBaseSize(QSize(30, 30))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.btn_refresh_ports.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_refresh_ports, 1, 3, 2, 1)

        self.lbl_matrix_conn = QLabel(self.scrollAreaWidgetContents)
        self.lbl_matrix_conn.setObjectName(u"lbl_matrix_conn")
        self.lbl_matrix_conn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        self.lbl_matrix_conn.setFont(font)
        self.lbl_matrix_conn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_matrix_conn, 0, 1, 1, 4)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 70))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 17, 1, 1, 1)

        self.cb_controller_ports = QComboBox(self.scrollAreaWidgetContents)
        self.cb_controller_ports.setObjectName(u"cb_controller_ports")
        sizePolicy.setHeightForWidth(self.cb_controller_ports.sizePolicy().hasHeightForWidth())
        self.cb_controller_ports.setSizePolicy(sizePolicy)
        self.cb_controller_ports.setMinimumSize(QSize(200, 0))
        self.cb_controller_ports.setMaximumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.cb_controller_ports.setFont(font1)
        self.cb_controller_ports.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_controller_ports, 2, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(0, 70))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 11, 1, 1, 1)

        self.btn_test_gamma_blue = QPushButton(self.scrollAreaWidgetContents)
        self.btn_test_gamma_blue.setObjectName(u"btn_test_gamma_blue")
        self.btn_test_gamma_blue.setMinimumSize(QSize(200, 0))
        self.btn_test_gamma_blue.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_gamma_blue, 8, 4, 1, 1)

        self.sb_gamma_green = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_gamma_green.setObjectName(u"sb_gamma_green")
        self.sb_gamma_green.setMinimumSize(QSize(200, 0))
        self.sb_gamma_green.setMaximumSize(QSize(400, 50))
        self.sb_gamma_green.setFrame(True)
        self.sb_gamma_green.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_green.setDecimals(1)
        self.sb_gamma_green.setMinimum(1.000000000000000)
        self.sb_gamma_green.setMaximum(5.000000000000000)
        self.sb_gamma_green.setSingleStep(0.100000000000000)
        self.sb_gamma_green.setValue(2.200000000000000)

        self.gridLayout_2.addWidget(self.sb_gamma_green, 7, 2, 1, 1)

        self.btn_cal_poti_left_min = QPushButton(self.scrollAreaWidgetContents)
        self.btn_cal_poti_left_min.setObjectName(u"btn_cal_poti_left_min")
        self.btn_cal_poti_left_min.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_left_min.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_left_min, 16, 2, 1, 1)

        self.sb_gamma_red = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_gamma_red.setObjectName(u"sb_gamma_red")
        self.sb_gamma_red.setMinimumSize(QSize(200, 0))
        self.sb_gamma_red.setMaximumSize(QSize(400, 50))
        self.sb_gamma_red.setFrame(True)
        self.sb_gamma_red.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_red.setDecimals(1)
        self.sb_gamma_red.setMinimum(1.000000000000000)
        self.sb_gamma_red.setMaximum(5.000000000000000)
        self.sb_gamma_red.setSingleStep(0.100000000000000)
        self.sb_gamma_red.setValue(2.200000000000000)

        self.gridLayout_2.addWidget(self.sb_gamma_red, 6, 2, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QSize(0, 10))
        self.line_4.setBaseSize(QSize(0, 10))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 9, 1, 1, 4)

        self.btn_test_gamma_green = QPushButton(self.scrollAreaWidgetContents)
        self.btn_test_gamma_green.setObjectName(u"btn_test_gamma_green")
        self.btn_test_gamma_green.setMinimumSize(QSize(200, 0))
        self.btn_test_gamma_green.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_gamma_green, 7, 4, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 70))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 70))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 16, 1, 1, 1)

        self.btn_controller_connect = QPushButton(self.scrollAreaWidgetContents)
        self.btn_controller_connect.setObjectName(u"btn_controller_connect")
        sizePolicy.setHeightForWidth(self.btn_controller_connect.sizePolicy().hasHeightForWidth())
        self.btn_controller_connect.setSizePolicy(sizePolicy)
        self.btn_controller_connect.setMinimumSize(QSize(200, 0))
        self.btn_controller_connect.setMaximumSize(QSize(400, 50))
        self.btn_controller_connect.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_controller_connect, 2, 4, 1, 1)

        self.btn_matrix_connect = QPushButton(self.scrollAreaWidgetContents)
        self.btn_matrix_connect.setObjectName(u"btn_matrix_connect")
        sizePolicy.setHeightForWidth(self.btn_matrix_connect.sizePolicy().hasHeightForWidth())
        self.btn_matrix_connect.setSizePolicy(sizePolicy)
        self.btn_matrix_connect.setMinimumSize(QSize(200, 0))
        self.btn_matrix_connect.setMaximumSize(QSize(400, 50))
        self.btn_matrix_connect.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_matrix_connect, 1, 4, 1, 1)

        self.btn_cal_poti_right_min = QPushButton(self.scrollAreaWidgetContents)
        self.btn_cal_poti_right_min.setObjectName(u"btn_cal_poti_right_min")
        self.btn_cal_poti_right_min.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_right_min.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_right_min, 17, 2, 1, 1)

        self.lbl_controller_port = QLabel(self.scrollAreaWidgetContents)
        self.lbl_controller_port.setObjectName(u"lbl_controller_port")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_controller_port.sizePolicy().hasHeightForWidth())
        self.lbl_controller_port.setSizePolicy(sizePolicy2)
        self.lbl_controller_port.setMinimumSize(QSize(0, 70))
        self.lbl_controller_port.setFont(font1)
        self.lbl_controller_port.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_controller_port, 2, 1, 1, 1)

        self.lbl_calibration = QLabel(self.scrollAreaWidgetContents)
        self.lbl_calibration.setObjectName(u"lbl_calibration")
        font2 = QFont()
        font2.setBold(True)
        self.lbl_calibration.setFont(font2)
        self.lbl_calibration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_calibration, 15, 1, 1, 4)

        self.lbl_gamma_corr = QLabel(self.scrollAreaWidgetContents)
        self.lbl_gamma_corr.setObjectName(u"lbl_gamma_corr")
        self.lbl_gamma_corr.setFont(font2)
        self.lbl_gamma_corr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_gamma_corr, 5, 1, 1, 4)

        self.cb_matrix_ports = QComboBox(self.scrollAreaWidgetContents)
        self.cb_matrix_ports.setObjectName(u"cb_matrix_ports")
        sizePolicy.setHeightForWidth(self.cb_matrix_ports.sizePolicy().hasHeightForWidth())
        self.cb_matrix_ports.setSizePolicy(sizePolicy)
        self.cb_matrix_ports.setMinimumSize(QSize(200, 0))
        self.cb_matrix_ports.setMaximumSize(QSize(400, 50))
        self.cb_matrix_ports.setFont(font1)
        self.cb_matrix_ports.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_matrix_ports, 1, 2, 1, 1)

        self.btn_cal_poti_left_max = QPushButton(self.scrollAreaWidgetContents)
        self.btn_cal_poti_left_max.setObjectName(u"btn_cal_poti_left_max")
        self.btn_cal_poti_left_max.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_left_max.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_left_max, 16, 4, 1, 1)

        self.btn_test_gamma_red = QPushButton(self.scrollAreaWidgetContents)
        self.btn_test_gamma_red.setObjectName(u"btn_test_gamma_red")
        sizePolicy.setHeightForWidth(self.btn_test_gamma_red.sizePolicy().hasHeightForWidth())
        self.btn_test_gamma_red.setSizePolicy(sizePolicy)
        self.btn_test_gamma_red.setMinimumSize(QSize(200, 0))
        self.btn_test_gamma_red.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_gamma_red, 6, 4, 1, 1)

        self.lbl_matrix_port = QLabel(self.scrollAreaWidgetContents)
        self.lbl_matrix_port.setObjectName(u"lbl_matrix_port")
        sizePolicy2.setHeightForWidth(self.lbl_matrix_port.sizePolicy().hasHeightForWidth())
        self.lbl_matrix_port.setSizePolicy(sizePolicy2)
        self.lbl_matrix_port.setMinimumSize(QSize(0, 70))
        self.lbl_matrix_port.setFont(font1)
        self.lbl_matrix_port.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_matrix_port, 1, 1, 1, 1)

        self.btn_cal_poti_right_max = QPushButton(self.scrollAreaWidgetContents)
        self.btn_cal_poti_right_max.setObjectName(u"btn_cal_poti_right_max")
        self.btn_cal_poti_right_max.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_right_max.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_right_max, 17, 4, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 70))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 7, 1, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QSize(0, 10))
        self.line_2.setBaseSize(QSize(0, 10))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 1, 1, 4)

        self.lbl_color_scale = QLabel(self.scrollAreaWidgetContents)
        self.lbl_color_scale.setObjectName(u"lbl_color_scale")
        self.lbl_color_scale.setFont(font2)
        self.lbl_color_scale.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_color_scale, 10, 1, 1, 4)

        self.sb_gamma_blue = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_gamma_blue.setObjectName(u"sb_gamma_blue")
        self.sb_gamma_blue.setMinimumSize(QSize(200, 0))
        self.sb_gamma_blue.setMaximumSize(QSize(400, 50))
        self.sb_gamma_blue.setFrame(True)
        self.sb_gamma_blue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_blue.setDecimals(1)
        self.sb_gamma_blue.setMinimum(1.000000000000000)
        self.sb_gamma_blue.setMaximum(5.000000000000000)
        self.sb_gamma_blue.setSingleStep(0.100000000000000)
        self.sb_gamma_blue.setValue(2.200000000000000)

        self.gridLayout_2.addWidget(self.sb_gamma_blue, 8, 2, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(0, 70))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 13, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_scale_red = QLabel(self.scrollAreaWidgetContents)
        self.lbl_scale_red.setObjectName(u"lbl_scale_red")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_scale_red.sizePolicy().hasHeightForWidth())
        self.lbl_scale_red.setSizePolicy(sizePolicy3)
        self.lbl_scale_red.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_2.addWidget(self.lbl_scale_red)

        self.sld_scale_red = QSlider(self.scrollAreaWidgetContents)
        self.sld_scale_red.setObjectName(u"sld_scale_red")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sld_scale_red.sizePolicy().hasHeightForWidth())
        self.sld_scale_red.setSizePolicy(sizePolicy4)
        self.sld_scale_red.setMaximum(100)
        self.sld_scale_red.setValue(100)
        self.sld_scale_red.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.sld_scale_red)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 11, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_scale_green = QLabel(self.scrollAreaWidgetContents)
        self.lbl_scale_green.setObjectName(u"lbl_scale_green")
        sizePolicy3.setHeightForWidth(self.lbl_scale_green.sizePolicy().hasHeightForWidth())
        self.lbl_scale_green.setSizePolicy(sizePolicy3)
        self.lbl_scale_green.setMinimumSize(QSize(20, 0))

        self.horizontalLayout.addWidget(self.lbl_scale_green)

        self.sld_scale_green = QSlider(self.scrollAreaWidgetContents)
        self.sld_scale_green.setObjectName(u"sld_scale_green")
        sizePolicy4.setHeightForWidth(self.sld_scale_green.sizePolicy().hasHeightForWidth())
        self.sld_scale_green.setSizePolicy(sizePolicy4)
        self.sld_scale_green.setMaximum(100)
        self.sld_scale_green.setValue(100)
        self.sld_scale_green.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_scale_green)


        self.gridLayout_2.addLayout(self.horizontalLayout, 12, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_scale_blue = QLabel(self.scrollAreaWidgetContents)
        self.lbl_scale_blue.setObjectName(u"lbl_scale_blue")
        sizePolicy3.setHeightForWidth(self.lbl_scale_blue.sizePolicy().hasHeightForWidth())
        self.lbl_scale_blue.setSizePolicy(sizePolicy3)
        self.lbl_scale_blue.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_3.addWidget(self.lbl_scale_blue)

        self.sld_scale_blue = QSlider(self.scrollAreaWidgetContents)
        self.sld_scale_blue.setObjectName(u"sld_scale_blue")
        sizePolicy4.setHeightForWidth(self.sld_scale_blue.sizePolicy().hasHeightForWidth())
        self.sld_scale_blue.setSizePolicy(sizePolicy4)
        self.sld_scale_blue.setMaximum(100)
        self.sld_scale_blue.setValue(100)
        self.sld_scale_blue.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.sld_scale_blue)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 13, 2, 1, 1)

        self.btn_test_scale = QPushButton(self.scrollAreaWidgetContents)
        self.btn_test_scale.setObjectName(u"btn_test_scale")
        self.btn_test_scale.setMinimumSize(QSize(200, 0))
        self.btn_test_scale.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_scale, 12, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(TabSettings)

        QMetaObject.connectSlotsByName(TabSettings)
    # setupUi

    def retranslateUi(self, TabSettings):
        TabSettings.setWindowTitle(QCoreApplication.translate("TabSettings", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("TabSettings", u"Blue", None))
        self.label_8.setText(QCoreApplication.translate("TabSettings", u"Green", None))
        self.btn_refresh_ports.setText("")
        self.lbl_matrix_conn.setText(QCoreApplication.translate("TabSettings", u"Serial Connections", None))
        self.label_6.setText(QCoreApplication.translate("TabSettings", u"Poti right", None))
        self.label_7.setText(QCoreApplication.translate("TabSettings", u"Red", None))
        self.btn_test_gamma_blue.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.btn_cal_poti_left_min.setText(QCoreApplication.translate("TabSettings", u"min", None))
        self.btn_test_gamma_green.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.label_2.setText(QCoreApplication.translate("TabSettings", u"Red", None))
        self.label_5.setText(QCoreApplication.translate("TabSettings", u"Poti left", None))
        self.btn_controller_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.btn_matrix_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.btn_cal_poti_right_min.setText(QCoreApplication.translate("TabSettings", u"min", None))
        self.lbl_controller_port.setText(QCoreApplication.translate("TabSettings", u"Controller", None))
        self.lbl_calibration.setText(QCoreApplication.translate("TabSettings", u"Calibration", None))
        self.lbl_gamma_corr.setText(QCoreApplication.translate("TabSettings", u"Gamma Correction", None))
        self.btn_cal_poti_left_max.setText(QCoreApplication.translate("TabSettings", u"max", None))
        self.btn_test_gamma_red.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.lbl_matrix_port.setText(QCoreApplication.translate("TabSettings", u"Matrix", None))
        self.btn_cal_poti_right_max.setText(QCoreApplication.translate("TabSettings", u"max", None))
        self.label_3.setText(QCoreApplication.translate("TabSettings", u"Green", None))
        self.lbl_color_scale.setText(QCoreApplication.translate("TabSettings", u"Color Scale", None))
        self.label_9.setText(QCoreApplication.translate("TabSettings", u"Blue", None))
        self.lbl_scale_red.setText(QCoreApplication.translate("TabSettings", u"TextLabel", None))
        self.lbl_scale_green.setText(QCoreApplication.translate("TabSettings", u"TextLabel", None))
        self.lbl_scale_blue.setText(QCoreApplication.translate("TabSettings", u"TextLabel", None))
        self.btn_test_scale.setText(QCoreApplication.translate("TabSettings", u"Test", None))
    # retranslateUi

