# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_TabAnimation(object):
    def setupUi(self, TabAnimation):
        if not TabAnimation.objectName():
            TabAnimation.setObjectName(u"TabAnimation")
        TabAnimation.resize(400, 300)
        self.gridLayout = QGridLayout(TabAnimation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.cb_animation_type = QComboBox(TabAnimation)
        self.cb_animation_type.setObjectName(u"cb_animation_type")

        self.gridLayout.addWidget(self.cb_animation_type, 0, 1, 1, 1)

        self.label = QLabel(TabAnimation)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(TabAnimation)

        QMetaObject.connectSlotsByName(TabAnimation)
    # setupUi

    def retranslateUi(self, TabAnimation):
        TabAnimation.setWindowTitle(QCoreApplication.translate("TabAnimation", u"Form", None))
        self.label.setText(QCoreApplication.translate("TabAnimation", u"Animation", None))
    # retranslateUi

