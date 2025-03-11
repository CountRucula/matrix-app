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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_TabSettings(object):
    def setupUi(self, TabSettings):
        if not TabSettings.objectName():
            TabSettings.setObjectName(u"TabSettings")
        TabSettings.resize(545, 485)
        self.verticalLayout = QVBoxLayout(TabSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_matrix_conn = QLabel(TabSettings)
        self.lbl_matrix_conn.setObjectName(u"lbl_matrix_conn")
        self.lbl_matrix_conn.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        font.setBold(True)
        self.lbl_matrix_conn.setFont(font)
        self.lbl_matrix_conn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_matrix_conn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_matrix_port = QLabel(TabSettings)
        self.lbl_matrix_port.setObjectName(u"lbl_matrix_port")
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_matrix_port.setFont(font1)
        self.lbl_matrix_port.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_matrix_port)

        self.cb_matrix_ports = QComboBox(TabSettings)
        self.cb_matrix_ports.setObjectName(u"cb_matrix_ports")
        self.cb_matrix_ports.setFont(font1)

        self.horizontalLayout.addWidget(self.cb_matrix_ports)

        self.btn_refresh_ports = QToolButton(TabSettings)
        self.btn_refresh_ports.setObjectName(u"btn_refresh_ports")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.btn_refresh_ports.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_refresh_ports)

        self.lbl_matrix_baud = QLabel(TabSettings)
        self.lbl_matrix_baud.setObjectName(u"lbl_matrix_baud")
        self.lbl_matrix_baud.setFont(font1)
        self.lbl_matrix_baud.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_matrix_baud)

        self.cb_matrix_baudrates = QComboBox(TabSettings)
        self.cb_matrix_baudrates.setObjectName(u"cb_matrix_baudrates")
        self.cb_matrix_baudrates.setFont(font1)
        self.cb_matrix_baudrates.setFrame(False)

        self.horizontalLayout.addWidget(self.cb_matrix_baudrates)

        self.btn_matrix_connect = QPushButton(TabSettings)
        self.btn_matrix_connect.setObjectName(u"btn_matrix_connect")
        self.btn_matrix_connect.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_matrix_connect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(TabSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.lbl_frackstock_conn = QLabel(TabSettings)
        self.lbl_frackstock_conn.setObjectName(u"lbl_frackstock_conn")
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.lbl_frackstock_conn.setFont(font2)
        self.lbl_frackstock_conn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_frackstock_conn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TabSettings)

        QMetaObject.connectSlotsByName(TabSettings)
    # setupUi

    def retranslateUi(self, TabSettings):
        TabSettings.setWindowTitle(QCoreApplication.translate("TabSettings", u"Form", None))
        self.lbl_matrix_conn.setText(QCoreApplication.translate("TabSettings", u"Matrix Connection", None))
        self.lbl_matrix_port.setText(QCoreApplication.translate("TabSettings", u"Port:", None))
        self.btn_refresh_ports.setText("")
        self.lbl_matrix_baud.setText(QCoreApplication.translate("TabSettings", u"Baud:", None))
        self.btn_matrix_connect.setText(QCoreApplication.translate("TabSettings", u"Connect", None))
        self.lbl_frackstock_conn.setText(QCoreApplication.translate("TabSettings", u"Frackstock Connection", None))
    # retranslateUi

