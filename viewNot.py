from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import win32con
from win32clipboard import OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData


class Ui_ViewNotation(object):
    def setupUi(self, viewNotation):
        viewNotation.setObjectName("viewNotation")
        viewNotation.resize(450, 600)
        viewNotation.setMinimumSize(QtCore.QSize(450, 600))
        viewNotation.setMaximumSize(QtCore.QSize(450, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        viewNotation.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(viewNotation)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 455, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.notation = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.notation.setObjectName("notation")
        self.verticalLayout.addWidget(self.notation)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(viewNotation)
        QtCore.QMetaObject.connectSlotsByName(viewNotation)

    def retranslateUi(self, viewNotation):
        _translate = QtCore.QCoreApplication.translate
        viewNotation.setWindowTitle(_translate("viewNotation", "查看文本棋谱"))
        self.pushButton_2.setText(_translate("viewNotation", "复制"))
        self.pushButton.setText(_translate("viewNotation", "关闭"))


class win_ViewNotation(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(win_ViewNotation, self).__init__(parent)
        self.ui = Ui_ViewNotation()
        self.ui.setupUi(self)
        self.init_slots()

    def init_slots(self):
        self.ui.pushButton_2.clicked.connect(self.copy)
        self.ui.pushButton.clicked.connect(self.Close)

    def copy(self):
        OpenClipboard()
        EmptyClipboard()
        SetClipboardData(win32con.CF_UNICODETEXT, self.ui.notation.toPlainText())
        CloseClipboard()
        QtWidgets.QMessageBox.information(self, u"中国象棋自动打谱工具", u"棋谱已复制到剪贴板。")

    def Close(self):
        self.close()

    def get_data_notation(self, notation):
        self.ui.notation.setText(notation)