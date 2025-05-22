# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_TabMusic(object):
    def setupUi(self, TabMusic):
        if not TabMusic.objectName():
            TabMusic.setObjectName(u"TabMusic")
        TabMusic.resize(663, 558)
        self.gridLayout = QGridLayout(TabMusic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_preview = QPushButton(TabMusic)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout.addWidget(self.btn_preview)

        self.btn_display = QPushButton(TabMusic)
        self.btn_display.setObjectName(u"btn_display")

        self.horizontalLayout.addWidget(self.btn_display)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.lbl_status = QLabel(TabMusic)
        self.lbl_status.setObjectName(u"lbl_status")

        self.gridLayout.addWidget(self.lbl_status, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(TabMusic)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 622, 722))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.btn_mode_timeline_dual = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_timeline_dual.setObjectName(u"btn_mode_timeline_dual")
        self.btn_mode_timeline_dual.setMinimumSize(QSize(150, 200))
        self.btn_mode_timeline_dual.setIconSize(QSize(128, 128))
        self.btn_mode_timeline_dual.setCheckable(True)
        self.btn_mode_timeline_dual.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.btn_mode_timeline_dual, 0, 1, 1, 1)

        self.btn_mode_timeline = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_timeline.setObjectName(u"btn_mode_timeline")
        self.btn_mode_timeline.setMinimumSize(QSize(150, 200))
        self.btn_mode_timeline.setIconSize(QSize(128, 128))
        self.btn_mode_timeline.setCheckable(True)
        self.btn_mode_timeline.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.btn_mode_timeline, 0, 0, 1, 1)

        self.btn_mode_bands = QToolButton(self.scrollAreaWidgetContents)
        self.btn_mode_bands.setObjectName(u"btn_mode_bands")
        self.btn_mode_bands.setMinimumSize(QSize(150, 200))
        self.btn_mode_bands.setIconSize(QSize(128, 128))
        self.btn_mode_bands.setCheckable(True)
        self.btn_mode_bands.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.btn_mode_bands, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.mode_settings = QStackedWidget(self.scrollAreaWidgetContents)
        self.mode_settings.setObjectName(u"mode_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_settings.sizePolicy().hasHeightForWidth())
        self.mode_settings.setSizePolicy(sizePolicy)
        self.page_timeline = QWidget()
        self.page_timeline.setObjectName(u"page_timeline")
        self.gridLayout_5 = QGridLayout(self.page_timeline)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_6 = QLabel(self.page_timeline)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 1, 0, 1, 3)

        self.sld_timeline_sensitivity = QSlider(self.page_timeline)
        self.sld_timeline_sensitivity.setObjectName(u"sld_timeline_sensitivity")
        self.sld_timeline_sensitivity.setMinimum(1)
        self.sld_timeline_sensitivity.setMaximum(200)
        self.sld_timeline_sensitivity.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_10.addWidget(self.sld_timeline_sensitivity, 0, 2, 1, 1)

        self.lbl_timeline_sensitivity = QLabel(self.page_timeline)
        self.lbl_timeline_sensitivity.setObjectName(u"lbl_timeline_sensitivity")

        self.gridLayout_10.addWidget(self.lbl_timeline_sensitivity, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.mode_settings.addWidget(self.page_timeline)
        self.page_dual = QWidget()
        self.page_dual.setObjectName(u"page_dual")
        self.gridLayout_9 = QGridLayout(self.page_dual)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_5 = QLabel(self.page_dual)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.sld_timelinedual_sensitivity = QSlider(self.page_dual)
        self.sld_timelinedual_sensitivity.setObjectName(u"sld_timelinedual_sensitivity")
        self.sld_timelinedual_sensitivity.setMinimum(1)
        self.sld_timelinedual_sensitivity.setMaximum(200)
        self.sld_timelinedual_sensitivity.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_8.addWidget(self.sld_timelinedual_sensitivity, 0, 2, 1, 1)

        self.lbl_timelinedual_sensitivity = QLabel(self.page_dual)
        self.lbl_timelinedual_sensitivity.setObjectName(u"lbl_timelinedual_sensitivity")

        self.gridLayout_8.addWidget(self.lbl_timelinedual_sensitivity, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.mode_settings.addWidget(self.page_dual)
        self.page_bands = QWidget()
        self.page_bands.setObjectName(u"page_bands")
        sizePolicy.setHeightForWidth(self.page_bands.sizePolicy().hasHeightForWidth())
        self.page_bands.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.page_bands)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.page_bands)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(0, 70))

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.sld_bands_spacing = QSlider(self.page_bands)
        self.sld_bands_spacing.setObjectName(u"sld_bands_spacing")
        self.sld_bands_spacing.setMinimum(0)
        self.sld_bands_spacing.setMaximum(10)
        self.sld_bands_spacing.setValue(1)
        self.sld_bands_spacing.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.sld_bands_spacing, 1, 3, 1, 1)

        self.label_8 = QLabel(self.page_bands)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 70))

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_3 = QLabel(self.page_bands)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 70))

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.sld_bands_f_max = QSlider(self.page_bands)
        self.sld_bands_f_max.setObjectName(u"sld_bands_f_max")
        self.sld_bands_f_max.setMinimum(2000)
        self.sld_bands_f_max.setMaximum(24000)
        self.sld_bands_f_max.setSingleStep(2000)
        self.sld_bands_f_max.setValue(20000)
        self.sld_bands_f_max.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.sld_bands_f_max, 4, 3, 1, 1)

        self.sld_bands_bin_width = QSlider(self.page_bands)
        self.sld_bands_bin_width.setObjectName(u"sld_bands_bin_width")
        self.sld_bands_bin_width.setMinimum(1)
        self.sld_bands_bin_width.setMaximum(50)
        self.sld_bands_bin_width.setValue(2)
        self.sld_bands_bin_width.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.sld_bands_bin_width, 0, 3, 1, 1)

        self.label_2 = QLabel(self.page_bands)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 70))

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.lbl_bands_f_min = QLabel(self.page_bands)
        self.lbl_bands_f_min.setObjectName(u"lbl_bands_f_min")
        self.lbl_bands_f_min.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_bands_f_min, 5, 1, 1, 1)

        self.lbl_bands_spacing = QLabel(self.page_bands)
        self.lbl_bands_spacing.setObjectName(u"lbl_bands_spacing")
        self.lbl_bands_spacing.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_bands_spacing, 1, 1, 1, 1)

        self.lbl_bands_a_max = QLabel(self.page_bands)
        self.lbl_bands_a_max.setObjectName(u"lbl_bands_a_max")
        self.lbl_bands_a_max.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_bands_a_max, 2, 1, 1, 1)

        self.label = QLabel(self.page_bands)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 70))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.sld_bands_a_max = QSlider(self.page_bands)
        self.sld_bands_a_max.setObjectName(u"sld_bands_a_max")
        self.sld_bands_a_max.setMinimum(-100)
        self.sld_bands_a_max.setMaximum(100)
        self.sld_bands_a_max.setSingleStep(10)
        self.sld_bands_a_max.setValue(50)
        self.sld_bands_a_max.setOrientation(Qt.Orientation.Horizontal)
        self.sld_bands_a_max.setTickPosition(QSlider.TickPosition.NoTicks)

        self.gridLayout_2.addWidget(self.sld_bands_a_max, 2, 3, 1, 1)

        self.sld_bands_a_min = QSlider(self.page_bands)
        self.sld_bands_a_min.setObjectName(u"sld_bands_a_min")
        self.sld_bands_a_min.setMinimum(-100)
        self.sld_bands_a_min.setMaximum(100)
        self.sld_bands_a_min.setSingleStep(10)
        self.sld_bands_a_min.setValue(-20)
        self.sld_bands_a_min.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.sld_bands_a_min, 3, 3, 1, 1)

        self.lbl_bands_f_max = QLabel(self.page_bands)
        self.lbl_bands_f_max.setObjectName(u"lbl_bands_f_max")
        self.lbl_bands_f_max.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_bands_f_max, 4, 1, 1, 1)

        self.lbl_bands_a_min = QLabel(self.page_bands)
        self.lbl_bands_a_min.setObjectName(u"lbl_bands_a_min")
        self.lbl_bands_a_min.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_bands_a_min, 3, 1, 1, 1)

        self.label_4 = QLabel(self.page_bands)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 70))

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.sld_bands_f_min = QSlider(self.page_bands)
        self.sld_bands_f_min.setObjectName(u"sld_bands_f_min")
        self.sld_bands_f_min.setMinimum(0)
        self.sld_bands_f_min.setMaximum(200)
        self.sld_bands_f_min.setSingleStep(10)
        self.sld_bands_f_min.setValue(50)
        self.sld_bands_f_min.setTracking(True)
        self.sld_bands_f_min.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.sld_bands_f_min, 5, 3, 1, 1)

        self.lbl_bands_bin_width = QLabel(self.page_bands)
        self.lbl_bands_bin_width.setObjectName(u"lbl_bands_bin_width")
        self.lbl_bands_bin_width.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_bands_bin_width, 0, 1, 1, 1)

        self.label_9 = QLabel(self.page_bands)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_10 = QLabel(self.page_bands)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_11 = QLabel(self.page_bands)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 4, 2, 1, 1)

        self.label_12 = QLabel(self.page_bands)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 5, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.line = QFrame(self.page_bands)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 1)

        self.mode_settings.addWidget(self.page_bands)

        self.verticalLayout_2.addWidget(self.mode_settings)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.retranslateUi(TabMusic)

        self.mode_settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabMusic)
    # setupUi

    def retranslateUi(self, TabMusic):
        TabMusic.setWindowTitle(QCoreApplication.translate("TabMusic", u"Form", None))
        self.btn_preview.setText(QCoreApplication.translate("TabMusic", u"Preview", None))
        self.btn_display.setText(QCoreApplication.translate("TabMusic", u"Display", None))
        self.lbl_status.setText("")
        self.btn_mode_timeline_dual.setText(QCoreApplication.translate("TabMusic", u"Timeline Dual", None))
        self.btn_mode_timeline.setText(QCoreApplication.translate("TabMusic", u"Timeline", None))
        self.btn_mode_bands.setText(QCoreApplication.translate("TabMusic", u"Frequency Bands", None))
        self.label_6.setText(QCoreApplication.translate("TabMusic", u"Sensitivity", None))
        self.lbl_timeline_sensitivity.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("TabMusic", u"Sensitivity", None))
        self.lbl_timelinedual_sensitivity.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("TabMusic", u"Max Frequenz", None))
        self.label_8.setText(QCoreApplication.translate("TabMusic", u"Min Frequenz", None))
        self.label_3.setText(QCoreApplication.translate("TabMusic", u"Min Amplitude", None))
        self.label_2.setText(QCoreApplication.translate("TabMusic", u"Max Amplitude", None))
        self.lbl_bands_f_min.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.lbl_bands_spacing.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.lbl_bands_a_max.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("TabMusic", u"Bin Width", None))
        self.lbl_bands_f_max.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.lbl_bands_a_min.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("TabMusic", u"Spacing", None))
        self.lbl_bands_bin_width.setText(QCoreApplication.translate("TabMusic", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("TabMusic", u"dB", None))
        self.label_10.setText(QCoreApplication.translate("TabMusic", u"dB", None))
        self.label_11.setText(QCoreApplication.translate("TabMusic", u"Hz", None))
        self.label_12.setText(QCoreApplication.translate("TabMusic", u"Hz", None))
    # retranslateUi

