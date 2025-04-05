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
        TabSettings.resize(545, 485)
        self.verticalLayout = QVBoxLayout(TabSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_matrix_conn = QLabel(TabSettings)
        self.lbl_matrix_conn.setObjectName(u"lbl_matrix_conn")
        self.lbl_matrix_conn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        self.lbl_matrix_conn.setFont(font)
        self.lbl_matrix_conn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_matrix_conn)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cb_matrix_ports = QComboBox(TabSettings)
        self.cb_matrix_ports.setObjectName(u"cb_matrix_ports")
        font1 = QFont()
        font1.setPointSize(12)
        self.cb_matrix_ports.setFont(font1)
        self.cb_matrix_ports.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_matrix_ports, 0, 1, 1, 1)

        self.lbl_matrix_port = QLabel(TabSettings)
        self.lbl_matrix_port.setObjectName(u"lbl_matrix_port")
        self.lbl_matrix_port.setFont(font1)
        self.lbl_matrix_port.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_matrix_port, 0, 0, 1, 1)

        self.btn_matrix_connect = QPushButton(TabSettings)
        self.btn_matrix_connect.setObjectName(u"btn_matrix_connect")
        self.btn_matrix_connect.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_matrix_connect, 0, 3, 1, 1)

        self.lbl_controller_port = QLabel(TabSettings)
        self.lbl_controller_port.setObjectName(u"lbl_controller_port")
        self.lbl_controller_port.setFont(font1)
        self.lbl_controller_port.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_controller_port, 1, 0, 1, 1)

        self.cb_controller_ports = QComboBox(TabSettings)
        self.cb_controller_ports.setObjectName(u"cb_controller_ports")
        self.cb_controller_ports.setFont(font1)
        self.cb_controller_ports.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_controller_ports, 1, 1, 1, 1)

        self.btn_controller_connect = QPushButton(TabSettings)
        self.btn_controller_connect.setObjectName(u"btn_controller_connect")
        self.btn_controller_connect.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_controller_connect, 1, 3, 1, 1)

        self.btn_refresh_ports = QToolButton(TabSettings)
        self.btn_refresh_ports.setObjectName(u"btn_refresh_ports")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.btn_refresh_ports.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_refresh_ports, 0, 2, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line = QFrame(TabSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.line_2 = QFrame(TabSettings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.lbl_gamma_corr = QLabel(TabSettings)
        self.lbl_gamma_corr.setObjectName(u"lbl_gamma_corr")
        font2 = QFont()
        font2.setBold(True)
        self.lbl_gamma_corr.setFont(font2)
        self.lbl_gamma_corr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_gamma_corr)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.sb_gamma_green = QDoubleSpinBox(TabSettings)
        self.sb_gamma_green.setObjectName(u"sb_gamma_green")
        self.sb_gamma_green.setMinimumSize(QSize(100, 0))
        self.sb_gamma_green.setFrame(True)
        self.sb_gamma_green.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_green.setDecimals(1)
        self.sb_gamma_green.setMinimum(1.000000000000000)
        self.sb_gamma_green.setMaximum(3.000000000000000)
        self.sb_gamma_green.setSingleStep(0.100000000000000)
        self.sb_gamma_green.setValue(2.200000000000000)

        self.gridLayout.addWidget(self.sb_gamma_green, 2, 1, 1, 1)

        self.btn_test_gamma_blue = QPushButton(TabSettings)
        self.btn_test_gamma_blue.setObjectName(u"btn_test_gamma_blue")

        self.gridLayout.addWidget(self.btn_test_gamma_blue, 3, 2, 1, 1)

        self.btn_test_gamma_green = QPushButton(TabSettings)
        self.btn_test_gamma_green.setObjectName(u"btn_test_gamma_green")
        self.btn_test_gamma_green.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.btn_test_gamma_green, 2, 2, 1, 1)

        self.btn_test_gamma_red = QPushButton(TabSettings)
        self.btn_test_gamma_red.setObjectName(u"btn_test_gamma_red")

        self.gridLayout.addWidget(self.btn_test_gamma_red, 0, 2, 1, 1)

        self.sb_gamma_red = QDoubleSpinBox(TabSettings)
        self.sb_gamma_red.setObjectName(u"sb_gamma_red")
        self.sb_gamma_red.setMinimumSize(QSize(100, 0))
        self.sb_gamma_red.setFrame(True)
        self.sb_gamma_red.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_red.setDecimals(1)
        self.sb_gamma_red.setMinimum(1.000000000000000)
        self.sb_gamma_red.setMaximum(3.000000000000000)
        self.sb_gamma_red.setSingleStep(0.100000000000000)
        self.sb_gamma_red.setValue(2.200000000000000)

        self.gridLayout.addWidget(self.sb_gamma_red, 0, 1, 1, 1)

        self.label_3 = QLabel(TabSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.sb_gamma_blue = QDoubleSpinBox(TabSettings)
        self.sb_gamma_blue.setObjectName(u"sb_gamma_blue")
        self.sb_gamma_blue.setMinimumSize(QSize(100, 0))
        self.sb_gamma_blue.setFrame(True)
        self.sb_gamma_blue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sb_gamma_blue.setDecimals(1)
        self.sb_gamma_blue.setMinimum(1.000000000000000)
        self.sb_gamma_blue.setMaximum(3.000000000000000)
        self.sb_gamma_blue.setSingleStep(0.100000000000000)
        self.sb_gamma_blue.setValue(2.200000000000000)

        self.gridLayout.addWidget(self.sb_gamma_blue, 3, 1, 1, 1)

        self.label_4 = QLabel(TabSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(TabSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TabSettings)

        QMetaObject.connectSlotsByName(TabSettings)
    # setupUi

    def retranslateUi(self, TabSettings):
        TabSettings.setWindowTitle(QCoreApplication.translate("TabSettings", u"Form", None))
        self.lbl_matrix_conn.setText(QCoreApplication.translate("TabSettings", u"Hardware Connection", None))
        self.lbl_matrix_port.setText(QCoreApplication.translate("TabSettings", u"Matrix", None))
        self.btn_matrix_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.lbl_controller_port.setText(QCoreApplication.translate("TabSettings", u"Controller", None))
        self.btn_controller_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.btn_refresh_ports.setText("")
        self.lbl_gamma_corr.setText(QCoreApplication.translate("TabSettings", u"Gamma Correction", None))
        self.btn_test_gamma_blue.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.btn_test_gamma_green.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.btn_test_gamma_red.setText(QCoreApplication.translate("TabSettings", u"Test", None))
        self.label_3.setText(QCoreApplication.translate("TabSettings", u"Green", None))
        self.label_4.setText(QCoreApplication.translate("TabSettings", u"Blue", None))
        self.label_2.setText(QCoreApplication.translate("TabSettings", u"Red", None))
    # retranslateUi

