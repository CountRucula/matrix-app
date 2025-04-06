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
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_TabSettings(object):
    def setupUi(self, TabSettings):
        if not TabSettings.objectName():
            TabSettings.setObjectName(u"TabSettings")
        TabSettings.resize(800, 480)
        self.verticalLayout = QVBoxLayout(TabSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.btn_controller_connect = QPushButton(TabSettings)
        self.btn_controller_connect.setObjectName(u"btn_controller_connect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_controller_connect.sizePolicy().hasHeightForWidth())
        self.btn_controller_connect.setSizePolicy(sizePolicy)
        self.btn_controller_connect.setMinimumSize(QSize(200, 0))
        self.btn_controller_connect.setMaximumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(12)
        self.btn_controller_connect.setFont(font)

        self.gridLayout_2.addWidget(self.btn_controller_connect, 2, 4, 1, 1)

        self.cb_matrix_ports = QComboBox(TabSettings)
        self.cb_matrix_ports.setObjectName(u"cb_matrix_ports")
        sizePolicy.setHeightForWidth(self.cb_matrix_ports.sizePolicy().hasHeightForWidth())
        self.cb_matrix_ports.setSizePolicy(sizePolicy)
        self.cb_matrix_ports.setMinimumSize(QSize(200, 0))
        self.cb_matrix_ports.setMaximumSize(QSize(400, 50))
        self.cb_matrix_ports.setFont(font)
        self.cb_matrix_ports.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_matrix_ports, 1, 2, 1, 1)

        self.lbl_calibration = QLabel(TabSettings)
        self.lbl_calibration.setObjectName(u"lbl_calibration")
        font1 = QFont()
        font1.setBold(True)
        self.lbl_calibration.setFont(font1)
        self.lbl_calibration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_calibration, 10, 1, 1, 4)

        self.lbl_matrix_conn = QLabel(TabSettings)
        self.lbl_matrix_conn.setObjectName(u"lbl_matrix_conn")
        self.lbl_matrix_conn.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.lbl_matrix_conn.setFont(font2)
        self.lbl_matrix_conn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_matrix_conn, 0, 1, 1, 4)

        self.btn_matrix_connect = QPushButton(TabSettings)
        self.btn_matrix_connect.setObjectName(u"btn_matrix_connect")
        sizePolicy.setHeightForWidth(self.btn_matrix_connect.sizePolicy().hasHeightForWidth())
        self.btn_matrix_connect.setSizePolicy(sizePolicy)
        self.btn_matrix_connect.setMinimumSize(QSize(200, 0))
        self.btn_matrix_connect.setMaximumSize(QSize(400, 50))
        self.btn_matrix_connect.setFont(font)

        self.gridLayout_2.addWidget(self.btn_matrix_connect, 1, 4, 1, 1)

        self.btn_cal_poti_right_min = QPushButton(TabSettings)
        self.btn_cal_poti_right_min.setObjectName(u"btn_cal_poti_right_min")
        self.btn_cal_poti_right_min.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_right_min.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_right_min, 12, 2, 1, 1)

        self.btn_test_gamma_green = QPushButton(TabSettings)
        self.btn_test_gamma_green.setObjectName(u"btn_test_gamma_green")
        self.btn_test_gamma_green.setMinimumSize(QSize(200, 0))
        self.btn_test_gamma_green.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_gamma_green, 7, 4, 1, 1)

        self.lbl_controller_port = QLabel(TabSettings)
        self.lbl_controller_port.setObjectName(u"lbl_controller_port")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_controller_port.sizePolicy().hasHeightForWidth())
        self.lbl_controller_port.setSizePolicy(sizePolicy1)
        self.lbl_controller_port.setFont(font)
        self.lbl_controller_port.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_controller_port, 2, 1, 1, 1)

        self.sb_gamma_blue = QDoubleSpinBox(TabSettings)
        self.sb_gamma_blue.setObjectName(u"sb_gamma_blue")
        self.sb_gamma_blue.setMinimumSize(QSize(200, 0))
        self.sb_gamma_blue.setMaximumSize(QSize(400, 50))
        self.sb_gamma_blue.setFrame(True)
        self.sb_gamma_blue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_blue.setDecimals(1)
        self.sb_gamma_blue.setMinimum(1.000000000000000)
        self.sb_gamma_blue.setMaximum(3.000000000000000)
        self.sb_gamma_blue.setSingleStep(0.100000000000000)
        self.sb_gamma_blue.setValue(2.200000000000000)

        self.gridLayout_2.addWidget(self.sb_gamma_blue, 8, 2, 1, 1)

        self.label_4 = QLabel(TabSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 8, 1, 1, 1)

        self.line_2 = QFrame(TabSettings)
        self.line_2.setObjectName(u"line_2")
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QSize(0, 10))
        self.line_2.setBaseSize(QSize(0, 10))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 1, 1, 4)

        self.label_2 = QLabel(TabSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)

        self.btn_test_gamma_blue = QPushButton(TabSettings)
        self.btn_test_gamma_blue.setObjectName(u"btn_test_gamma_blue")
        self.btn_test_gamma_blue.setMinimumSize(QSize(200, 0))
        self.btn_test_gamma_blue.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_gamma_blue, 8, 4, 1, 1)

        self.cb_controller_ports = QComboBox(TabSettings)
        self.cb_controller_ports.setObjectName(u"cb_controller_ports")
        sizePolicy.setHeightForWidth(self.cb_controller_ports.sizePolicy().hasHeightForWidth())
        self.cb_controller_ports.setSizePolicy(sizePolicy)
        self.cb_controller_ports.setMinimumSize(QSize(200, 0))
        self.cb_controller_ports.setMaximumSize(QSize(400, 50))
        self.cb_controller_ports.setFont(font)
        self.cb_controller_ports.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_controller_ports, 2, 2, 1, 1)

        self.label_3 = QLabel(TabSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 7, 1, 1, 1)

        self.btn_cal_poti_left_max = QPushButton(TabSettings)
        self.btn_cal_poti_left_max.setObjectName(u"btn_cal_poti_left_max")
        self.btn_cal_poti_left_max.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_left_max.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_left_max, 11, 4, 1, 1)

        self.lbl_gamma_corr = QLabel(TabSettings)
        self.lbl_gamma_corr.setObjectName(u"lbl_gamma_corr")
        self.lbl_gamma_corr.setFont(font1)
        self.lbl_gamma_corr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_gamma_corr, 5, 1, 1, 4)

        self.sb_gamma_green = QDoubleSpinBox(TabSettings)
        self.sb_gamma_green.setObjectName(u"sb_gamma_green")
        self.sb_gamma_green.setMinimumSize(QSize(200, 0))
        self.sb_gamma_green.setMaximumSize(QSize(400, 50))
        self.sb_gamma_green.setFrame(True)
        self.sb_gamma_green.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_green.setDecimals(1)
        self.sb_gamma_green.setMinimum(1.000000000000000)
        self.sb_gamma_green.setMaximum(3.000000000000000)
        self.sb_gamma_green.setSingleStep(0.100000000000000)
        self.sb_gamma_green.setValue(2.200000000000000)

        self.gridLayout_2.addWidget(self.sb_gamma_green, 7, 2, 1, 1)

        self.btn_cal_poti_right_max = QPushButton(TabSettings)
        self.btn_cal_poti_right_max.setObjectName(u"btn_cal_poti_right_max")
        self.btn_cal_poti_right_max.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_right_max.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_right_max, 12, 4, 1, 1)

        self.btn_refresh_ports = QToolButton(TabSettings)
        self.btn_refresh_ports.setObjectName(u"btn_refresh_ports")
        self.btn_refresh_ports.setBaseSize(QSize(30, 30))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.btn_refresh_ports.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_refresh_ports, 1, 3, 2, 1)

        self.btn_cal_poti_left_min = QPushButton(TabSettings)
        self.btn_cal_poti_left_min.setObjectName(u"btn_cal_poti_left_min")
        self.btn_cal_poti_left_min.setMinimumSize(QSize(200, 0))
        self.btn_cal_poti_left_min.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_cal_poti_left_min, 11, 2, 1, 1)

        self.btn_test_gamma_red = QPushButton(TabSettings)
        self.btn_test_gamma_red.setObjectName(u"btn_test_gamma_red")
        sizePolicy.setHeightForWidth(self.btn_test_gamma_red.sizePolicy().hasHeightForWidth())
        self.btn_test_gamma_red.setSizePolicy(sizePolicy)
        self.btn_test_gamma_red.setMinimumSize(QSize(200, 0))
        self.btn_test_gamma_red.setMaximumSize(QSize(400, 50))

        self.gridLayout_2.addWidget(self.btn_test_gamma_red, 6, 4, 1, 1)

        self.label_5 = QLabel(TabSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 11, 1, 1, 1)

        self.label_6 = QLabel(TabSettings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 12, 1, 1, 1)

        self.lbl_matrix_port = QLabel(TabSettings)
        self.lbl_matrix_port.setObjectName(u"lbl_matrix_port")
        sizePolicy1.setHeightForWidth(self.lbl_matrix_port.sizePolicy().hasHeightForWidth())
        self.lbl_matrix_port.setSizePolicy(sizePolicy1)
        self.lbl_matrix_port.setFont(font)
        self.lbl_matrix_port.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_matrix_port, 1, 1, 1, 1)

        self.sb_gamma_red = QDoubleSpinBox(TabSettings)
        self.sb_gamma_red.setObjectName(u"sb_gamma_red")
        self.sb_gamma_red.setMinimumSize(QSize(200, 0))
        self.sb_gamma_red.setMaximumSize(QSize(400, 50))
        self.sb_gamma_red.setFrame(True)
        self.sb_gamma_red.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_red.setDecimals(1)
        self.sb_gamma_red.setMinimum(1.000000000000000)
        self.sb_gamma_red.setMaximum(3.000000000000000)
        self.sb_gamma_red.setSingleStep(0.100000000000000)
        self.sb_gamma_red.setValue(2.200000000000000)

        self.gridLayout_2.addWidget(self.sb_gamma_red, 6, 2, 1, 1)

        self.line_3 = QFrame(TabSettings)
        self.line_3.setObjectName(u"line_3")
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QSize(0, 10))
        self.line_3.setBaseSize(QSize(0, 10))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 9, 1, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TabSettings)

        QMetaObject.connectSlotsByName(TabSettings)
    # setupUi

    def retranslateUi(self, TabSettings):
        TabSettings.setWindowTitle(QCoreApplication.translate("TabSettings", u"Form", None))
        self.btn_controller_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.lbl_calibration.setText(QCoreApplication.translate("TabSettings", u"Calibration", None))
        self.lbl_matrix_conn.setText(QCoreApplication.translate("TabSettings", u"Serial Connections", None))
        self.btn_matrix_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.btn_cal_poti_right_min.setText(QCoreApplication.translate("TabSettings", u"min", None))
        self.btn_test_gamma_green.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.lbl_controller_port.setText(QCoreApplication.translate("TabSettings", u"Controller", None))
        self.label_4.setText(QCoreApplication.translate("TabSettings", u"Blue", None))
        self.label_2.setText(QCoreApplication.translate("TabSettings", u"Red", None))
        self.btn_test_gamma_blue.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.label_3.setText(QCoreApplication.translate("TabSettings", u"Green", None))
        self.btn_cal_poti_left_max.setText(QCoreApplication.translate("TabSettings", u"max", None))
        self.lbl_gamma_corr.setText(QCoreApplication.translate("TabSettings", u"Gamma Correction", None))
        self.btn_cal_poti_right_max.setText(QCoreApplication.translate("TabSettings", u"max", None))
        self.btn_refresh_ports.setText("")
        self.btn_cal_poti_left_min.setText(QCoreApplication.translate("TabSettings", u"min", None))
        self.btn_test_gamma_red.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.label_5.setText(QCoreApplication.translate("TabSettings", u"Poti left", None))
        self.label_6.setText(QCoreApplication.translate("TabSettings", u"Poti right", None))
        self.lbl_matrix_port.setText(QCoreApplication.translate("TabSettings", u"Matrix", None))
    # retranslateUi

