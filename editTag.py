from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox


class Ui_EditTag(object):
    def setupUi(self, EditTag):
        EditTag.setObjectName("EditTag")
        EditTag.resize(438, 338)
        EditTag.setMinimumSize(QtCore.QSize(438, 338))
        EditTag.setMaximumSize(QtCore.QSize(438, 338))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditTag.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditTag.sizePolicy().hasHeightForWidth())
        EditTag.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(EditTag)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 420, 191))
        self.groupBox.setMinimumSize(QtCore.QSize(420, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(420, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 222, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.event = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.event.setObjectName("event")
        self.horizontalLayout_9.addWidget(self.event)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.round = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.round.setObjectName("round")
        self.horizontalLayout_8.addWidget(self.round)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.date = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.date.setObjectName("date")
        self.horizontalLayout_7.addWidget(self.date)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.site = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.site.setObjectName("site")
        self.horizontalLayout_2.addWidget(self.site)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(240, 19, 351, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 163, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.unitOfRed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.unitOfRed.setObjectName("unitOfRed")
        self.gridLayout.addWidget(self.unitOfRed, 0, 1, 1, 1)
        self.playerOfRed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.playerOfRed.setObjectName("playerOfRed")
        self.gridLayout.addWidget(self.playerOfRed, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 163, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.unitOfBlack = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.unitOfBlack.setObjectName("unitOfBlack")
        self.gridLayout_2.addWidget(self.unitOfBlack, 0, 1, 1, 1)
        self.playerOfBlack = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.playerOfBlack.setObjectName("playerOfBlack")
        self.gridLayout_2.addWidget(self.playerOfBlack, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(EditTag)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 420, 91))
        self.groupBox_4.setMinimumSize(QtCore.QSize(420, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(420, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 401, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)
        self.ECCO = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ECCO.setMinimumSize(QtCore.QSize(30, 0))
        self.ECCO.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ECCO.setObjectName("ECCO")
        self.gridLayout_4.addWidget(self.ECCO, 1, 1, 1, 1)
        self.opening = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.opening.setMinimumSize(QtCore.QSize(360, 0))
        self.opening.setMaximumSize(QtCore.QSize(360, 16777215))
        self.opening.setObjectName("opening")
        self.gridLayout_4.addWidget(self.opening, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(EditTag)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 300, 241, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_decide = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_decide.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_decide.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_decide.setObjectName("pushButton_decide")
        self.horizontalLayout_4.addWidget(self.pushButton_decide)
        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_cancel)

        self.retranslateUi(EditTag)
        QtCore.QMetaObject.connectSlotsByName(EditTag)

    def retranslateUi(self, EditTag):
        _translate = QtCore.QCoreApplication.translate
        EditTag.setWindowTitle(_translate("EditTag", "编辑标签"))
        self.groupBox.setTitle(_translate("EditTag", "比赛"))
        self.label_6.setText(_translate("EditTag", "赛事"))
        self.label_5.setText(_translate("EditTag", "轮次"))
        self.label_4.setText(_translate("EditTag", "日期"))
        self.label.setText(_translate("EditTag", "地点"))
        self.label_2.setText(_translate("EditTag", "结果"))
        self.comboBox.setItemText(0, _translate("EditTag", "未知"))
        self.comboBox.setItemText(1, _translate("EditTag", "红胜"))
        self.comboBox.setItemText(2, _translate("EditTag", "黑胜"))
        self.comboBox.setItemText(3, _translate("EditTag", "和棋"))
        self.groupBox_3.setTitle(_translate("EditTag", "红方"))
        self.label_8.setText(_translate("EditTag", "选手 "))
        self.label_7.setText(_translate("EditTag", "单位 "))
        self.groupBox_2.setTitle(_translate("EditTag", "黑方"))
        self.label_10.setText(_translate("EditTag", "选手 "))
        self.label_9.setText(_translate("EditTag", "单位 "))
        self.groupBox_4.setTitle(_translate("EditTag", "开局"))
        self.label_3.setText(_translate("EditTag", "开局"))
        self.label_13.setText(_translate("EditTag", "ECCO"))
        self.pushButton_decide.setText(_translate("EditTag", "确定"))
        self.pushButton_cancel.setText(_translate("EditTag", "取消"))


class win_EditTag(QtWidgets.QMainWindow):
    signal_notation = pyqtSignal(list)

    def __init__(self, parent=None):
        super(win_EditTag, self).__init__(parent)
        self.ui = Ui_EditTag()
        self.ui.setupUi(self)
        self.init_slots()

    def init_slots(self):
        self.ui.pushButton_decide.clicked.connect(self.decide)
        self.ui.pushButton_cancel.clicked.connect(self.Close)

    def decide(self):
        if self.ui.round.text() != "" and not self.ui.round.text().isdigit():
            QMessageBox.warning(self, u"中国象棋自动打谱工具", u"轮次必须为数字！")
            return
        if (self.ui.playerOfRed.text() != "" and any(char.isdigit() for char in self.ui.playerOfRed.text())) or \
                (self.ui.playerOfBlack.text() != "" and any(char.isdigit() for char in self.ui.playerOfBlack.text())):
            QMessageBox.warning(self, u"中国象棋自动打谱工具", u"选手名字不得包含数字！")
            return
        if self.ui.ECCO.text() != "":
            if len(self.ui.ECCO.text()) == 3:
                if not (self.ui.ECCO.text()[0].isalpha() and self.ui.ECCO.text()[1: 3].isdigit()):
                    QMessageBox.warning(self, u"中国象棋自动打谱工具", u"请输入正确的ECCO编号，格式为1位字母+2位数字")
                    return
            else:
                QMessageBox.warning(self, u"中国象棋自动打谱工具", u"请输入正确的ECCO编号，格式为1位字母+2位数字")
                return
        if self.ui.opening.text() != "" and any(char.isdigit() for char in self.ui.opening.text()):
            QMessageBox.warning(self, u"中国象棋自动打谱工具", u"开局名称不得包含数字！")
            return
        ls = ["" for _ in range(11)]
        ls[0] = self.ui.event.text()
        ls[1] = self.ui.round.text()
        ls[2] = self.ui.date.text()
        ls[3] = self.ui.site.text()
        ls[4] = self.ui.unitOfRed.text()
        ls[5] = self.ui.playerOfRed.text()
        ls[6] = self.ui.unitOfBlack.text()
        ls[7] = self.ui.playerOfBlack.text()
        ls[8] = self.ui.comboBox.currentText()
        ls[9] = self.ui.ECCO.text()
        ls[10] = self.ui.opening.text()
        self.signal_notation.emit(ls)
        self.close()

    def Close(self):
        self.close()

    def get_data_notation(self, ls):
        self.ui.event.setText(ls[0])
        self.ui.round.setText(ls[1])
        self.ui.date.setText(ls[2])
        self.ui.site.setText(ls[3])
        self.ui.unitOfRed.setText(ls[4])
        self.ui.playerOfRed.setText(ls[5])
        self.ui.unitOfBlack.setText(ls[6])
        self.ui.playerOfBlack.setText(ls[7])
        self.ui.comboBox.setCurrentText(ls[8])
        self.ui.ECCO.setText(ls[9])
        self.ui.opening.setText(ls[10])
