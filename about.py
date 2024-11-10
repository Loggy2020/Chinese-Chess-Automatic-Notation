from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(534, 252)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QtCore.QSize(534, 252))
        About.setMaximumSize(QtCore.QSize(534, 252))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(About)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 14, 491, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 269))
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/logo2.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(400, 200))
        self.label_2.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "关于自动打谱系统"))
        self.label_2.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600;\">中国象棋自动打谱系统</span></p><p>版本 1.0</p><p>中国象棋自动打谱系统是为中国象棋开发的基于计算机视觉的自动打谱系统。</p><p>戴林鑫 保留所有权利</p></body></html>"))


class win_About(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(win_About, self).__init__(parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)