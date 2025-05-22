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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_TabAnimation(object):
    def setupUi(self, TabAnimation):
        if not TabAnimation.objectName():
            TabAnimation.setObjectName(u"TabAnimation")
        TabAnimation.resize(843, 604)
        self.gridLayout = QGridLayout(TabAnimation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_preview = QPushButton(TabAnimation)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout.addWidget(self.btn_preview)

        self.btn_display = QPushButton(TabAnimation)
        self.btn_display.setObjectName(u"btn_display")

        self.horizontalLayout.addWidget(self.btn_display)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(TabAnimation)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -231, 802, 764))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_mode_sine = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_sine.setObjectName(u"btn_mode_sine")
        self.btn_mode_sine.setMinimumSize(QSize(150, 200))
        self.btn_mode_sine.setIconSize(QSize(128, 128))
        self.btn_mode_sine.setCheckable(True)
        self.btn_mode_sine.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_sine, 0, 0, 1, 1)

        self.btn_mode_rect = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_rect.setObjectName(u"btn_mode_rect")
        self.btn_mode_rect.setMinimumSize(QSize(150, 200))
        self.btn_mode_rect.setIconSize(QSize(128, 128))
        self.btn_mode_rect.setCheckable(True)
        self.btn_mode_rect.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_rect, 0, 1, 1, 1)

        self.btn_mode_sawtooth = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_sawtooth.setObjectName(u"btn_mode_sawtooth")
        self.btn_mode_sawtooth.setMinimumSize(QSize(150, 200))
        self.btn_mode_sawtooth.setIconSize(QSize(128, 128))
        self.btn_mode_sawtooth.setCheckable(True)
        self.btn_mode_sawtooth.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_sawtooth, 0, 2, 1, 1)

        self.btn_mode_rainbow = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_rainbow.setObjectName(u"btn_mode_rainbow")
        self.btn_mode_rainbow.setMinimumSize(QSize(150, 200))
        self.btn_mode_rainbow.setIconSize(QSize(128, 128))
        self.btn_mode_rainbow.setCheckable(True)
        self.btn_mode_rainbow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.btn_mode_rainbow, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.mode_settings = QStackedWidget(self.scrollAreaWidgetContents)
        self.mode_settings.setObjectName(u"mode_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_settings.sizePolicy().hasHeightForWidth())
        self.mode_settings.setSizePolicy(sizePolicy)
        self.page_sine = QWidget()
        self.page_sine.setObjectName(u"page_sine")
        self.gridLayout_4 = QGridLayout(self.page_sine)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.page_sine)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 70))

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.sld_sine_phase = QSlider(self.page_sine)
        self.sld_sine_phase.setObjectName(u"sld_sine_phase")
        self.sld_sine_phase.setMinimum(0)
        self.sld_sine_phase.setMaximum(350)
        self.sld_sine_phase.setSingleStep(10)
        self.sld_sine_phase.setPageStep(1)
        self.sld_sine_phase.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sld_sine_phase, 4, 3, 1, 1)

        self.label = QLabel(self.page_sine)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 70))

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lbl_sine_offset = QLabel(self.page_sine)
        self.lbl_sine_offset.setObjectName(u"lbl_sine_offset")
        self.lbl_sine_offset.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_sine_offset, 3, 1, 1, 1)

        self.label_8 = QLabel(self.page_sine)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 4, 2, 1, 1)

        self.lbl_sine_phase = QLabel(self.page_sine)
        self.lbl_sine_phase.setObjectName(u"lbl_sine_phase")
        self.lbl_sine_phase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_sine_phase, 4, 1, 1, 1)

        self.sld_sine_offset = QSlider(self.page_sine)
        self.sld_sine_offset.setObjectName(u"sld_sine_offset")
        self.sld_sine_offset.setMinimum(-19)
        self.sld_sine_offset.setMaximum(19)
        self.sld_sine_offset.setPageStep(1)
        self.sld_sine_offset.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sld_sine_offset, 3, 3, 1, 1)

        self.label_10 = QLabel(self.page_sine)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(0, 70))

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_32 = QLabel(self.page_sine)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)
        self.label_32.setMinimumSize(QSize(0, 70))

        self.gridLayout_3.addWidget(self.label_32, 4, 0, 1, 1)

        self.lbl_sine_a = QLabel(self.page_sine)
        self.lbl_sine_a.setObjectName(u"lbl_sine_a")
        self.lbl_sine_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_sine_a, 2, 1, 1, 1)

        self.sld_sine_a = QSlider(self.page_sine)
        self.sld_sine_a.setObjectName(u"sld_sine_a")
        self.sld_sine_a.setMinimum(1)
        self.sld_sine_a.setMaximum(10)
        self.sld_sine_a.setPageStep(1)
        self.sld_sine_a.setValue(8)
        self.sld_sine_a.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sld_sine_a, 2, 3, 1, 1)

        self.sld_sine_f = QSlider(self.page_sine)
        self.sld_sine_f.setObjectName(u"sld_sine_f")
        self.sld_sine_f.setMinimum(0)
        self.sld_sine_f.setMaximum(50)
        self.sld_sine_f.setPageStep(1)
        self.sld_sine_f.setValue(10)
        self.sld_sine_f.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sld_sine_f, 0, 3, 1, 1)

        self.label_7 = QLabel(self.page_sine)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.lbl_sine_waves = QLabel(self.page_sine)
        self.lbl_sine_waves.setObjectName(u"lbl_sine_waves")
        self.lbl_sine_waves.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_sine_waves, 1, 1, 1, 1)

        self.sld_sine_waves = QSlider(self.page_sine)
        self.sld_sine_waves.setObjectName(u"sld_sine_waves")
        self.sld_sine_waves.setMinimum(1)
        self.sld_sine_waves.setMaximum(10)
        self.sld_sine_waves.setPageStep(1)
        self.sld_sine_waves.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sld_sine_waves, 1, 3, 1, 1)

        self.lbl_sine_f = QLabel(self.page_sine)
        self.lbl_sine_f.setObjectName(u"lbl_sine_f")
        self.lbl_sine_f.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_sine_f, 0, 1, 1, 1)

        self.label_5 = QLabel(self.page_sine)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 70))

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.mode_settings.addWidget(self.page_sine)
        self.page_rect = QWidget()
        self.page_rect.setObjectName(u"page_rect")
        self.gridLayout_6 = QGridLayout(self.page_rect)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_11 = QLabel(self.page_rect)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 2, 1, 1)

        self.sld_rect_waves = QSlider(self.page_rect)
        self.sld_rect_waves.setObjectName(u"sld_rect_waves")
        self.sld_rect_waves.setMinimum(1)
        self.sld_rect_waves.setMaximum(10)
        self.sld_rect_waves.setPageStep(1)
        self.sld_rect_waves.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.sld_rect_waves, 1, 3, 1, 1)

        self.lbl_rect_waves = QLabel(self.page_rect)
        self.lbl_rect_waves.setObjectName(u"lbl_rect_waves")
        self.lbl_rect_waves.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_rect_waves, 1, 1, 1, 1)

        self.label_25 = QLabel(self.page_rect)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_25, 5, 0, 1, 1)

        self.label_6 = QLabel(self.page_rect)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.lbl_rect_phase = QLabel(self.page_rect)
        self.lbl_rect_phase.setObjectName(u"lbl_rect_phase")
        self.lbl_rect_phase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_rect_phase, 4, 1, 1, 1)

        self.lbl_rect_offset = QLabel(self.page_rect)
        self.lbl_rect_offset.setObjectName(u"lbl_rect_offset")
        self.lbl_rect_offset.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_rect_offset, 3, 1, 1, 1)

        self.label_15 = QLabel(self.page_rect)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 4, 2, 1, 1)

        self.sld_rect_phase = QSlider(self.page_rect)
        self.sld_rect_phase.setObjectName(u"sld_rect_phase")
        self.sld_rect_phase.setMinimum(0)
        self.sld_rect_phase.setMaximum(359)
        self.sld_rect_phase.setSingleStep(10)
        self.sld_rect_phase.setPageStep(1)
        self.sld_rect_phase.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.sld_rect_phase, 4, 3, 1, 1)

        self.lbl_rect_duty = QLabel(self.page_rect)
        self.lbl_rect_duty.setObjectName(u"lbl_rect_duty")
        self.lbl_rect_duty.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_rect_duty, 5, 1, 1, 1)

        self.label_26 = QLabel(self.page_rect)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 5, 2, 1, 1)

        self.sld_rect_offset = QSlider(self.page_rect)
        self.sld_rect_offset.setObjectName(u"sld_rect_offset")
        self.sld_rect_offset.setMinimum(-19)
        self.sld_rect_offset.setMaximum(19)
        self.sld_rect_offset.setPageStep(1)
        self.sld_rect_offset.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.sld_rect_offset, 3, 3, 1, 1)

        self.sld_rect_a = QSlider(self.page_rect)
        self.sld_rect_a.setObjectName(u"sld_rect_a")
        self.sld_rect_a.setMinimum(1)
        self.sld_rect_a.setMaximum(10)
        self.sld_rect_a.setPageStep(1)
        self.sld_rect_a.setValue(8)
        self.sld_rect_a.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.sld_rect_a, 2, 3, 1, 1)

        self.lbl_rect_a = QLabel(self.page_rect)
        self.lbl_rect_a.setObjectName(u"lbl_rect_a")
        self.lbl_rect_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_rect_a, 2, 1, 1, 1)

        self.sld_rect_f = QSlider(self.page_rect)
        self.sld_rect_f.setObjectName(u"sld_rect_f")
        self.sld_rect_f.setMinimum(0)
        self.sld_rect_f.setMaximum(50)
        self.sld_rect_f.setPageStep(1)
        self.sld_rect_f.setValue(10)
        self.sld_rect_f.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.sld_rect_f, 0, 3, 1, 1)

        self.label_2 = QLabel(self.page_rect)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.sld_rect_duty = QSlider(self.page_rect)
        self.sld_rect_duty.setObjectName(u"sld_rect_duty")
        self.sld_rect_duty.setMinimum(0)
        self.sld_rect_duty.setMaximum(100)
        self.sld_rect_duty.setSingleStep(5)
        self.sld_rect_duty.setPageStep(1)
        self.sld_rect_duty.setValue(50)
        self.sld_rect_duty.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.sld_rect_duty, 5, 3, 1, 1)

        self.lbl_rect_f = QLabel(self.page_rect)
        self.lbl_rect_f.setObjectName(u"lbl_rect_f")
        self.lbl_rect_f.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_rect_f, 0, 1, 1, 1)

        self.label_31 = QLabel(self.page_rect)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)
        self.label_31.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_31, 4, 0, 1, 1)

        self.label_4 = QLabel(self.page_rect)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_14 = QLabel(self.page_rect)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 6, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.mode_settings.addWidget(self.page_rect)
        self.page_saw = QWidget()
        self.page_saw.setObjectName(u"page_saw")
        self.gridLayout_8 = QGridLayout(self.page_saw)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lbl_saw_a = QLabel(self.page_saw)
        self.lbl_saw_a.setObjectName(u"lbl_saw_a")
        self.lbl_saw_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_saw_a, 2, 1, 1, 1)

        self.label_18 = QLabel(self.page_saw)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_27 = QLabel(self.page_saw)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.label_27, 5, 0, 1, 1)

        self.sld_saw_f = QSlider(self.page_saw)
        self.sld_saw_f.setObjectName(u"sld_saw_f")
        self.sld_saw_f.setMinimum(0)
        self.sld_saw_f.setMaximum(50)
        self.sld_saw_f.setPageStep(1)
        self.sld_saw_f.setValue(10)
        self.sld_saw_f.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.sld_saw_f, 0, 3, 1, 1)

        self.lbl_saw_phase = QLabel(self.page_saw)
        self.lbl_saw_phase.setObjectName(u"lbl_saw_phase")
        self.lbl_saw_phase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_saw_phase, 4, 1, 1, 1)

        self.lbl_saw_waves = QLabel(self.page_saw)
        self.lbl_saw_waves.setObjectName(u"lbl_saw_waves")
        self.lbl_saw_waves.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_saw_waves, 1, 1, 1, 1)

        self.label_28 = QLabel(self.page_saw)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 5, 2, 1, 1)

        self.label_29 = QLabel(self.page_saw)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_19 = QLabel(self.page_saw)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 0, 2, 1, 1)

        self.lbl_saw_symmetry = QLabel(self.page_saw)
        self.lbl_saw_symmetry.setObjectName(u"lbl_saw_symmetry")
        self.lbl_saw_symmetry.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_saw_symmetry, 5, 1, 1, 1)

        self.sld_saw_a = QSlider(self.page_saw)
        self.sld_saw_a.setObjectName(u"sld_saw_a")
        self.sld_saw_a.setMinimum(1)
        self.sld_saw_a.setMaximum(10)
        self.sld_saw_a.setPageStep(1)
        self.sld_saw_a.setValue(8)
        self.sld_saw_a.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.sld_saw_a, 2, 3, 1, 1)

        self.lbl_saw_f = QLabel(self.page_saw)
        self.lbl_saw_f.setObjectName(u"lbl_saw_f")
        self.lbl_saw_f.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_saw_f, 0, 1, 1, 1)

        self.label_22 = QLabel(self.page_saw)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.label_22, 3, 0, 1, 1)

        self.label_21 = QLabel(self.page_saw)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)

        self.lbl_saw_offset = QLabel(self.page_saw)
        self.lbl_saw_offset.setObjectName(u"lbl_saw_offset")
        self.lbl_saw_offset.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_saw_offset, 3, 1, 1, 1)

        self.label_30 = QLabel(self.page_saw)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 4, 2, 1, 1)

        self.sld_saw_symmetry = QSlider(self.page_saw)
        self.sld_saw_symmetry.setObjectName(u"sld_saw_symmetry")
        self.sld_saw_symmetry.setMinimum(0)
        self.sld_saw_symmetry.setMaximum(100)
        self.sld_saw_symmetry.setSingleStep(5)
        self.sld_saw_symmetry.setPageStep(1)
        self.sld_saw_symmetry.setValue(50)
        self.sld_saw_symmetry.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.sld_saw_symmetry, 5, 3, 1, 1)

        self.sld_saw_waves = QSlider(self.page_saw)
        self.sld_saw_waves.setObjectName(u"sld_saw_waves")
        self.sld_saw_waves.setMinimum(1)
        self.sld_saw_waves.setMaximum(10)
        self.sld_saw_waves.setPageStep(1)
        self.sld_saw_waves.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.sld_saw_waves, 1, 3, 1, 1)

        self.label_17 = QLabel(self.page_saw)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)

        self.sld_saw_phase = QSlider(self.page_saw)
        self.sld_saw_phase.setObjectName(u"sld_saw_phase")
        self.sld_saw_phase.setMinimum(0)
        self.sld_saw_phase.setMaximum(359)
        self.sld_saw_phase.setSingleStep(10)
        self.sld_saw_phase.setPageStep(1)
        self.sld_saw_phase.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.sld_saw_phase, 4, 3, 1, 1)

        self.sld_saw_offset = QSlider(self.page_saw)
        self.sld_saw_offset.setObjectName(u"sld_saw_offset")
        self.sld_saw_offset.setMinimum(-19)
        self.sld_saw_offset.setMaximum(19)
        self.sld_saw_offset.setPageStep(1)
        self.sld_saw_offset.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.sld_saw_offset, 3, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 6, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.mode_settings.addWidget(self.page_saw)
        self.page_rainbow = QWidget()
        self.page_rainbow.setObjectName(u"page_rainbow")
        self.mode_settings.addWidget(self.page_rainbow)

        self.verticalLayout.addWidget(self.mode_settings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(TabAnimation)

        self.mode_settings.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TabAnimation)
    # setupUi

    def retranslateUi(self, TabAnimation):
        TabAnimation.setWindowTitle(QCoreApplication.translate("TabAnimation", u"Form", None))
        self.btn_preview.setText(QCoreApplication.translate("TabAnimation", u"Preview", None))
        self.btn_display.setText(QCoreApplication.translate("TabAnimation", u"Display", None))
        self.btn_mode_sine.setText(QCoreApplication.translate("TabAnimation", u"Sine", None))
        self.btn_mode_rect.setText(QCoreApplication.translate("TabAnimation", u"Rectangle", None))
        self.btn_mode_sawtooth.setText(QCoreApplication.translate("TabAnimation", u"Sawtooth", None))
        self.btn_mode_rainbow.setText(QCoreApplication.translate("TabAnimation", u"Rainbow", None))
        self.label_3.setText(QCoreApplication.translate("TabAnimation", u"Waves", None))
        self.label.setText(QCoreApplication.translate("TabAnimation", u"Frequenz", None))
        self.lbl_sine_offset.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("TabAnimation", u"\u00b0", None))
        self.lbl_sine_phase.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("TabAnimation", u"Offset", None))
        self.label_32.setText(QCoreApplication.translate("TabAnimation", u"Phase", None))
        self.lbl_sine_a.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("TabAnimation", u"Hz", None))
        self.lbl_sine_waves.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.lbl_sine_f.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("TabAnimation", u"Amplitude", None))
        self.label_11.setText(QCoreApplication.translate("TabAnimation", u"Hz", None))
        self.lbl_rect_waves.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("TabAnimation", u"Duty", None))
        self.label_6.setText(QCoreApplication.translate("TabAnimation", u"Amplitude", None))
        self.lbl_rect_phase.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.lbl_rect_offset.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("TabAnimation", u"\u00b0", None))
        self.lbl_rect_duty.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("TabAnimation", u"%", None))
        self.lbl_rect_a.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("TabAnimation", u"Frequenz", None))
        self.lbl_rect_f.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("TabAnimation", u"Phase", None))
        self.label_4.setText(QCoreApplication.translate("TabAnimation", u"Waves", None))
        self.label_14.setText(QCoreApplication.translate("TabAnimation", u"Offset", None))
        self.lbl_saw_a.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("TabAnimation", u"Frequenz", None))
        self.label_27.setText(QCoreApplication.translate("TabAnimation", u"Symmetry", None))
        self.lbl_saw_phase.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.lbl_saw_waves.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("TabAnimation", u"%", None))
        self.label_29.setText(QCoreApplication.translate("TabAnimation", u"Phase", None))
        self.label_19.setText(QCoreApplication.translate("TabAnimation", u"Hz", None))
        self.lbl_saw_symmetry.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.lbl_saw_f.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("TabAnimation", u"Offset", None))
        self.label_21.setText(QCoreApplication.translate("TabAnimation", u"Amplitude", None))
        self.lbl_saw_offset.setText(QCoreApplication.translate("TabAnimation", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("TabAnimation", u"\u00b0", None))
        self.label_17.setText(QCoreApplication.translate("TabAnimation", u"Waves", None))
    # retranslateUi

