import sys, re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from captcha.image import ImageCaptcha
import smtplib
from email.mime.text import MIMEText
from random import randint
import cv2
import numpy as np


class Ui_Feedback(object):
    def setupUi(self, Feedback):
        Feedback.setObjectName("Feedback")
        Feedback.resize(500, 450)
        Feedback.setMinimumSize(QtCore.QSize(500, 450))
        Feedback.setMaximumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Feedback.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Feedback.sizePolicy().hasHeightForWidth())
        Feedback.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(Feedback)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 481, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(210, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(210, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.widget = QtWidgets.QWidget(Feedback)
        self.widget.setGeometry(QtCore.QRect(10, 410, 479, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)

        self.retranslateUi(Feedback)
        QtCore.QMetaObject.connectSlotsByName(Feedback)

    def retranslateUi(self, Feedback):
        _translate = QtCore.QCoreApplication.translate
        Feedback.setWindowTitle(_translate("Feedback", "意见反馈"))
        self.label.setText(_translate("Feedback", "意见反馈"))
        self.label_2.setText(_translate("Feedback", "如果有任何问题、意见或建议，请写在下面并发送给作者。"))
        self.label_3.setText(_translate("Feedback",
                                        "<html><head/><body><p>您的Email:<span style=\" color:#ff0000; vertical-align:super;\">*</span></p></body></html>"))
        self.label_4.setText(_translate("Feedback", "　　　　　 回复将发送到这个Email地址"))
        self.label_5.setText(_translate("Feedback",
                                        "<html><head/><body><p>意见内容:<span style=\" color:#ff0000; vertical-align:super;\">*</span></p></body></html>"))
        self.label_6.setText(_translate("Feedback",
                                        "<html><head/><body><p>验证码:<span style=\" color:#ff0000; vertical-align:super;\">*</span></p></body></html>"))
        self.label_8.setText(_translate("Feedback", "单击更换验证码"))
        self.pushButton_2.setText(_translate("Feedback", "提交"))
        self.pushButton.setText(_translate("Feedback", "关闭"))


class win_Feedback(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(win_Feedback, self).__init__(parent)
        self.ui = Ui_Feedback()
        self.ui.setupUi(self)
        self.init_slots()
        self.generate_authCode()

    def generate_authCode(self):
        ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.code = ''
        for i in range(4):
            self.code += ls[randint(0, 61)]
        img = ImageCaptcha().generate_image(self.code)
        image = cv2.resize(np.asarray(img), dsize=(75, 25), interpolation=cv2.INTER_AREA)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        QtImg = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_ARGB32)
        self.ui.label_7.setPixmap(QtGui.QPixmap.fromImage(QtImg))

    def init_slots(self):
        self.ui.pushButton.clicked.connect(self.Close)
        self.ui.pushButton_2.clicked.connect(self.submit)

    def mousePressEvent(self, qme):
        if self.childAt(qme.x(), qme.y()) is self.ui.label_7:
            self.generate_authCode()

    def submit(self):
        if self.ui.lineEdit.text() == "":
            QMessageBox.warning(self, u"中国象棋自动打谱工具", u"请填写邮箱！")
            return
        if not re.findall('^\w+@\w+\.com$', self.ui.lineEdit.text()):
            QMessageBox.warning(self, u"中国象棋自动打谱工具", u"请填写正确的邮箱格式！")
            return
        if self.ui.textEdit.toPlainText() == "":
            QMessageBox.warning(self, u"中国象棋自动打谱工具", u"意见内容不能为空！")
            return
        if self.ui.lineEdit_2.text() != self.code:
            warningText = "请填写验证码！" if self.ui.lineEdit_2.text() == "" else "验证码错误！"
            QMessageBox.warning(self, u"中国象棋自动打谱工具", warningText)
            return
        s = smtplib.SMTP("smtp.163.com", 25)
        s.login("loggy12@163.com", "TZDAMKTDUDKSHXVR")
        msg = self.ui.textEdit.toPlainText()
        msg += "\n邮箱：%s" % self.ui.lineEdit.text()
        msg = MIMEText(msg)
        msg["Subject"] = "象棋自动打谱系统的意见反馈"
        msg["From"] = "loggy12@163.com"
        msg["To"] = "773645385@qq.com"
        s.sendmail("loggy12@163.com", "773645385@qq.com", msg.as_string())
        QMessageBox.information(self, u"中国象棋自动打谱工具", u"意见提交成功，感谢您的反馈！")

    def Close(self):
        self.close()
