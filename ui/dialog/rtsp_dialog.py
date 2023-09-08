# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(744, 41)
        Form.setMinimumSize(QSize(0, 40))
        Form.setMaximumSize(QSize(16777215, 41))
        icon = QIcon()
        icon.addFile(u":/all/img/logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"#Form{\n"
"background:qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(48, 167, 217), stop:1 rgb(5,150,229))\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"QLabel{font-family: \"Microsoft YaHei\";\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color:white;}")

        self.horizontalLayout.addWidget(self.label)

        self.rtspEdit = QLineEdit(Form)
        self.rtspEdit.setObjectName(u"rtspEdit")
        self.rtspEdit.setMinimumSize(QSize(0, 31))
        self.rtspEdit.setStyleSheet(u"background-color: rgb(207, 207, 207);\n"
"	background-color: #f7f7f7;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 5px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"	padding-left: 12px; /* \u6587\u672c\u8ddd\u79bb\u5de6\u8fb9\u754c\u67095px */\n"
"font-family: \"Microsoft YaHei\";\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.rtspEdit)

        self.rtspButton = QPushButton(Form)
        self.rtspButton.setObjectName(u"rtspButton")
        self.rtspButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
"width:70px;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding: 5px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(144, 0, 255, 0.8);\n"
"border-radius: 3px;\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radiu"
                        "s: 3px;\n"
"                     background-color:  rgba(255,255,255,150);}\n"
"\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 3px;\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.rtspButton)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
"width:70px;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding: 5px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(144, 0, 255, 0.8);\n"
"border-radius: 3px;\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radiu"
                        "s: 3px;\n"
"                     background-color:  rgba(255,255,255,150);}\n"
"\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 3px;\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"RTSP监控", None))
        self.label.setText(QCoreApplication.translate("Form", u"rtsp address:", None))
        self.rtspEdit.setText("")
        self.rtspButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
    # retranslateUi

