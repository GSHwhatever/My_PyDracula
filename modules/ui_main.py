# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindIkvnh.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 729)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/my_tm.ico);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Normal)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_login = QPushButton(self.topMenu)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_login.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-screen-desktop.png);")

        self.verticalLayout_8.addWidget(self.btn_login)

        self.btn_search = QPushButton(self.topMenu)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QSize(0, 45))
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_search.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_search)

        self.btn_batch = QPushButton(self.topMenu)
        self.btn_batch.setObjectName(u"btn_batch")
        sizePolicy.setHeightForWidth(self.btn_batch.sizePolicy().hasHeightForWidth())
        self.btn_batch.setSizePolicy(sizePolicy)
        self.btn_batch.setMinimumSize(QSize(0, 45))
        self.btn_batch.setFont(font)
        self.btn_batch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_batch.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_batch.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-vertical-align-bottom.png)")

        self.verticalLayout_8.addWidget(self.btn_batch)

        self.btn_set = QPushButton(self.topMenu)
        self.btn_set.setObjectName(u"btn_set")
        sizePolicy.setHeightForWidth(self.btn_set.sizePolicy().hasHeightForWidth())
        self.btn_set.setSizePolicy(sizePolicy)
        self.btn_set.setMinimumSize(QSize(0, 45))
        self.btn_set.setFont(font)
        self.btn_set.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_set.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_set.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_8.addWidget(self.btn_set)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/my2.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.widget = QWidget(self.login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1181, 611))
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(150, 210, 911, 321))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.horizontalLayoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_6)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 411, 281))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 10, 381, 61))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_idcard_login = QLabel(self.horizontalLayoutWidget_2)
        self.lb_idcard_login.setObjectName(u"lb_idcard_login")

        self.horizontalLayout_9.addWidget(self.lb_idcard_login)

        self.le_idcard_login = QLineEdit(self.horizontalLayoutWidget_2)
        self.le_idcard_login.setObjectName(u"le_idcard_login")
        self.le_idcard_login.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_9.addWidget(self.le_idcard_login)


        self.verticalLayout_17.addWidget(self.frame)

        self.frame_4 = QFrame(self.verticalLayoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_3 = QWidget(self.frame_4)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 381, 61))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.lb_name_login = QLabel(self.horizontalLayoutWidget_3)
        self.lb_name_login.setObjectName(u"lb_name_login")

        self.horizontalLayout_11.addWidget(self.lb_name_login)

        self.le_name_login = QLineEdit(self.horizontalLayoutWidget_3)
        self.le_name_login.setObjectName(u"le_name_login")
        self.le_name_login.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.le_name_login)


        self.verticalLayout_17.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.verticalLayoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_6 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 10, 381, 61))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pb_login_login = QPushButton(self.horizontalLayoutWidget_6)
        self.pb_login_login.setObjectName(u"pb_login_login")
        self.pb_login_login.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_12.addWidget(self.pb_login_login)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.pb_rc_login = QPushButton(self.horizontalLayoutWidget_6)
        self.pb_rc_login.setObjectName(u"pb_rc_login")
        self.pb_rc_login.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_12.addWidget(self.pb_rc_login)


        self.verticalLayout_17.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(450, 0, 451, 319))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_10)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 391, 281))
        self.verticalLayout_23 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.verticalLayoutWidget_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_4 = QWidget(self.frame_8)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 10, 369, 61))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lb_user_login = QLabel(self.horizontalLayoutWidget_4)
        self.lb_user_login.setObjectName(u"lb_user_login")

        self.horizontalLayout_14.addWidget(self.lb_user_login)

        self.le_user_login = QLineEdit(self.horizontalLayoutWidget_4)
        self.le_user_login.setObjectName(u"le_user_login")
        self.le_user_login.setEnabled(True)
        self.le_user_login.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_user_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_user_login.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.le_user_login)


        self.verticalLayout_23.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.verticalLayoutWidget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_9 = QWidget(self.frame_7)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 10, 369, 61))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lb_origin_login = QLabel(self.horizontalLayoutWidget_9)
        self.lb_origin_login.setObjectName(u"lb_origin_login")

        self.horizontalLayout_19.addWidget(self.lb_origin_login)

        self.le_origin_login = QLineEdit(self.horizontalLayoutWidget_9)
        self.le_origin_login.setObjectName(u"le_origin_login")
        self.le_origin_login.setEnabled(True)
        self.le_origin_login.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_origin_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_origin_login.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.le_origin_login)


        self.verticalLayout_23.addWidget(self.frame_7)

        self.frame_3 = QFrame(self.verticalLayoutWidget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_11 = QWidget(self.frame_3)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(10, 10, 371, 58))
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(125, 56, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_6)

        self.pb_vpn_login = QPushButton(self.horizontalLayoutWidget_11)
        self.pb_vpn_login.setObjectName(u"pb_vpn_login")

        self.horizontalLayout_21.addWidget(self.pb_vpn_login)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_5)


        self.verticalLayout_23.addWidget(self.frame_3)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(150, 70, 281, 80))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 251, 71))
        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(600, 70, 281, 80))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 251, 71))
        self.stackedWidget.addWidget(self.login)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.search.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.search)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_3 = QFrame(self.search)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.row_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 20, 421, 51))
        self.label_6 = QLabel(self.row_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 100, 91, 31))
        self.lineEdit = QLineEdit(self.row_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 100, 351, 31))
        self.pushButton = QPushButton(self.row_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(740, 100, 81, 31))
        self.ryjb_info = QTabWidget(self.row_3)
        self.ryjb_info.setObjectName(u"ryjb_info")
        self.ryjb_info.setGeometry(QRect(0, 130, 1161, 451))
        self.ryjb_info.setStyleSheet(u"")
        self.ryjb_info.setTabPosition(QTabWidget.TabPosition.North)
        self.ryjb_info.setTabShape(QTabWidget.TabShape.Triangular)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tableWidget = QTableWidget(self.tab_7)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1151, 421))
        self.tableWidget.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.CustomDashLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.ryjb_info.addTab(self.tab_7, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.tableWidget_3 = QTableWidget(self.tab_2)
        if (self.tableWidget_3.columnCount() < 34):
            self.tableWidget_3.setColumnCount(34)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(13, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(14, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(15, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(16, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(17, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(18, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(19, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(20, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(21, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(22, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(23, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(24, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(25, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(26, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(27, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(28, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(29, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(30, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(31, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(32, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(33, __qtablewidgetitem51)
        if (self.tableWidget_3.rowCount() < 5):
            self.tableWidget_3.setRowCount(5)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem56)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(0, 0, 1151, 421))
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"")
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(40)
        self.ryjb_info.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget_4 = QTableWidget(self.tab_3)
        if (self.tableWidget_4.columnCount() < 15):
            self.tableWidget_4.setColumnCount(15)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(14, __qtablewidgetitem71)
        if (self.tableWidget_4.rowCount() < 5):
            self.tableWidget_4.setRowCount(5)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(4, __qtablewidgetitem76)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(0, 0, 1151, 421))
        self.tableWidget_4.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"")
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(40)
        self.ryjb_info.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableWidget_5 = QTableWidget(self.tab_4)
        if (self.tableWidget_5.columnCount() < 13):
            self.tableWidget_5.setColumnCount(13)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(10, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(11, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(12, __qtablewidgetitem89)
        if (self.tableWidget_5.rowCount() < 5):
            self.tableWidget_5.setRowCount(5)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setVerticalHeaderItem(0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setVerticalHeaderItem(1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setVerticalHeaderItem(2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setVerticalHeaderItem(3, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setVerticalHeaderItem(4, __qtablewidgetitem94)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(0, 0, 1151, 431))
        self.tableWidget_5.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"")
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(40)
        self.ryjb_info.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tableWidget_6 = QTableWidget(self.tab_5)
        if (self.tableWidget_6.columnCount() < 12):
            self.tableWidget_6.setColumnCount(12)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(10, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(11, __qtablewidgetitem106)
        if (self.tableWidget_6.rowCount() < 5):
            self.tableWidget_6.setRowCount(5)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setVerticalHeaderItem(0, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setVerticalHeaderItem(1, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setVerticalHeaderItem(2, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setVerticalHeaderItem(3, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setVerticalHeaderItem(4, __qtablewidgetitem111)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setGeometry(QRect(0, 0, 1151, 421))
        self.tableWidget_6.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"")
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget_6.verticalHeader().setDefaultSectionSize(40)
        self.ryjb_info.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tableWidget_7 = QTableWidget(self.tab_6)
        if (self.tableWidget_7.columnCount() < 15):
            self.tableWidget_7.setColumnCount(15)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(9, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(10, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(11, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(12, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(13, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(14, __qtablewidgetitem126)
        if (self.tableWidget_7.rowCount() < 5):
            self.tableWidget_7.setRowCount(5)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_7.setVerticalHeaderItem(0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_7.setVerticalHeaderItem(1, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_7.setVerticalHeaderItem(2, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_7.setVerticalHeaderItem(3, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_7.setVerticalHeaderItem(4, __qtablewidgetitem131)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setGeometry(QRect(0, 0, 1151, 421))
        self.tableWidget_7.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"")
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_7.verticalHeader().setDefaultSectionSize(40)
        self.ryjb_info.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.search)
        self.batch = QWidget()
        self.batch.setObjectName(u"batch")
        self.lb_file_batch = QLabel(self.batch)
        self.lb_file_batch.setObjectName(u"lb_file_batch")
        self.lb_file_batch.setGeometry(QRect(260, 120, 61, 31))
        self.pb_select_batch = QPushButton(self.batch)
        self.pb_select_batch.setObjectName(u"pb_select_batch")
        self.pb_select_batch.setGeometry(QRect(750, 120, 71, 31))
        self.le_input_batch = QLineEdit(self.batch)
        self.le_input_batch.setObjectName(u"le_input_batch")
        self.le_input_batch.setGeometry(QRect(330, 120, 401, 31))
        self.le_input_batch.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.gridLayoutWidget = QWidget(self.batch)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(260, 170, 471, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_sheet_batch = QLabel(self.gridLayoutWidget)
        self.lb_sheet_batch.setObjectName(u"lb_sheet_batch")

        self.gridLayout_2.addWidget(self.lb_sheet_batch, 0, 0, 1, 1)

        self.lb_colum_batch = QLabel(self.gridLayoutWidget)
        self.lb_colum_batch.setObjectName(u"lb_colum_batch")

        self.gridLayout_2.addWidget(self.lb_colum_batch, 0, 2, 1, 1)

        self.le_sheet_batch = QLineEdit(self.gridLayoutWidget)
        self.le_sheet_batch.setObjectName(u"le_sheet_batch")
        self.le_sheet_batch.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.le_sheet_batch, 0, 1, 1, 1)

        self.le_colum_batch = QLineEdit(self.gridLayoutWidget)
        self.le_colum_batch.setObjectName(u"le_colum_batch")
        self.le_colum_batch.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.le_colum_batch, 0, 3, 1, 1)

        self.lb_startrow_batch = QLabel(self.gridLayoutWidget)
        self.lb_startrow_batch.setObjectName(u"lb_startrow_batch")

        self.gridLayout_2.addWidget(self.lb_startrow_batch, 1, 0, 1, 1)

        self.le_startrow_batch = QLineEdit(self.gridLayoutWidget)
        self.le_startrow_batch.setObjectName(u"le_startrow_batch")
        self.le_startrow_batch.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.le_startrow_batch, 1, 1, 1, 1)

        self.lb_endrow_batch = QLabel(self.gridLayoutWidget)
        self.lb_endrow_batch.setObjectName(u"lb_endrow_batch")

        self.gridLayout_2.addWidget(self.lb_endrow_batch, 1, 2, 1, 1)

        self.le_endrow_batch = QLineEdit(self.gridLayoutWidget)
        self.le_endrow_batch.setObjectName(u"le_endrow_batch")
        self.le_endrow_batch.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.le_endrow_batch, 1, 3, 1, 1)

        self.lb_title_batch = QLabel(self.batch)
        self.lb_title_batch.setObjectName(u"lb_title_batch")
        self.lb_title_batch.setGeometry(QRect(380, 20, 411, 61))
        self.pb_run_batch = QPushButton(self.batch)
        self.pb_run_batch.setObjectName(u"pb_run_batch")
        self.pb_run_batch.setGeometry(QRect(750, 220, 71, 31))
        self.scrollArea = QScrollArea(self.batch)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(260, 270, 571, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 249))
        self.tb_batch = QTextEdit(self.scrollAreaWidgetContents)
        self.tb_batch.setObjectName(u"tb_batch")
        self.tb_batch.setGeometry(QRect(0, 0, 571, 251))
        self.tb_batch.setStyleSheet(u"background-color: rgb(58, 58, 58)\n"
"rgb(0, 0, 0)")
        self.tb_batch.setReadOnly(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar = QProgressBar(self.batch)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(270, 540, 561, 23))
        self.progressBar.setStyleSheet(u"background: transparent;")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.comboBox = QComboBox(self.batch)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(740, 170, 161, 31))
        self.comboBox.setEditable(False)
        self.stackedWidget.addWidget(self.batch)
        self.set = QWidget()
        self.set.setObjectName(u"set")
        self.lb_title_set = QLabel(self.set)
        self.lb_title_set.setObjectName(u"lb_title_set")
        self.lb_title_set.setGeometry(QRect(470, 20, 241, 91))
        self.label = QLabel(self.set)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 120, 151, 51))
        self.label_2 = QLabel(self.set)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 180, 101, 31))
        self.lineEdit_2 = QLineEdit(self.set)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 180, 211, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.label_3 = QLabel(self.set)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 220, 101, 31))
        self.lineEdit_3 = QLineEdit(self.set)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(310, 220, 211, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pushButton_2 = QPushButton(self.set)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 270, 71, 31))
        self.label_4 = QLabel(self.set)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(670, 120, 151, 51))
        self.stackedWidget_2 = QStackedWidget(self.set)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 0, 1178, 603))
        self.stackedWidget_2.setStyleSheet(u"background: transparent;")
        self.home_2 = QWidget()
        self.home_2.setObjectName(u"home_2")
        self.home_2.setStyleSheet(u"background-image: url(:/images/images/images/my2.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget_2.addWidget(self.home_2)
        self.login_2 = QWidget()
        self.login_2.setObjectName(u"login_2")
        self.le_idcard_login_2 = QLineEdit(self.login_2)
        self.le_idcard_login_2.setObjectName(u"le_idcard_login_2")
        self.le_idcard_login_2.setGeometry(QRect(460, 180, 300, 50))
        self.le_idcard_login_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_name_login_2 = QLineEdit(self.login_2)
        self.le_name_login_2.setObjectName(u"le_name_login_2")
        self.le_name_login_2.setGeometry(QRect(460, 250, 300, 50))
        self.le_name_login_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_user_login_2 = QLineEdit(self.login_2)
        self.le_user_login_2.setObjectName(u"le_user_login_2")
        self.le_user_login_2.setGeometry(QRect(960, 110, 191, 30))
        self.le_user_login_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_origin_login_2 = QLineEdit(self.login_2)
        self.le_origin_login_2.setObjectName(u"le_origin_login_2")
        self.le_origin_login_2.setGeometry(QRect(960, 150, 191, 30))
        self.le_origin_login_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lb_idcard_login_2 = QLabel(self.login_2)
        self.lb_idcard_login_2.setObjectName(u"lb_idcard_login_2")
        self.lb_idcard_login_2.setGeometry(QRect(350, 190, 101, 41))
        self.lb_name_login_2 = QLabel(self.login_2)
        self.lb_name_login_2.setObjectName(u"lb_name_login_2")
        self.lb_name_login_2.setGeometry(QRect(360, 260, 91, 31))
        self.lb_title_login_2 = QLabel(self.login_2)
        self.lb_title_login_2.setObjectName(u"lb_title_login_2")
        self.lb_title_login_2.setGeometry(QRect(470, 30, 231, 91))
        self.pb_rc_login_2 = QPushButton(self.login_2)
        self.pb_rc_login_2.setObjectName(u"pb_rc_login_2")
        self.pb_rc_login_2.setGeometry(QRect(460, 340, 100, 40))
        self.pb_rc_login_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pb_login_login_2 = QPushButton(self.login_2)
        self.pb_login_login_2.setObjectName(u"pb_login_login_2")
        self.pb_login_login_2.setGeometry(QRect(660, 340, 100, 40))
        self.pb_login_login_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.lb_user_login_2 = QLabel(self.login_2)
        self.lb_user_login_2.setObjectName(u"lb_user_login_2")
        self.lb_user_login_2.setGeometry(QRect(910, 110, 53, 30))
        self.lb_origin_login_2 = QLabel(self.login_2)
        self.lb_origin_login_2.setObjectName(u"lb_origin_login_2")
        self.lb_origin_login_2.setGeometry(QRect(910, 150, 53, 30))
        self.lb_statue_login_2 = QLabel(self.login_2)
        self.lb_statue_login_2.setObjectName(u"lb_statue_login_2")
        self.lb_statue_login_2.setGeometry(QRect(890, 60, 100, 40))
        self.stackedWidget_2.addWidget(self.login_2)
        self.search_2 = QWidget()
        self.search_2.setObjectName(u"search_2")
        self.search_2.setStyleSheet(u"b")
        self.verticalLayout_19 = QVBoxLayout(self.search_2)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.row_2 = QFrame(self.search_2)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.row_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.row_2)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_21.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_4 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_content_wid_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_4, 1, 0, 1, 2)


        self.horizontalLayout_10.addLayout(self.gridLayout_3)


        self.verticalLayout_21.addWidget(self.frame_content_wid_2)


        self.verticalLayout_20.addWidget(self.frame_div_content_2)


        self.verticalLayout_19.addWidget(self.row_2)

        self.row_4 = QFrame(self.search_2)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setMinimumSize(QSize(0, 150))
        self.row_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.row_4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = QTableWidget(self.row_4)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem135)
        if (self.tableWidget_2.rowCount() < 16):
            self.tableWidget_2.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setFont(font4);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem155)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_2.setPalette(palette)
        self.tableWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_13.addWidget(self.tableWidget_2)


        self.verticalLayout_19.addWidget(self.row_4)

        self.stackedWidget_2.addWidget(self.search_2)
        self.batch_2 = QWidget()
        self.batch_2.setObjectName(u"batch_2")
        self.lb_file_batch_2 = QLabel(self.batch_2)
        self.lb_file_batch_2.setObjectName(u"lb_file_batch_2")
        self.lb_file_batch_2.setGeometry(QRect(260, 120, 61, 31))
        self.pb_select_batch_2 = QPushButton(self.batch_2)
        self.pb_select_batch_2.setObjectName(u"pb_select_batch_2")
        self.pb_select_batch_2.setGeometry(QRect(784, 170, 71, 31))
        self.le_input_batch_2 = QLineEdit(self.batch_2)
        self.le_input_batch_2.setObjectName(u"le_input_batch_2")
        self.le_input_batch_2.setGeometry(QRect(330, 120, 401, 31))
        self.le_input_batch_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.gridLayoutWidget_2 = QWidget(self.batch_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(260, 170, 471, 80))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_sheet_batch_2 = QLabel(self.gridLayoutWidget_2)
        self.lb_sheet_batch_2.setObjectName(u"lb_sheet_batch_2")

        self.gridLayout_4.addWidget(self.lb_sheet_batch_2, 0, 0, 1, 1)

        self.lb_colum_batch_2 = QLabel(self.gridLayoutWidget_2)
        self.lb_colum_batch_2.setObjectName(u"lb_colum_batch_2")

        self.gridLayout_4.addWidget(self.lb_colum_batch_2, 0, 2, 1, 1)

        self.le_sheet_batch_2 = QLineEdit(self.gridLayoutWidget_2)
        self.le_sheet_batch_2.setObjectName(u"le_sheet_batch_2")
        self.le_sheet_batch_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.le_sheet_batch_2, 0, 1, 1, 1)

        self.le_colum_batch_2 = QLineEdit(self.gridLayoutWidget_2)
        self.le_colum_batch_2.setObjectName(u"le_colum_batch_2")
        self.le_colum_batch_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.le_colum_batch_2, 0, 3, 1, 1)

        self.lb_hy_batch_2 = QLabel(self.gridLayoutWidget_2)
        self.lb_hy_batch_2.setObjectName(u"lb_hy_batch_2")

        self.gridLayout_4.addWidget(self.lb_hy_batch_2, 1, 0, 1, 1)

        self.le_hy_batch_2 = QLineEdit(self.gridLayoutWidget_2)
        self.le_hy_batch_2.setObjectName(u"le_hy_batch_2")
        self.le_hy_batch_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.le_hy_batch_2, 1, 1, 1, 1)

        self.lb_other_batch_2 = QLabel(self.gridLayoutWidget_2)
        self.lb_other_batch_2.setObjectName(u"lb_other_batch_2")

        self.gridLayout_4.addWidget(self.lb_other_batch_2, 1, 2, 1, 1)

        self.le_other_batch_2 = QLineEdit(self.gridLayoutWidget_2)
        self.le_other_batch_2.setObjectName(u"le_other_batch_2")
        self.le_other_batch_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.le_other_batch_2, 1, 3, 1, 1)

        self.tb_batch_2 = QTextBrowser(self.batch_2)
        self.tb_batch_2.setObjectName(u"tb_batch_2")
        self.tb_batch_2.setGeometry(QRect(260, 270, 471, 251))
        self.tb_batch_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_jbbx_2 = QCheckBox(self.batch_2)
        self.cb_jbbx_2.setObjectName(u"cb_jbbx_2")
        self.cb_jbbx_2.setGeometry(QRect(790, 210, 141, 41))
        self.cb_jbbx_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_jbtz_2 = QCheckBox(self.batch_2)
        self.cb_jbtz_2.setObjectName(u"cb_jbtz_2")
        self.cb_jbtz_2.setGeometry(QRect(790, 260, 141, 41))
        self.cb_jbtz_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_jbinfo_2 = QCheckBox(self.batch_2)
        self.cb_jbinfo_2.setObjectName(u"cb_jbinfo_2")
        self.cb_jbinfo_2.setGeometry(QRect(790, 310, 141, 41))
        self.cb_jbinfo_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lb_title_batch_2 = QLabel(self.batch_2)
        self.lb_title_batch_2.setObjectName(u"lb_title_batch_2")
        self.lb_title_batch_2.setGeometry(QRect(380, 20, 411, 61))
        self.pb_run_batch_2 = QPushButton(self.batch_2)
        self.pb_run_batch_2.setObjectName(u"pb_run_batch_2")
        self.pb_run_batch_2.setGeometry(QRect(860, 170, 71, 31))
        self.stackedWidget_2.addWidget(self.batch_2)
        self.set_2 = QWidget()
        self.set_2.setObjectName(u"set_2")
        self.lb_title_set2 = QLabel(self.set_2)
        self.lb_title_set2.setObjectName(u"lb_title_set2")
        self.lb_title_set2.setGeometry(QRect(470, 20, 241, 91))
        self.lb_login_set = QLabel(self.set_2)
        self.lb_login_set.setObjectName(u"lb_login_set")
        self.lb_login_set.setGeometry(QRect(200, 120, 151, 51))
        self.lb_idcard_set = QLabel(self.set_2)
        self.lb_idcard_set.setObjectName(u"lb_idcard_set")
        self.lb_idcard_set.setGeometry(QRect(220, 180, 101, 31))
        self.le_idcard_set = QLineEdit(self.set_2)
        self.le_idcard_set.setObjectName(u"le_idcard_set")
        self.le_idcard_set.setGeometry(QRect(310, 180, 211, 31))
        self.le_idcard_set.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_idcard_set.setReadOnly(True)
        self.lb_name_set = QLabel(self.set_2)
        self.lb_name_set.setObjectName(u"lb_name_set")
        self.lb_name_set.setGeometry(QRect(220, 220, 101, 31))
        self.le_name_set = QLineEdit(self.set_2)
        self.le_name_set.setObjectName(u"le_name_set")
        self.le_name_set.setGeometry(QRect(310, 220, 211, 31))
        self.le_name_set.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_name_set.setReadOnly(True)
        self.pb_submit_set = QPushButton(self.set_2)
        self.pb_submit_set.setObjectName(u"pb_submit_set")
        self.pb_submit_set.setGeometry(QRect(440, 270, 71, 31))
        self.lb_path_set = QLabel(self.set_2)
        self.lb_path_set.setObjectName(u"lb_path_set")
        self.lb_path_set.setGeometry(QRect(670, 120, 151, 51))
        self.lb_path2_set = QLabel(self.set_2)
        self.lb_path2_set.setObjectName(u"lb_path2_set")
        self.lb_path2_set.setGeometry(QRect(690, 180, 101, 31))
        self.le_path_set = QLineEdit(self.set_2)
        self.le_path_set.setObjectName(u"le_path_set")
        self.le_path_set.setGeometry(QRect(740, 220, 211, 31))
        self.le_path_set.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_path_set.setReadOnly(True)
        self.pb_choose_set = QPushButton(self.set_2)
        self.pb_choose_set.setObjectName(u"pb_choose_set")
        self.pb_choose_set.setGeometry(QRect(880, 270, 71, 31))
        self.lb_host_set = QLabel(self.set_2)
        self.lb_host_set.setObjectName(u"lb_host_set")
        self.lb_host_set.setGeometry(QRect(200, 340, 151, 51))
        self.lb_jb_set = QLabel(self.set_2)
        self.lb_jb_set.setObjectName(u"lb_jb_set")
        self.lb_jb_set.setGeometry(QRect(230, 400, 101, 31))
        self.lb_JB_set = QLabel(self.set_2)
        self.lb_JB_set.setObjectName(u"lb_JB_set")
        self.lb_JB_set.setGeometry(QRect(230, 440, 101, 31))
        self.le_jb_set = QLineEdit(self.set_2)
        self.le_jb_set.setObjectName(u"le_jb_set")
        self.le_jb_set.setGeometry(QRect(320, 400, 211, 31))
        self.le_jb_set.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_jb_set.setReadOnly(True)
        self.le_JB_set = QLineEdit(self.set_2)
        self.le_JB_set.setObjectName(u"le_JB_set")
        self.le_JB_set.setGeometry(QRect(320, 440, 211, 31))
        self.le_JB_set.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_JB_set.setReadOnly(True)
        self.pb_submit_set2 = QPushButton(self.set_2)
        self.pb_submit_set2.setObjectName(u"pb_submit_set2")
        self.pb_submit_set2.setGeometry(QRect(460, 490, 71, 31))
        self.pb_edit_set = QPushButton(self.set_2)
        self.pb_edit_set.setObjectName(u"pb_edit_set")
        self.pb_edit_set.setGeometry(QRect(310, 270, 71, 31))
        self.pb_edit_set2 = QPushButton(self.set_2)
        self.pb_edit_set2.setObjectName(u"pb_edit_set2")
        self.pb_edit_set2.setGeometry(QRect(320, 490, 71, 31))
        self.lb_path_set_2 = QLabel(self.set_2)
        self.lb_path_set_2.setObjectName(u"lb_path_set_2")
        self.lb_path_set_2.setGeometry(QRect(670, 340, 151, 51))
        self.le_path_set_2 = QLineEdit(self.set_2)
        self.le_path_set_2.setObjectName(u"le_path_set_2")
        self.le_path_set_2.setGeometry(QRect(740, 440, 411, 31))
        self.le_path_set_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_path_set_2.setReadOnly(True)
        self.lb_path2_set_2 = QLabel(self.set_2)
        self.lb_path2_set_2.setObjectName(u"lb_path2_set_2")
        self.lb_path2_set_2.setGeometry(QRect(690, 400, 101, 31))
        self.pb_choose_set_2 = QPushButton(self.set_2)
        self.pb_choose_set_2.setObjectName(u"pb_choose_set_2")
        self.pb_choose_set_2.setGeometry(QRect(880, 490, 71, 31))
        self.stackedWidget_2.addWidget(self.set_2)
        self.stackedWidget.addWidget(self.set)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_background = QPushButton(self.topMenus)
        self.btn_background.setObjectName(u"btn_background")
        sizePolicy.setHeightForWidth(self.btn_background.sizePolicy().hasHeightForWidth())
        self.btn_background.setSizePolicy(sizePolicy)
        self.btn_background.setMinimumSize(QSize(0, 45))
        self.btn_background.setFont(font)
        self.btn_background.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_background.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_background.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-highligt.png);")
        self.btn_background.setIcon(icon4)

        self.verticalLayout_14.addWidget(self.btn_background)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.ryjb_info.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)
        self.stackedWidget_2.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_batch.setText(QCoreApplication.translate("MainWindow", u"Batch", None))
        self.btn_set.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u91d1\u4fdd\u4e0b\u8f7d\u5668\u6781\u901f\u7248</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.lb_idcard_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u8eab\u4efd\u8bc1\u53f7</span></p></body></html>", None))
        self.lb_name_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u59d3\u540d</span></p></body></html>", None))
        self.pb_login_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.pb_rc_login.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u914d\u7f6e", None))
        self.lb_user_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u7528\u6237</span></p></body></html>", None))
        self.le_user_login.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.le_user_login.setPlaceholderText("")
        self.lb_origin_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u673a\u6784</span></p></body></html>", None))
        self.le_origin_login.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.le_origin_login.setPlaceholderText("")
        self.pb_vpn_login.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u767b\u5f55\u5c0f\u98de\u673a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u767b\u5f55</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">\u72b6\u6001</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">\u4e2a\u4eba\u57fa\u7840\u4fe1\u606f\u67e5\u8be2</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u8eab\u4efd\u8bc1\u53f7</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u793e\u4f1a\u4fdd\u969c\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6c11\u65cf", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u65e5\u671f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u521b\u4e1a\u8bc1\u53f7\u7801", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u5458\u7c7b\u522b", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5316\u7a0b\u5ea6", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7\u7801", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u72b6\u6001", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u4eba", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u673a\u6784", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u65e5\u671f", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.ryjb_info.setTabText(self.ryjb_info.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u4eba\u5458\u57fa\u672c\u4fe1\u606f", None))
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u793e\u4f1a\u4fdd\u969c\u53f7", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u7c7b\u578b", None));
        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u53f7\u7801", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u7c7b\u578b", None));
        ___qtablewidgetitem24 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u6807\u8bb0", None));
        ___qtablewidgetitem25 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\u540d\u79f0", None));
        ___qtablewidgetitem26 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\u7edf\u4e00\u793e\u4f1a\u4fe1\u7528\u4ee3\u7801", None));
        ___qtablewidgetitem27 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\u7c7b\u578b", None));
        ___qtablewidgetitem28 = self.tableWidget_3.horizontalHeaderItem(10)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u5f62\u5f0f", None));
        ___qtablewidgetitem29 = self.tableWidget_3.horizontalHeaderItem(11)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u7c7b\u578b", None));
        ___qtablewidgetitem30 = self.tableWidget_3.horizontalHeaderItem(12)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u767b\u8bb0\u65e5\u671f", None));
        ___qtablewidgetitem31 = self.tableWidget_3.horizontalHeaderItem(13)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u65e5\u671f", None));
        ___qtablewidgetitem32 = self.tableWidget_3.horizontalHeaderItem(14)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u5730\u70b9", None));
        ___qtablewidgetitem33 = self.tableWidget_3.horizontalHeaderItem(15)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u5730\u70b9\u8be6\u7ec6\u5730\u5740", None));
        ___qtablewidgetitem34 = self.tableWidget_3.horizontalHeaderItem(16)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u804c\u4e1a\uff08\u5de5\u79cd\uff09", None));
        ___qtablewidgetitem35 = self.tableWidget_3.horizontalHeaderItem(17)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u5de5\u79cd\u540d\u79f0", None));
        ___qtablewidgetitem36 = self.tableWidget_3.horizontalHeaderItem(18)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u4e8b\u4ea7\u4e1a\u7c7b\u522b", None));
        ___qtablewidgetitem37 = self.tableWidget_3.horizontalHeaderItem(19)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u767b\u8bb0\u5931\u4e1a\u4eba\u5458", None));
        ___qtablewidgetitem38 = self.tableWidget_3.horizontalHeaderItem(20)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5c31\u4e1a\u56f0\u96be\u4eba\u5458", None));
        ___qtablewidgetitem39 = self.tableWidget_3.horizontalHeaderItem(21)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u65e5\u671f\u3010\u4e2a\u4f53\u7ecf\u8425\u3011", None));
        ___qtablewidgetitem40 = self.tableWidget_3.horizontalHeaderItem(22)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u8425\u4f4f\u6240\u3010\u4e2a\u4f53\u7ecf\u8425\u3011", None));
        ___qtablewidgetitem41 = self.tableWidget_3.horizontalHeaderItem(23)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u5185\u5bb9\u3010\u7075\u6d3b\u5c31\u4e1a\u3011", None));
        ___qtablewidgetitem42 = self.tableWidget_3.horizontalHeaderItem(24)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u5408\u540c\u5f00\u59cb\u65e5\u671f", None));
        ___qtablewidgetitem43 = self.tableWidget_3.horizontalHeaderItem(25)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u5408\u540c\u7ed3\u675f\u65e5\u671f", None));
        ___qtablewidgetitem44 = self.tableWidget_3.horizontalHeaderItem(26)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u5c97\u4f4d\u540d\u79f0", None));
        ___qtablewidgetitem45 = self.tableWidget_3.horizontalHeaderItem(27)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u5c97\u4f4d\u7f16\u7801", None));
        ___qtablewidgetitem46 = self.tableWidget_3.horizontalHeaderItem(28)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u662f\u54264050\u4eba\u5458", None));
        ___qtablewidgetitem47 = self.tableWidget_3.horizontalHeaderItem(29)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u85aa\u8d44\u62a5\u916c", None));
        ___qtablewidgetitem48 = self.tableWidget_3.horizontalHeaderItem(30)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u56f0\u96be\u4eba\u5458\u7c7b\u522b", None));
        ___qtablewidgetitem49 = self.tableWidget_3.horizontalHeaderItem(31)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u4eba", None));
        ___qtablewidgetitem50 = self.tableWidget_3.horizontalHeaderItem(32)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u673a\u6784", None));
        ___qtablewidgetitem51 = self.tableWidget_3.horizontalHeaderItem(33)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u65e5\u671f", None));
        ___qtablewidgetitem52 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem53 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem54 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem55 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem56 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.ryjb_info.setTabText(self.ryjb_info.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u767b\u8bb0\u4fe1\u606f", None))
        ___qtablewidgetitem57 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u5931\u4e1a\u767b\u8bb0\u65e5\u671f", None));
        ___qtablewidgetitem58 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u793e\u4f1a\u4fdd\u969c\u53f7\u7801", None));
        ___qtablewidgetitem59 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem60 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem61 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u7c7b\u578b", None));
        ___qtablewidgetitem62 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u53f7\u7801", None));
        ___qtablewidgetitem63 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u5386", None));
        ___qtablewidgetitem64 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u6237\u7c4d\u5730\u533a\u5212", None));
        ___qtablewidgetitem65 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u5e38\u4f4f\u5730\u533a\u5212", None));
        ___qtablewidgetitem66 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u5931\u4e1a\u65f6\u95f4", None));
        ___qtablewidgetitem67 = self.tableWidget_4.horizontalHeaderItem(10)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u5931\u4e1a\u539f\u56e0", None));
        ___qtablewidgetitem68 = self.tableWidget_4.horizontalHeaderItem(11)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u6807\u8bb0", None));
        ___qtablewidgetitem69 = self.tableWidget_4.horizontalHeaderItem(12)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u4eba", None));
        ___qtablewidgetitem70 = self.tableWidget_4.horizontalHeaderItem(13)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u673a\u6784", None));
        ___qtablewidgetitem71 = self.tableWidget_4.horizontalHeaderItem(14)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u65e5\u671f", None));
        ___qtablewidgetitem72 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem73 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem74 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem75 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem76 = self.tableWidget_4.verticalHeaderItem(4)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.ryjb_info.setTabText(self.ryjb_info.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5931\u4e1a\u767b\u8bb0\u4fe1\u606f", None))
        ___qtablewidgetitem77 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\u8bc1\u53f7", None));
        ___qtablewidgetitem78 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem79 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem80 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u7533\u8bf7\u7c7b\u578b", None));
        ___qtablewidgetitem81 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u521b\u4e1a\u8bc1\u53f7\u7801", None));
        ___qtablewidgetitem82 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"\u539f\u8bc1\u4ef6\u53f7\u7801", None));
        ___qtablewidgetitem83 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u653e\u6807\u8bb0", None));
        ___qtablewidgetitem84 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u6807\u8bb0", None));
        ___qtablewidgetitem85 = self.tableWidget_5.horizontalHeaderItem(8)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u653e\u65e5\u671f", None));
        ___qtablewidgetitem86 = self.tableWidget_5.horizontalHeaderItem(9)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u8bc1\u673a\u6784", None));
        ___qtablewidgetitem87 = self.tableWidget_5.horizontalHeaderItem(10)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u4eba", None));
        ___qtablewidgetitem88 = self.tableWidget_5.horizontalHeaderItem(11)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u673a\u6784", None));
        ___qtablewidgetitem89 = self.tableWidget_5.horizontalHeaderItem(12)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u65e5\u671f", None));
        ___qtablewidgetitem90 = self.tableWidget_5.verticalHeaderItem(0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem91 = self.tableWidget_5.verticalHeaderItem(1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem92 = self.tableWidget_5.verticalHeaderItem(2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem93 = self.tableWidget_5.verticalHeaderItem(3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem94 = self.tableWidget_5.verticalHeaderItem(4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.ryjb_info.setTabText(self.ryjb_info.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u521b\u4e1a\u8bc1\u4fe1\u606f", None))
        ___qtablewidgetitem95 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"\u793e\u4f1a\u4fdd\u969c\u53f7", None));
        ___qtablewidgetitem96 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem97 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u53f7\u7801", None));
        ___qtablewidgetitem98 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem99 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u65e5\u671f", None));
        ___qtablewidgetitem100 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"\u4f4f\u5740", None));
        ___qtablewidgetitem101 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u7535\u8bdd", None));
        ___qtablewidgetitem102 = self.tableWidget_6.horizontalHeaderItem(7)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u5458\u7c7b\u522b", None));
        ___qtablewidgetitem103 = self.tableWidget_6.horizontalHeaderItem(8)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u6807\u8bb0", None));
        ___qtablewidgetitem104 = self.tableWidget_6.horizontalHeaderItem(9)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u63f4\u52a9\u5bf9\u8c61\u7c7b\u578b", None));
        ___qtablewidgetitem105 = self.tableWidget_6.horizontalHeaderItem(10)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u63f4\u52a9\u5bf9\u8c61\u8ba4\u5b9a\u65f6\u95f4", None));
        ___qtablewidgetitem106 = self.tableWidget_6.horizontalHeaderItem(11)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u63f4\u52a9\u5bf9\u8c61\u6709\u6548\u671f\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem107 = self.tableWidget_6.verticalHeaderItem(0)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem108 = self.tableWidget_6.verticalHeaderItem(1)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem109 = self.tableWidget_6.verticalHeaderItem(2)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem110 = self.tableWidget_6.verticalHeaderItem(3)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem111 = self.tableWidget_6.verticalHeaderItem(4)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.ryjb_info.setTabText(self.ryjb_info.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u5c31\u4e1a\u56f0\u96be\u4eba\u5458\u8ba4\u5b9a\u4fe1\u606f", None))
        ___qtablewidgetitem112 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem113 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4ef6\u53f7\u7801", None));
        ___qtablewidgetitem114 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem115 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"\u804c\u4e1a\u5de5\u79cd\u540d\u79f0", None));
        ___qtablewidgetitem116 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"\u804c\u4e1a\u65b9\u5411", None));
        ___qtablewidgetitem117 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"\u6280\u80fd\u7b49\u7ea7", None));
        ___qtablewidgetitem118 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"\u7406\u8bba\u77e5\u8bc6\u8003\u8bd5\u6210\u7ee9", None));
        ___qtablewidgetitem119 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"\u6280\u80fd\u8003\u6838\u6210\u7ee9", None));
        ___qtablewidgetitem120 = self.tableWidget_7.horizontalHeaderItem(8)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5b9a\u6210\u7ee9", None));
        ___qtablewidgetitem121 = self.tableWidget_7.horizontalHeaderItem(9)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5316\u7a0b\u5ea6", None));
        ___qtablewidgetitem122 = self.tableWidget_7.horizontalHeaderItem(10)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"\u8bc1\u4e66\u7f16\u53f7", None));
        ___qtablewidgetitem123 = self.tableWidget_7.horizontalHeaderItem(11)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u8bc1\u65e5\u671f", None));
        ___qtablewidgetitem124 = self.tableWidget_7.horizontalHeaderItem(12)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"\u804c\u4e1a\u6280\u80fd\u9274\u5b9a\u673a\u6784", None));
        ___qtablewidgetitem125 = self.tableWidget_7.horizontalHeaderItem(13)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u8bc1\u673a\u5173", None));
        ___qtablewidgetitem126 = self.tableWidget_7.horizontalHeaderItem(14)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8d23\u4efb\u5355\u4f4d", None));
        ___qtablewidgetitem127 = self.tableWidget_7.verticalHeaderItem(0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem128 = self.tableWidget_7.verticalHeaderItem(1)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem129 = self.tableWidget_7.verticalHeaderItem(2)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem130 = self.tableWidget_7.verticalHeaderItem(3)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem131 = self.tableWidget_7.verticalHeaderItem(4)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.ryjb_info.setTabText(self.ryjb_info.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u804c\u4e1a\u8d44\u683c\u8bc1\u4e66\u4fe1\u606f", None))
        self.lb_file_batch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u6587\u4ef6\u8def\u5f84</span></p></body></html>", None))
        self.pb_select_batch.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.le_input_batch.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_input_batch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9excel\u6587\u4ef6\u8def\u5f84", None))
        self.lb_sheet_batch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Sheet\u8868</span></p></body></html>", None))
        self.lb_colum_batch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u5217\u53f7</span></p></body></html>", None))
        self.le_sheet_batch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u7b2c\u4e00\u4e2aSheet\u8868", None))
        self.le_colum_batch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4A\u5217", None))
        self.lb_startrow_batch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u9996\u884c</span></p></body></html>", None))
        self.le_startrow_batch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u884c\uff0c\u9ed8\u8ba4\u7b2c\u4e00\u884c", None))
        self.lb_endrow_batch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u5c3e\u884c</span></p></body></html>", None))
        self.le_endrow_batch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u884c\uff0c\u9ed8\u8ba4\u6570\u636e\u6700\u540e\u4e00\u884c", None))
        self.lb_title_batch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u6279\u91cf\u5bfc\u51fa\u67e5\u8be2\u7ed3\u679c</span></p></body></html>", None))
        self.pb_run_batch.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u7aef\u53c2\u4fdd\u60c5\u51b5", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u91d1\u4fdd\u53f0\u8d26\u8be6\u60c5", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u91d1\u4fdd\u4e2a\u4eba\u57fa\u672c\u4fe1\u606f", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u9879\u76ee", None))
        self.lb_title_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u8bbe\u7f6e</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u914d\u7f6e\u767b\u5f55\u4fe1\u606f\uff1a</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u8eab\u4efd\u8bc1\u53f7</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u59d3\u540d</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u914d\u7f6e\u5bfc\u51fa\u8def\u5f84\uff1a</span></p></body></html>", None))
        self.lb_idcard_login_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u8eab\u4efd\u8bc1\u53f7</span></p></body></html>", None))
        self.lb_name_login_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u59d3\u540d</span></p></body></html>", None))
        self.lb_title_login_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700;\">\u767b\u5f55</span></p></body></html>", None))
        self.pb_rc_login_2.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u914d\u7f6e", None))
        self.pb_login_login_2.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.lb_user_login_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u7528\u6237</span></p></body></html>", None))
        self.lb_origin_login_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u673a\u6784</span></p></body></html>", None))
        self.lb_statue_login_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u767b\u5f55\u72b6\u6001\uff1a</span></p></body></html>", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        ___qtablewidgetitem132 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem133 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem134 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem135 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem136 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem137 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem138 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem139 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem140 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem141 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem142 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem143 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem144 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem145 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem146 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem147 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem148 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem149 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem150 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem151 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem152 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem153 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem154 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem155 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.lb_file_batch_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u6587\u4ef6\u8def\u5f84</span></p></body></html>", None))
        self.pb_select_batch_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.le_input_batch_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_sheet_batch_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Sheet\u8868</span></p></body></html>", None))
        self.lb_colum_batch_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u5217\u53f7</span></p></body></html>", None))
        self.lb_hy_batch_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u884c\u57df</span></p></body></html>", None))
        self.lb_other_batch_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">\u5176\u4ed6</span></p></body></html>", None))
        self.cb_jbbx_2.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u529e\u7aef\u4fdd\u9669", None))
        self.cb_jbtz_2.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u4fdd\u53f0\u8d26", None))
        self.cb_jbinfo_2.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u4fdd\u4e2a\u4eba\u57fa\u672c\u4fe1\u606f", None))
        self.lb_title_batch_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u6279\u91cf\u5bfc\u51fa\u67e5\u8be2\u7ed3\u679c</span></p></body></html>", None))
        self.pb_run_batch_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.lb_title_set2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u8bbe\u7f6e</span></p></body></html>", None))
        self.lb_login_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u914d\u7f6e\u767b\u5f55\u4fe1\u606f\uff1a</span></p></body></html>", None))
        self.lb_idcard_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u8eab\u4efd\u8bc1\u53f7</span></p></body></html>", None))
        self.lb_name_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u59d3\u540d</span></p></body></html>", None))
        self.pb_submit_set.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.lb_path_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u914d\u7f6e\u5bfc\u51fa\u8def\u5f84\uff1a</span></p></body></html>", None))
        self.lb_path2_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u9009\u62e9\u8def\u5f84\uff1a</span></p></body></html>", None))
        self.pb_choose_set.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.lb_host_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u914d\u7f6e\u4e3b\u673a\u5730\u5740\uff1a</span></p></body></html>", None))
        self.lb_jb_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u91d1\u4fdd</span></p></body></html>", None))
        self.lb_JB_set.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u7ecf\u529e</span></p></body></html>", None))
        self.pb_submit_set2.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.pb_edit_set.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.pb_edit_set2.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.lb_path_set_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u914d\u7f6e\u5c0f\u98de\u673a\u8def\u5f84\uff1a</span></p></body></html>", None))
        self.lb_path2_set_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u9009\u62e9\u8def\u5f84\uff1a</span></p></body></html>", None))
        self.pb_choose_set_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.btn_background.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Whatever,", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

