# -*-coding: utf-8 -*-
import os
import sys
import numpy as np
import copy
from skimage import measure
import time
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal
# 以下导入其它界面
from editTag import win_EditTag
from options import win_Options
from releaseNot import win_ReleaseNotation
from viewNot import win_ViewNotation
from manual import win_Manual
from feedback import win_Feedback
from about import win_About


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(840, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(840, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_video.setObjectName("pushButton_video")
        self.horizontalLayout_5.addWidget(self.pushButton_video)
        self.filePath = QtWidgets.QTextBrowser(self.centralwidget)
        self.filePath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.filePath.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.filePath.setReadOnly(False)
        self.filePath.setAcceptRichText(False)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout_5.addWidget(self.filePath)
        self.pushButton_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_img.setObjectName("pushButton_img")
        self.horizontalLayout_5.addWidget(self.pushButton_img)
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_camera.setObjectName("pushButton_camera")
        self.horizontalLayout_5.addWidget(self.pushButton_camera)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(1677215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(0, 700))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setMinimumSize(QtCore.QSize(150, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(0, 11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.progressBar = QtWidgets.QSlider(self.groupBox_2)
        self.progressBar.setEnabled(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_8.addWidget(self.progressBar)
        self.nowTime = QtWidgets.QLabel(self.groupBox_2)
        self.nowTime.setObjectName("nowTime")
        self.horizontalLayout_8.addWidget(self.nowTime)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.totalTime = QtWidgets.QLabel(self.groupBox_2)
        self.totalTime.setObjectName("totalTime")
        self.horizontalLayout_8.addWidget(self.totalTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_start.setEnabled(False)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_stop.setEnabled(False)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.pushButton_skip = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_skip.setEnabled(False)
        self.pushButton_skip.setObjectName("pushButton_skip")
        self.horizontalLayout.addWidget(self.pushButton_skip)
        self.pushButton_finish = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_finish.setEnabled(False)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.horizontalLayout.addWidget(self.pushButton_finish)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.action_open = QtWidgets.QMenu(self.menu)
        self.action_open.setObjectName("action_open")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menuBar)
        self.action_video = QtWidgets.QAction(MainWindow)
        self.action_video.setObjectName("action_video")
        self.action_image = QtWidgets.QAction(MainWindow)
        self.action_image.setObjectName("action_image")
        self.action_camera = QtWidgets.QAction(MainWindow)
        self.action_camera.setObjectName("action_camera")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setShortcutVisibleInContextMenu(True)
        self.action_save.setEnabled(False)
        self.action_save.setObjectName("action_save")
        self.action_saveAs = QtWidgets.QAction(MainWindow)
        self.action_saveAs.setShortcutVisibleInContextMenu(True)
        self.action_saveAs.setEnabled(False)
        self.action_saveAs.setObjectName("action_saveAs")
        self.action_view = QtWidgets.QAction(MainWindow)
        self.action_view.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_view.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action_view.setShortcutVisibleInContextMenu(True)
        self.action_view.setObjectName("action_view")
        self.action_eidtTag = QtWidgets.QAction(MainWindow)
        self.action_eidtTag.setObjectName("action_eidtTag")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_viewLog = QtWidgets.QAction(MainWindow)
        self.action_viewLog.setObjectName("action_viewLog")
        self.action_quit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.action_quit.setObjectName("action_quit")
        self.action_detect = QtWidgets.QAction(MainWindow)
        self.action_detect.setEnabled(False)
        self.action_detect.setShortcutVisibleInContextMenu(True)
        self.action_detect.setObjectName("action_detect")
        self.action_stop = QtWidgets.QAction(MainWindow)
        self.action_stop.setEnabled(False)
        self.action_stop.setShortcutVisibleInContextMenu(True)
        self.action_stop.setObjectName("action_stop")
        self.action_skip = QtWidgets.QAction(MainWindow)
        self.action_skip.setEnabled(False)
        self.action_skip.setShortcutVisibleInContextMenu(True)
        self.action_skip.setObjectName("action_skip")
        self.action_finish = QtWidgets.QAction(MainWindow)
        self.action_finish.setEnabled(False)
        self.action_finish.setShortcutVisibleInContextMenu(True)
        self.action_finish.setObjectName("action_finish")
        self.action_release = QtWidgets.QAction(MainWindow)
        self.action_release.setEnabled(False)
        self.action_release.setObjectName("action_release")
        self.action_options = QtWidgets.QAction(MainWindow)
        self.action_options.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.action_options.setObjectName("action_options")
        self.action_feedback = QtWidgets.QAction(MainWindow)
        self.action_feedback.setObjectName("action_feedback")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setMenuRole(QtWidgets.QAction.AboutRole)
        self.action_about.setObjectName("action_about")
        self.action_manual = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/用户手册.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_manual.setIcon(icon1)
        self.action_manual.setShortcutVisibleInContextMenu(True)
        self.action_manual.setObjectName("action_manual")
        self.action_open.addAction(self.action_video)
        self.action_open.addAction(self.action_image)
        self.action_open.addAction(self.action_camera)
        self.menu.addAction(self.action_open.menuAction())
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveAs)
        self.menu.addSeparator()
        self.menu.addAction(self.action_view)
        self.menu.addAction(self.action_eidtTag)
        self.menu.addSeparator()
        self.menu.addAction(self.action_viewLog)
        self.menu.addAction(self.action_quit)
        self.menu_2.addAction(self.action_detect)
        self.menu_2.addAction(self.action_stop)
        self.menu_2.addAction(self.action_skip)
        self.menu_2.addAction(self.action_finish)
        self.menu_2.addAction(self.action_release)
        self.menu_3.addAction(self.action_options)
        self.menu_4.addAction(self.action_manual)
        self.menu_4.addAction(self.action_feedback)
        self.menu_4.addAction(self.action_about)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中国象棋自动打谱工具"))
        self.label_2.setText(_translate("MainWindow", "请选择检测源"))
        self.pushButton_video.setText(_translate("MainWindow", "打开视频"))
        self.pushButton_img.setText(_translate("MainWindow", "打开图片"))
        self.pushButton_camera.setText(_translate("MainWindow", "打开摄像头"))
        self.groupBox_2.setTitle(_translate("MainWindow", "操作区"))
        self.label_3.setText(_translate("MainWindow", "检测结果"))
        self.label_4.setText(_translate("MainWindow", "着法列表"))
        self.label.setText(_translate("MainWindow", "[视频区域]"))
        self.nowTime.setText(_translate("MainWindow", "00:00"))
        self.label_7.setText(_translate("MainWindow", "/"))
        self.totalTime.setText(_translate("MainWindow", "00:00"))
        self.pushButton_start.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_stop.setText(_translate("MainWindow", "暂停/继续"))
        self.pushButton_skip.setText(_translate("MainWindow", "快进"))
        self.pushButton_finish.setText(_translate("MainWindow", "结束检测"))
        self.pushButton_save.setText(_translate("MainWindow", "保存棋谱"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.action_open.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "操作"))
        self.menu_3.setTitle(_translate("MainWindow", "选项"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.action_video.setText(_translate("MainWindow", "视频..."))
        self.action_image.setText(_translate("MainWindow", "图片..."))
        self.action_camera.setText(_translate("MainWindow", "摄像头..."))
        self.action_save.setText(_translate("MainWindow", "保存(S)"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_saveAs.setText(_translate("MainWindow", "另存为(A)..."))
        self.action_saveAs.setIconText(_translate("MainWindow", "另存为(A)..."))
        self.action_saveAs.setToolTip(_translate("MainWindow", "另存为(A)..."))
        self.action_saveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_view.setText(_translate("MainWindow", "查看棋谱文本(V)"))
        self.action_view.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_eidtTag.setText(_translate("MainWindow", "编辑标签(T)..."))
        self.action_eidtTag.setIconText(_translate("MainWindow", "编辑标签(T)..."))
        self.action_eidtTag.setToolTip(_translate("MainWindow", "编辑标签(T)..."))
        self.action_viewLog.setText(_translate("MainWindow", "查看系统日志"))
        self.action_quit.setText(_translate("MainWindow", "退出(X)"))
        self.action_detect.setText(_translate("MainWindow", "开始检测"))
        self.action_detect.setShortcut(_translate("MainWindow", "F5"))
        self.action_stop.setText(_translate("MainWindow", "暂停/继续"))
        self.action_stop.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_skip.setText(_translate("MainWindow", "快进"))
        self.action_skip.setShortcut(_translate("MainWindow", "Right"))
        self.action_finish.setText(_translate("MainWindow", "结束检测"))
        self.action_finish.setShortcut(_translate("MainWindow", "Esc"))
        self.action_release.setText(_translate("MainWindow", "发布棋谱/图片..."))
        self.action_options.setText(_translate("MainWindow", "设置(O)..."))
        self.action_manual.setText(_translate("MainWindow", "用户手册(M)"))
        self.action_manual.setShortcut(_translate("MainWindow", "F1"))
        self.action_feedback.setText(_translate("MainWindow", "意见反馈..."))
        self.action_about.setText(_translate("MainWindow", "关于(A)"))


class win_Main(QtWidgets.QMainWindow):
    signal_int = pyqtSignal(int)  # 传送列表的信号
    signal_list = pyqtSignal(list)  # 编辑标签传送列表的信号
    signal_list2 = pyqtSignal(list)  # 发布棋谱传送列表的信号
    signal_str = pyqtSignal(str)  # 传送字符串的信号
    signal_img = pyqtSignal(np.ndarray)  # 传送图像的信号
    signal_opt = pyqtSignal(float, float, int, str, int, int, int, int, float)  # 传送设置的信号

    def __init__(self, parent=None):
        super(win_Main, self).__init__(parent)
        self.timer_video = QtCore.QTimer()  # 创建定时器
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_slots()
        self.cap = cv2.VideoCapture()
        self.stopFlag = 1  # 暂停与播放辅助信号，note：通过奇偶来控制暂停与播放
        self.type = 0  # 检测源，1为图片，2为视频，3为摄像头
        self.cameraFlag = False
        self.skip = False
        # 变量初始化
        self.tag = ["", "", "", "", "", "", "", "", "未知", "", ""]
        self.skipTime, self.detectGap = 10, 0.25  # 分别为快进幅度和每隔多少秒检测一次
        self.format = 2  # 棋谱布局
        self.savePath = ""  # 默认保存路径
        self.logPath = os.getcwd().replace('\\','/')  # 系统日志的保存路径
        self.houghmin, self.houghmax = 20, 35  # 检测到圆的最小半径，检测到圆的的最大半径
        self.para1, self.para2 = 1000, 20  # hough圆的两个参数
        self.radiousRate = 0.6

    def MessageBox(self, title, dialog):
        msg_box = QMessageBox(self)  # 实例化一个QMessageBox对象
        msg_box.setWindowTitle(title)  # 设置对话框的标题
        msg_box.setText(dialog)  # 设置对话框的内容
        msg_box.setIcon(QMessageBox.Question)
        # 调用addButton方法传入字符串，确定按钮扮演的角色
        msg_box.addButton("是", QMessageBox.YesRole)
        msg_box.addButton("否", QMessageBox.NoRole)
        msg_box.exec()
        return msg_box.clickedButton().text()

    # 控件绑定相关操作
    def init_slots(self):
        self.ui.pushButton_img.clicked.connect(self.getImage)
        self.ui.pushButton_video.clicked.connect(self.getVideo)
        self.ui.pushButton_camera.clicked.connect(self.openCamera)
        self.ui.pushButton_start.clicked.connect(self.startDetect)
        self.ui.pushButton_skip.clicked.connect(self.fastForward)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_finish.clicked.connect(self.finish)
        self.ui.pushButton_save.clicked.connect(self.save)
        self.timer_video.timeout.connect(self.openFrame)
        # 菜单操作
        self.ui.action_video.triggered.connect(self.getVideo)
        self.ui.action_image.triggered.connect(self.getImage)
        self.ui.action_camera.triggered.connect(self.openCamera)
        self.ui.action_save.triggered.connect(self.save)
        self.ui.action_saveAs.triggered.connect(self.save)
        self.ui.action_view.triggered.connect(self.viewNotation)
        self.ui.action_eidtTag.triggered.connect(self.editTag)
        self.ui.action_viewLog.triggered.connect(self.viewLog)
        self.ui.action_quit.triggered.connect(self.quit)
        self.ui.action_detect.triggered.connect(self.startDetect)
        self.ui.action_stop.triggered.connect(self.stop)
        self.ui.action_skip.triggered.connect(self.fastForward)
        self.ui.action_finish.triggered.connect(self.finish)
        self.ui.action_release.triggered.connect(self.release)
        self.ui.action_options.triggered.connect(self.options)
        self.ui.action_manual.triggered.connect(self.manual)
        self.ui.action_feedback.triggered.connect(self.feedback)
        self.ui.action_about.triggered.connect(self.about)

    def generateNotation(self):
        """
        按3种格式生成棋谱文本
        :param format=1:每行输出一步
        eg. 1.炮二平五
        　　　 馬8进7
        　　 2.馬二进三
        　　　　卒7进1
        :param format=2:每行输出一回合
        eg. 1.炮二平五 馬8进7
            2.馬二进三 卒7进1
        :param format=3:仅输出一行
        eg.1.炮二平五 馬8进7;2.馬二进三 卒7进1
        """
        text = "[赛事：%s]\n[轮次：%s]\n[日期：%s]\n[地点：%s]\n[红方队伍：%s]\n[红方选手：%s]\n[黑方队伍：%s]\n[黑方选手：%s]\n" \
               "[结果：%s]\n[ECCO: %s]\n[开局：%s]\n着法列表\n" % \
               (self.tag[0], self.tag[1], self.tag[2], self.tag[3], self.tag[4], self.tag[5], self.tag[6], self.tag[7],
                self.tag[8], self.tag[9], self.tag[10])
        if len(self.ui.textBrowser.toPlainText()) > 7:
            if self.format == 1:
                text += self.ui.textBrowser.toPlainText()[7:]
            elif self.format == 2:
                for i in range(1, len(self.Manual) + 1):
                    if i % 2 == 1:
                        text += "%d.%s" % (i // 2 + 1, self.Manual[i - 1])
                    else:
                        text += "  %s\n" % self.Manual[i - 1]
            elif self.format == 3:
                for i in range(1, len(self.Manual) + 1):
                    if i % 2 == 1:
                        text += "%d.%s" % (i // 2 + 1, self.Manual[i - 1])
                    else:
                        text += " %s;" % self.Manual[i - 1]
        text += "\n\n===========================\nmade by 中国象棋自动打谱工具"
        return text

    def generateBoard(self):
        """
        生成当前棋局，红方棋子以（）标记，黑方棋子以［］标记
        """
        character = ('　', '將', '車', '馬', '象', '士', '砲', '卒', '帥', '車', '馬', '相', '仕', '炮', '兵')
        text = ""
        if self.tag[5] != "" and self.tag[7] != "":
            text += "　　　　　　　 %s (对) %s\n" % (self.tag[5], self.tag[7])
        if self.tag[10] != "":
            text += "　　　　　　　 " + self.tag[10]
        if self.tag[9] != "":
            text += self.tag[9] + "\n"
        text += "\n"
        for i in range(10):
            for j in range(9):
                if self.board[i][j] == "*":
                    text += "　　　"
                elif self.board[i][j].isupper():
                    text += "（%s）" % character[self.chessB.index(self.board[i][j])]
                else:
                    text += "［%s］" % character[self.chessB.index(self.board[i][j])]
            text += "\n"
        text += "\n===================================\nmade by 中国象棋自动打谱工具"
        return text

    def generateLog(self, rounds, videoDuration, programDuration, result=0):
        """
        生成系统日志，内容包括日期时间、检测源及其类型、棋谱标签、回合数、图片数量/视频时长、系统运行时长
        :param rounds: 回合数
        :param videoDuration: 视频时长
        :param programDuration: 运行时长
        :param result: 检测结果，0代表成功，1代表失败，默认为0
        """
        text = "检测结束时间：%s\n" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if self.type == 1:
            text += "文件名："
            for i in self.files:
                text += os.path.basename(i) + " "
            text += "\n检测源类型：图片"
        elif self.type == 2:
            text += "文件名：%s\n检测源类型：视频" % os.path.basename(self.video_name)
        else:
            text += "检测源类型：摄像头"
        if result == 0:
            text += "\n[赛事：%s][轮次：%s][日期：%s][地点：%s]\n[红方队伍：%s][红方选手：%s]\n[黑方队伍：%s][黑方选手：%s]\n"\
                    "[结果：%s][ECCO: %s][开局：%s]\n" % (self.tag[0], self.tag[1], self.tag[2], self.tag[3], self.tag[4],
                    self.tag[5], self.tag[6], self.tag[7], self.tag[8], self.tag[9], self.tag[10])
            text += "已检测回合数：%d\n" % rounds
            if self.type == 1:
                text += "图片数量：%d" % len(self.files)
            else:
                text += "视频时长：%d秒" % videoDuration
            text += "\n系统运行时长：%d秒\n\n" % programDuration
        elif result == 1:
            text += "检测失败，检测源中可能不包含棋盘图像\n\n"
        with open(self.logPath + "/syslog.txt", "a") as f:
            f.write(text)
        f.close()

    def init_process(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.ChineseNum = ("", "九", "八", "七", "六", "五", "四", "三", "二", "一")
        self.chess = ('No', 'KinB', 'ChaB', 'HorB', 'Ele', 'ManB', 'CanB', 'PawB', 'KinR', 'ChaR', 'HorR', 'PM', 'ManR',
                      'CanR', 'PawR')  # 用于标记的文本
        self.chessB = ('*', 'k', 'c', 'h', 'e', 'm', 'a', 'p', 'K', 'C', 'H', 'E', 'M', 'A', 'P')  # 棋子记号，黑方为小写，红方为大写
        self.sampleLoc = [0, (5, 1), (1, 1), (2, 1), (3, 1), (4, 1), (2, 3), (3, 4), (5, 10), (1, 10), (2, 10), (3, 10),
                          (4, 10), (2, 8), (3, 7), (7, 4), (7, 7), (9, 1), (8, 1), (7, 1), (6, 1), (8, 3), (9, 10),
                          (8, 10), (7, 10), (6, 10), (8, 8)]
        self.board = [['c', 'h', 'e', 'm', 'k', 'm', 'e', 'h', 'c', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', 'a', '*', '*', '*', '*', '*', 'a', '*', '*', '*'],
                      ['p', '*', 'p', '*', 'p', '*', 'p', '*', 'p', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                      ['P', '*', 'P', '*', 'P', '*', 'P', '*', 'P', '*', '*'],
                      ['*', 'A', '*', '*', '*', '*', '*', 'A', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                      ['C', 'H', 'E', 'M', 'K', 'M', 'E', 'H', 'C', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.std = 700  # 视频/图像长、宽中的最大值
        self.pieceNum = 32
        self.PM_pos = [(1, 8), (3, 6), (3, 10), (5, 8), (7, 6), (7, 10), (9, 8)]
        self.ele_pos = [(1, 3), (3, 1), (3, 5), (5, 3), (7, 1), (7, 5), (9, 3)]
        self.ManB_pos = [(4, 1), (6, 1), (4, 3), (6, 3), (5, 2)]
        self.ManR_pos = [(4, 10), (6, 10), (4, 8), (6, 8), (5, 9)]
        self.board_new = copy.deepcopy(self.board)
        self.Manual = []  # 棋谱
        self.threshold = [0, 0]  # 红黑棋子r值的临界值
        self.topLeft, self.bottomRight, self.bottomLeft, self.topRight = (9999, 9999), (0, 0), (0, 0), (0, 0)
        # 棋盘左上、右下、左下、右上角的坐标
        self.tempR = []  # 用于存放红方棋子R值的临时列表
        self.tempB = []  # 用于存放黑方棋子R值的临时列表
        self.circles_adjusted = []  # 用于存放调整后的坐标的临时列表
        self.R = 20
        self.ui.pushButton_start.setDisabled(False)
        self.ui.action_detect.setDisabled(False)

    def img_resize(self, image):
        width, height = len(image[0]), len(image)
        if height >= width:
            width = int(width / (height / self.std))
            height = self.std
        else:
            height = int(height / (width / self.std))
            width = self.std
        return cv2.resize(image, dsize=(width, height), interpolation=cv2.INTER_AREA)

    def imshow(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        QtImg = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_ARGB32)
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(QtImg))
        self.ui.label.setScaledContents(True)  # 设置图像自适应界面大小

    def process(self, imgSource):
        """
        图像定位与识别的主函数，以黑箱处置。图像处理后会在主界面的视频区域中显示。
        :param imgSource: 待识别的图片
        """
        def rotate_img(image, angle):
            h, w = image.shape[:2]
            rotate_center = (w / 2, h / 2)
            # 获取旋转矩阵
            # 参数1为旋转中心点;
            # 参数2为旋转角度,正值-逆时针旋转;负值-顺时针旋转
            # 参数3为各向同性的比例因子,1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
            M = cv2.getRotationMatrix2D(rotate_center, angle, 1.0)
            # 计算图像新边界
            new_w = int(h * np.abs(M[0, 1]) + w * np.abs(M[0, 0]))
            new_h = int(h * np.abs(M[0, 0]) + w * np.abs(M[0, 1]))
            # 调整旋转矩阵以考虑平移
            M[0, 2] += (new_w - w) / 2
            M[1, 2] += (new_h - h) / 2
            return cv2.warpAffine(image, M, (new_w, new_h))

        def getLocation(coord, aR, tl, br, bl, tr):
            if abs(coord[1] - tl[1]) < abs(coord[1] - br[1]):
                px = int(np.round((coord[0] - tl[0]) / (aR[0] * 2), 0)) + 1 if coord[0] > tl[0] else 1
            else:
                px = int(np.round((coord[0] - bl[0]) / (aR[1] * 2), 0)) + 1 if coord[0] > bl[0] else 1
            if abs(coord[0] - tl[0]) < abs(coord[0] - br[0]):
                py = int(np.round((coord[1] - tl[1]) / (aR[2] * 2), 0)) + 1 if coord[1] > tl[1] else 1
            else:
                py = int(np.round((coord[1] - tr[1]) / (aR[3] * 2), 0)) + 1 if coord[1] > tr[1] else 1
            return px, py

        imgSource = self.img_resize(imgSource)
        lab = cv2.cvtColor(imgSource, cv2.COLOR_BGR2LAB)
        L, A, B = cv2.split(lab)  # 原图的LAB值
        ori_b, g, ori_r = cv2.split(imgSource)  # 原图的RGB值
        r0 = cv2.equalizeHist(ori_r)  # 直方图均衡可提高图像对比度
        g = cv2.equalizeHist(g)
        # 图像二值化
        thresh = 20
        temp, binary = cv2.threshold(g, thresh, 255, cv2.THRESH_BINARY)
        # 检测棋盘是否受到遮挡
        thresh2 = np.average(ori_r) - 70
        temp2, labels = cv2.threshold(B, thresh2, 255, cv2.THRESH_BINARY)
        labels = np.ones((len(imgSource), len(imgSource[0]))) * 255 - labels
        labels = measure.label(labels, connectivity=1)
        areaList = [prop.area for prop in measure.regionprops(labels)]
        connected = max(areaList) if areaList else 0
        if self.frame_count != 0:
            if connected / self.connectedRef > 1.2:
                self.imshow(imgSource)
                return
        fil = cv2.medianBlur(imgSource, 7)  # 中值滤波，滤波核为7时霍夫圆检测的准确率较高
        gaussian = cv2.GaussianBlur(fil, (7, 7), 0)  # 再通过高斯滤波降噪
        Canny = cv2.Canny(gaussian, 30, 30)
        # 输入图像，方法（类型），dp(dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推)，最短距离-可以分辨是两个圆否 则认为是同心圆 ,
        # 边缘检测时使用Canny算子的高阈值，中心点累加器阈值—候选圆心（霍夫空间内累加和大于该阈值的点就对应于圆心），检测到圆的最小半径，检测到圆的的最大半径
        circles = cv2.HoughCircles(Canny, cv2.HOUGH_GRADIENT, 1, 60, param1=self.para1, param2=self.para2,
                                   minRadius=self.houghmin, maxRadius=self.houghmax)
        if not circles is None:  # 检测到了圆
            if self.frame_count != 0 and len(circles[0]) == self.pieceNum:  # 若所有棋子位置均无变动，则跳过该帧
                for i in circles[0]:
                    posX, posY = getLocation(i, self.actualR, self.topLeft, self.bottomRight, self.bottomLeft,
                                             self.topRight)
                    if self.board[posY - 1][posX - 1] == "*":
                        break
                else:
                    self.imshow(imgSource)
                    return
            direction = [[] for _ in range(15)]
            flagCha, flagHor, flagEle, flagManB, flagPM, flagManR, flagCan, flagPawB, flagPawR = 0, 0, 0, 0, 0, 0, 0, \
                                                                                                 0, 0
            for circle in circles[0]:  # 遍历每一个圆
                x, y, r = int(circle[0]), int(circle[1]), self.R
                if x < r or y < r:
                    continue
                ori_r = np.where(binary == 0, ori_r, 0)  # 根据二值化图像筛选掉空白部分
                chessR = ori_r[y - r:y + r, x - r:x + r]
                exist = (chessR != 0)
                if exist.sum() == 0:
                    continue
                characterR = chessR.sum() / exist.sum()
                # 重新对棋子进行定位
                centreX, centreY = int(np.median(np.where(chessR != 0)[1])), int(np.median(np.where(chessR != 0)[0]))
                x, y = x + centreX - r, y + centreY - r
                if x < r or y < r:
                    continue
                if self.frame_count == 0:  # 确定棋盘的4个角
                    if x + y < sum(self.topLeft):
                        self.topLeft = (x, y)
                    if x + y > sum(self.bottomRight):
                        self.bottomRight = (x, y)
                    if y - x > self.bottomLeft[1] - self.bottomLeft[0]:
                        self.bottomLeft = (x, y)
                    if x - y > self.topRight[0] - self.topRight[1]:
                        self.topRight = (x, y)
                cv2.circle(imgSource, (x, y), r, (0, 255, 0), 2)  # 标记检测到的棋子位置

                if self.frame_count != 0:
                    posX, posY = getLocation((x, y), self.actualR, self.topLeft, self.bottomRight, self.bottomLeft,
                                             self.topRight)
                    disB, disR = abs(characterR - self.threshold[0]), abs(characterR - self.threshold[1])
                    # disB, disR分别表示棋子颜色与黑、红棋子平均r值的差距
                    if self.Manual:
                        if self.Manual[-1][1].isdigit() and disR < disB:  # 根据棋谱选择当前帧检测的棋子颜色
                            imgID, conf = self.red.predict(r0[y - r:y + r, x - r:x + r])  # 对检测到的红方棋子灰度图进行分类
                            imgID = imgID + 7 if imgID <= 7 else imgID
                        elif not self.Manual[-1][1].isdigit() and disB < disR:
                            imgID, conf = self.black.predict(r0[y - r:y + r, x - r:x + r])  # 对检测到的黑方棋子灰度图进行分类
                            imgID = imgID - 7 if imgID > 7 else imgID
                        else:
                            continue
                    elif disR < disB:
                        imgID, conf = self.red.predict(r0[y - r:y + r, x - r:x + r])
                        imgID = imgID + 7 if imgID <= 7 else imgID
                    else:
                        continue
                    if self.chessB[imgID] != self.board[posY - 1][posX - 1] and self.board[posY - 1][posX - 1] != "*":
                        if imgID <= 7 and self.chessB.index(self.board[posY - 1][posX - 1]) <= 7 or imgID > 7 and \
                                self.chessB.index(self.board[posY - 1][posX - 1]) > 7:  # 若检测到同色棋子互吃，则结束本次检测
                            cv2.putText(imgSource, "Wrong", (x - 20, y), self.font, 0.5, (255, 0, 0), 1)  # 标记棋子ID
                            continue
                    imgMark = self.chess[imgID] if conf < 200 else "Unknown"
                    cv2.putText(imgSource, imgMark, (x - 20, y), self.font, 0.5, (255, 0, 0), 1)  # 标记棋子ID
                    if conf >= 200:
                        continue
                    mes, checked = "", False
                    # ———————————————————————————————————————————着法计算——————————————————————————————————————————— #
                    if imgID == 1 or imgID == 8:  # 將或帥
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if self.board[posY - 2][posX - 1] == self.chessB[imgID]:
                                mes = "將%d进1" % posX if imgID == 1 else "帥%s退一" % self.ChineseNum[posX]
                                self.board_new[posY - 2][posX - 1] = '*'  # 注意board记录的是矩阵的切片，即实际坐标-1
                            elif self.board[posY][posX - 1] == self.chessB[imgID]:
                                mes = "將%d退1" % posX if imgID == 1 else "帥%s进一" % self.ChineseNum[posX]
                                self.board_new[posY][posX - 1] = '*'
                            elif self.board[posY - 1][posX - 2] == self.chessB[imgID]:
                                mes = "將%d平%d" % (posX - 1, posX) if imgID == 1 else "帥%s平%s" % (
                                    self.ChineseNum[posX - 1], self.ChineseNum[posX])
                                self.board_new[posY - 1][posX - 2] = '*'
                            elif self.board[posY - 1][posX] == self.chessB[imgID]:
                                mes = "將%d平%d" % (posX + 1, posX) if imgID == 1 else "帥%s平%s" % (
                                    self.ChineseNum[posX + 1], self.ChineseNum[posX])
                                self.board_new[posY - 1][posX] = '*'
                    elif imgID == 2 or imgID == 9:  # 車
                        temp = [x[posX - 1] for x in self.board]
                        temp1, temp2 = temp.count(self.chessB[imgID]), self.board[posY - 1].count(self.chessB[imgID])
                        if temp1 + temp2 >= 2:  # 该車所在行列上一帧有2个車时需要检验
                            flagCha = 1
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagCha == 1 and not direction[imgID]:
                                flagCha = 2
                            else:
                                checked = True
                        elif flagCha == 2:
                            direction[imgID].append((posY - 1, posX - 1))
                            posY, posX = direction[imgID].pop(0)
                            posY, posX = posY + 1, posX + 1
                            checked = True
                        if checked:
                            for i in range(10):
                                if self.board[i][posX - 1] == self.chessB[imgID] and (i, posX - 1) not in \
                                        direction[imgID]:
                                    if posY > i + 1:
                                        for j in range(i + 1, posY - 1):
                                            if self.board[j][posX - 1] != "*":
                                                checked = False
                                                break
                                        if checked:
                                            mes = "車%d进%d" % (posX, posY - (i + 1)) if imgID == 2 else "車%s退%s" % \
                                                (self.ChineseNum[posX], self.ChineseNum[-(posY - (i + 1))])
                                            self.board_new[i][posX - 1] = '*'
                                            break
                                    elif posY < i + 1:
                                        for j in range(posY, i):
                                            if self.board[j][posX - 1] != "*":
                                                checked = False
                                                break
                                        if checked:
                                            mes = "車%d退%d" % (posX, i + 1 - posY) if imgID == 2 else "車%s进%s" % \
                                                    (self.ChineseNum[posX], self.ChineseNum[-(i + 1 - posY)])
                                            self.board_new[i][posX - 1] = '*'
                                            break
                                elif self.board[posY - 1][i] == self.chessB[imgID] and (posY - 1, i) not in \
                                        direction[imgID]:
                                    mes = "車%d平%d" % (i + 1, posX) if imgID == 2 else "車%s平%s" % (
                                        self.ChineseNum[i + 1], self.ChineseNum[posX])
                                    self.board_new[posY - 1][i] = '*'
                                    break
                    elif imgID == 3 or imgID == 10:  # 馬
                        if flagHor == 0:
                            temp = 0
                            if self.board[posY - 3][posX - 2] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 3][posX] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 2][posX - 3] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 2][posX + 1] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY + 1][posX - 2] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY + 1][posX] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY][posX - 3] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY][posX + 1] == self.chessB[imgID]:
                                temp += 1
                            if temp > 1:
                                flagHor = 1
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagHor == 1 and not direction[imgID]:
                                flagHor = 2
                            else:
                                checked = True
                        elif flagHor == 2:
                            direction[imgID].append((posY - 1, posX - 1))
                            posY, posX = direction[imgID].pop(0)
                            posY, posX = posY + 1, posX + 1
                            checked = True
                        if checked:
                            if self.board[posY - 3][posX - 2] == self.chessB[imgID] and (posY - 3, posX - 2) not in \
                                    direction[imgID]:
                                if self.board[posY - 2][posX - 2] != "*":  # 蹩马腿时不可移动，该情况通常是假圆
                                    continue
                                mes = "馬%d进%d" % (posX - 1, posX) if imgID == 3 else "馬%s退%s" % (
                                    self.ChineseNum[posX - 1], self.ChineseNum[posX])
                                self.board_new[posY - 3][posX - 2] = '*'
                            elif self.board[posY - 3][posX] == self.chessB[imgID] and (posY - 3, posX) not in \
                                    direction[imgID]:
                                if self.board[posY - 2][posX] != "*":
                                    continue
                                mes = "馬%d进%d" % (posX + 1, posX) if imgID == 3 else "馬%s退%s" % (
                                    self.ChineseNum[posX + 1], self.ChineseNum[posX])
                                self.board_new[posY - 3][posX] = '*'
                            elif self.board[posY - 2][posX - 3] == self.chessB[imgID] and (posY - 2, posX - 3) not in \
                                    direction[imgID]:
                                if self.board[posY - 2][posX - 2] != "*":
                                    continue
                                mes = "馬%d进%d" % (posX - 2, posX) if imgID == 3 else "馬%s退%s" % (
                                    self.ChineseNum[posX - 2], self.ChineseNum[posX])
                                self.board_new[posY - 2][posX - 3] = '*'
                            elif self.board[posY - 2][posX + 1] == self.chessB[imgID] and (posY - 2, posX + 1) not in \
                                    direction[imgID]:
                                if self.board[posY - 2][posX] != "*":
                                    continue
                                mes = "馬%d进%d" % (posX + 2, posX) if imgID == 3 else "馬%s退%s" % (
                                    self.ChineseNum[posX + 2], self.ChineseNum[posX])
                                self.board_new[posY - 2][posX + 1] = '*'
                            elif self.board[posY + 1][posX - 2] == self.chessB[imgID] and (posY + 1, posX - 2) not in \
                                    direction[imgID]:
                                if self.board[posY][posX - 2] != "*":
                                    continue
                                mes = "馬%d退%d" % (posX - 1, posX) if imgID == 3 else "馬%s进%s" % (
                                    self.ChineseNum[posX - 1], self.ChineseNum[posX])
                                self.board_new[posY + 1][posX - 2] = '*'
                            elif self.board[posY + 1][posX] == self.chessB[imgID] and (posY + 1, posX) not in \
                                    direction[imgID]:
                                if self.board[posY][posX] != "*":
                                    continue
                                mes = "馬%d退%d" % (posX + 1, posX) if imgID == 3 else "馬%s进%s" % (
                                    self.ChineseNum[posX + 1], self.ChineseNum[posX])
                                self.board_new[posY + 1][posX] = '*'
                            elif self.board[posY][posX - 3] == self.chessB[imgID] and (posY, posX - 3) not in \
                                    direction[imgID]:
                                if self.board[posY][posX - 2] != "*":
                                    continue
                                mes = "馬%d退%d" % (posX - 2, posX) if imgID == 3 else "馬%s进%s" % (
                                    self.ChineseNum[posX - 2], self.ChineseNum[posX])
                                self.board_new[posY][posX - 3] = '*'
                            elif self.board[posY][posX + 1] == self.chessB[imgID] and (posY, posX + 1) not in \
                                    direction[imgID]:
                                if self.board[posY][posX] != "*":
                                    continue
                                mes = "馬%d退%d" % (posX + 2, posX) if imgID == 3 else "馬%s进%s" % (
                                    self.ChineseNum[posX + 2], self.ChineseNum[posX])
                                self.board_new[posY][posX + 1] = '*'
                    elif imgID == 4:  # 象
                        if (posX, posY) not in self.ele_pos:  # 若象不在其行动范围内，则结束检测
                            continue
                        if flagEle == 0:
                            if self.board[0][2] == self.board[0][6] == self.chessB[imgID] or self.board[4][2] == \
                                    self.board[4][6] == self.chessB[imgID] or self.board[0][2] == self.board[4][2] == \
                                    self.chessB[imgID] or self.board[0][6] == self.board[4][6] == self.chessB[imgID] or \
                                    self.board[2][0] == self.board[2][4] == self.chessB[imgID] or self.board[2][4] == \
                                    self.board[2][8] == self.chessB[imgID]:
                                flagEle = 1
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagEle == 1 and not direction[imgID]:
                                flagEle = 2
                            else:
                                checked = True
                        elif flagEle == 2:
                            direction[imgID].append((posY - 1, posX - 1))
                            posY, posX = direction[imgID].pop(0)
                            posY, posX = posY + 1, posX + 1
                            checked = True
                        if checked:
                            if posX == 1 or posX == 5 or posX == 9:
                                if self.board[0][2] == self.chessB[imgID] and (0, 2) not in direction[imgID]:
                                    if posX == 1 and self.board[1][1] != "*" or posX == 5 and self.board[1][3] != "*":
                                        # 别象脚时不可移动，该情况通常是假圆
                                        continue
                                    mes = "象3进%d" % posX
                                    self.board_new[0][2] = '*'
                                elif self.board[0][6] == self.chessB[imgID] and (0, 6) not in direction[imgID]:
                                    if posX == 9 and self.board[1][7] != "*" or posX == 5 and self.board[1][5] != "*":
                                        continue
                                    mes = "象7进%d" % posX
                                    self.board_new[0][6] = '*'
                                elif self.board[4][2] == self.chessB[imgID] and (4, 2) not in direction[imgID]:
                                    if posX == 1 and self.board[3][1] != "*" or posX == 5 and self.board[3][3] != "*":
                                        continue
                                    mes = "象3退%d" % posX
                                    self.board_new[4][2] = '*'
                                elif self.board[4][6] == self.chessB[imgID] and (4, 6) not in direction[imgID]:
                                    if posX == 9 and self.board[3][7] != "*" or posX == 5 and self.board[3][5] != "*":
                                        continue
                                    mes = "象7退%d" % posX
                                    self.board_new[4][6] = '*'
                                else:
                                    print("程序出错！")
                            elif posX == 3 or posX == 7:
                                if self.board[2][0] == self.chessB[imgID] and (2, 0) not in direction[imgID]:
                                    if posY == 5 and self.board[3][1] != "*" or posY == 1 and self.board[1][1] != "*":
                                        continue
                                    mes = "象1进3" if posY == 5 else "象1退3"
                                    self.board_new[2][0] = '*'
                                elif self.board[2][4] == self.chessB[imgID] and (2, 4) not in direction[imgID]:
                                    if posY == 5:
                                        if posX == 3 and self.board[3][3] != "*" or posX == 7 and self.board[3][5] != "*":
                                            continue
                                        mes = "象5进%d" % posX
                                    else:
                                        if posX == 3 and self.board[1][3] != "*" or posX == 7 and self.board[1][5] != "*":
                                            continue
                                        mes = "象5退%d" % posX
                                    self.board_new[2][4] = '*'
                                elif self.board[2][8] == self.chessB[imgID] and (2, 8) not in direction[imgID]:
                                    if posY == 5 and self.board[3][7] != "*" or posY == 1 and self.board[1][7] != "*":
                                        continue
                                    mes = "象9进7" if posY == 5 else "象9退7"
                                    self.board_new[2][8] = '*'
                                else:
                                    print("程序出错！")
                    elif imgID == 11:  # 相
                        if (posX, posY) not in self.PM_pos:  # 若相不在其行动范围内，则结束检测
                            continue
                        if flagPM == 0:
                            if self.board[9][2] == self.board[9][6] == self.chessB[imgID] or self.board[5][2] == \
                                    self.board[5][6] == self.chessB[imgID] or self.board[9][2] == self.board[5][2] == \
                                    self.chessB[imgID] or self.board[9][6] == self.board[5][6] == self.chessB[imgID] or \
                                    self.board[7][0] == self.board[7][4] == self.chessB[imgID] or self.board[7][4] == \
                                    self.board[7][8] == self.chessB[imgID]:
                                flagPM = 1
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagPM == 1 and not direction[imgID]:
                                flagPM = 2
                            else:
                                checked = True
                        elif flagPM == 2:
                            direction[imgID].append((posY - 1, posX - 1))
                            posY, posX = direction[imgID].pop(0)
                            posY, posX = posY + 1, posX + 1
                            checked = True
                        if checked:
                            if posX == 1 or posX == 5 or posX == 9:
                                if self.board[9][2] == self.chessB[imgID] and (9, 2) not in direction[imgID]:
                                    if posX == 1 and self.board[8][1] != "*" or posX == 5 and self.board[8][3] != "*":
                                        # 别相脚时不可移动，该情况通常是假圆
                                        continue
                                    mes = "相七进%s" % self.ChineseNum[posX]
                                    self.board_new[9][2] = '*'
                                elif self.board[9][6] == self.chessB[imgID] and (9, 6) not in direction[imgID]:
                                    if posX == 9 and self.board[8][7] != "*" or posX == 5 and self.board[8][5] != "*":
                                        continue
                                    mes = "相三进%s" % self.ChineseNum[posX]
                                    self.board_new[9][6] = '*'
                                elif self.board[5][2] == self.chessB[imgID] and (5, 2) not in direction[imgID]:
                                    if posX == 1 and self.board[6][1] != "*" or posX == 5 and self.board[6][3] != "*":
                                        continue
                                    mes = "相七退%s" % self.ChineseNum[posX]
                                    self.board_new[5][2] = '*'
                                elif self.board[5][6] == self.chessB[imgID] and (5, 6) not in direction[imgID]:
                                    if posX == 9 and self.board[6][7] != "*" or posX == 5 and self.board[6][5] != "*":
                                        continue
                                    mes = "相三退%s" % self.ChineseNum[posX]
                                    self.board_new[5][6] = '*'
                                else:
                                    print("程序出错！")
                            elif posX == 3 or posX == 7:
                                if self.board[7][0] == self.chessB[imgID] and (7, 0) not in direction[imgID]:
                                    if posY == 6 and self.board[6][1] != "*" or posY == 10 and self.board[8][1] != "*":
                                        continue
                                    mes = "相九进七" if posY == 6 else "相九退七"
                                    self.board_new[7][0] = '*'
                                elif self.board[7][4] == self.chessB[imgID] and (7, 4) not in direction[imgID]:
                                    if posY == 6:
                                        if posX == 3 and self.board[6][3] != "*" or posX == 7 and self.board[6][5] != "*":
                                            continue
                                        mes = "相五进%s" % self.ChineseNum[posX]
                                    else:
                                        if posX == 3 and self.board[8][3] != "*" or posX == 7 and self.board[8][5] != "*":
                                            continue
                                        mes = "相五退%s" % self.ChineseNum[posX]
                                    self.board_new[7][4] = '*'
                                elif self.board[7][8] == self.chessB[imgID] and (7, 8) not in direction[imgID]:
                                    if posY == 5 and self.board[6][7] != "*" or posY == 1 and self.board[8][7] != "*":
                                        continue
                                    mes = "相一进三" if posY == 6 else "相一退三"
                                    self.board_new[7][8] = '*'
                                else:
                                    print("程序出错！")
                    elif imgID == 5:  # 士
                        if (posX, posY) not in self.ManB_pos:  # 若士不在其行动范围内，则结束检测
                            continue
                        if (posX == 4 or posX == 6) and self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            mes = "士5退%d" % posX if posY == 1 else "士5进%d" % posX
                            self.board_new[1][4] = '*'
                        else:
                            if flagManB == 0:
                                temp = 0
                                if self.board[0][3] == self.chessB[imgID]:
                                    temp += 1
                                if self.board[0][5] == self.chessB[imgID]:
                                    temp += 1
                                if self.board[2][3] == self.chessB[imgID]:
                                    temp += 1
                                if self.board[2][5] == self.chessB[imgID]:
                                    temp += 1
                                if temp > 1:
                                    flagManB = 1
                            if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                                if flagManB == 1 and not direction[imgID]:
                                    flagManB = 2
                                else:
                                    checked = True
                            elif flagManB == 2:
                                direction[imgID].append((posY - 1, posX - 1))
                                posY, posX = direction[imgID].pop(0)
                                posY, posX = posY + 1, posX + 1
                                checked = True
                            if checked:
                                if self.board[0][3] == self.chessB[imgID] and (0, 3) not in direction[imgID]:
                                    mes = "士4进5"
                                    self.board_new[0][3] = '*'
                                elif self.board[0][5] == self.chessB[imgID] and (0, 5) not in direction[imgID]:
                                    mes = "士6进5"
                                    self.board_new[0][5] = '*'
                                elif self.board[2][3] == self.chessB[imgID] and (2, 3) not in direction[imgID]:
                                    mes = "士4退5"
                                    self.board_new[2][3] = '*'
                                elif self.board[2][5] == self.chessB[imgID] and (2, 5) not in direction[imgID]:
                                    mes = "士6退5"
                                    self.board_new[2][5] = '*'
                    elif imgID == 12:  # 仕
                        if (posX, posY) not in self.ManR_pos:  # 若仕不在其行动范围内，则结束检测
                            continue
                        if (posX == 4 or posX == 6) and self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            mes = "仕五退%s" % self.ChineseNum[posX] if posY == 10 else "仕五进%s" % self.ChineseNum[posX]
                            self.board_new[8][4] = '*'
                        else:
                            if flagManR == 0:
                                temp = 0
                                if self.board[9][3] == self.chessB[imgID]:
                                    temp += 1
                                if self.board[9][5] == self.chessB[imgID]:
                                    temp += 1
                                if self.board[7][3] == self.chessB[imgID]:
                                    temp += 1
                                if self.board[7][5] == self.chessB[imgID]:
                                    temp += 1
                                if temp > 1:
                                    flagManR = 1
                            if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                                if flagManR == 1 and not direction[imgID]:
                                    flagManR = 2
                                else:
                                    checked = True
                            elif flagManR == 2:
                                direction[imgID].append((posY - 1, posX - 1))
                                posY, posX = direction[imgID].pop(0)
                                posY, posX = posY + 1, posX + 1
                                checked = True
                            if checked:
                                if self.board[9][3] == self.chessB[imgID] and (9, 3) not in direction[imgID]:
                                    mes = "仕六进五"
                                    self.board_new[9][3] = '*'
                                elif self.board[9][5] == self.chessB[imgID] and (9, 5) not in direction[imgID]:
                                    mes = "仕四进五"
                                    self.board_new[9][5] = '*'
                                elif self.board[7][3] == self.chessB[imgID] and (7, 3) not in direction[imgID]:
                                    mes = "仕六退五"
                                    self.board_new[7][3] = '*'
                                elif self.board[7][5] == self.chessB[imgID] and (7, 5) not in direction[imgID]:
                                    mes = "仕四退五"
                                    self.board_new[7][5] = '*'
                    elif imgID == 6 or imgID == 13:  # 炮或砲
                        if flagCan == 0:
                            temp = [x[posX - 1] for x in self.board]
                            temp1, temp2 = temp.count(self.chessB[imgID]), self.board[posY - 1].count(self.chessB[imgID])
                            if temp1 + temp2 >= 2:  # 该炮/砲所在行列上一帧有两个炮/砲时需要检验
                                flagCan = 1
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagCan == 1 and not direction[imgID]:
                                flagCan = 2
                            else:
                                checked = True
                        elif flagCan == 2:
                            direction[imgID].append((posY - 1, posX - 1))
                            posY, posX = direction[imgID].pop(0)
                            posY, posX = posY + 1, posX + 1
                            checked = True
                        if checked:
                            for i in range(10):
                                if self.board[i][posX - 1] == self.chessB[imgID] and (i, posX - 1) not in \
                                        direction[imgID]:
                                    if posY > i + 1:
                                        mes = "砲%d进%d" % (posX, posY - (i + 1)) if imgID == 6 else \
                                            "炮%s退%s" % (self.ChineseNum[posX], self.ChineseNum[-(posY - (i + 1))])
                                    elif posY < i + 1:
                                        mes = "砲%d退%d" % (posX, i + 1 - posY) if imgID == 6 else \
                                            "炮%s进%s" % (self.ChineseNum[posX], self.ChineseNum[-(i + 1 - posY)])
                                    self.board_new[i][posX - 1] = '*'
                                    break
                                elif self.board[posY - 1][i] == self.chessB[imgID] and (posY - 1, i) not in \
                                        direction[imgID]:
                                    mes = "砲%d平%d" % (i + 1, posX) if imgID == 6 else "炮%s平%s" % (
                                        self.ChineseNum[i + 1], self.ChineseNum[posX])
                                    self.board_new[posY - 1][i] = '*'
                                    break
                    elif imgID == 7:  # 卒
                        temp = 0
                        if flagPawB == 0:
                            if self.board[posY - 2][posX - 1] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 1][posX - 2] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 1][posX] == self.chessB[imgID]:
                                temp += 1
                            flagPawB = temp - 1  # 当原棋盘该坐标周围有2个兵时flag=1，有3个兵时flag=2
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagPawB >= 1 and len(direction[imgID]) < flagPawB:
                                flagPawB += 1
                                pawB_pos = (posX, posY)
                            else:
                                checked = True
                        elif flagPawB == temp and flagPawB > 0:
                            direction[imgID].append((posY - 1, posX - 1))
                            posX, posY = pawB_pos
                            checked = True
                        if checked:
                            if self.board[posY - 2][posX - 1] == self.chessB[imgID] and (posY - 2, posX - 1) \
                                    not in direction[imgID]:
                                mes = "卒%d进1" % posX
                                self.board_new[posY - 2][posX - 1] = '*'
                            elif posY > 5 and self.board[posY - 1][posX - 2] == self.chessB[imgID] and (
                                    posY - 1, posX - 2) not in direction[imgID]:
                                mes = "卒%d平%d" % (posX - 1, posX)
                                self.board_new[posY - 1][posX - 2] = '*'
                            elif posY > 5 and self.board[posY - 1][posX] == self.chessB[imgID] and (
                                    posY - 1, posX) not in direction[imgID]:
                                mes = "卒%d平%d" % (posX + 1, posX)
                                self.board_new[posY - 1][posX] = '*'
                    elif imgID == 14:  # 兵
                        temp = 0
                        if flagPawR == 0:
                            if self.board[posY - 2][posX - 1] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 1][posX - 2] == self.chessB[imgID]:
                                temp += 1
                            if self.board[posY - 1][posX] == self.chessB[imgID]:
                                temp += 1
                            flagPawR = temp - 1  # 当原棋盘该坐标周围有2个兵时flag=1，有3个兵时flag=2
                        if self.chessB[imgID] != self.board[posY - 1][posX - 1]:
                            if flagPawR >= 1 and len(direction[imgID]) < flagPawR:
                                flagPawR += 1
                                pawR_pos = (posX, posY)
                            else:
                                checked = True
                        elif flagPawR == temp and flagPawR > 0:
                            direction[imgID].append((posY - 1, posX - 1))
                            posX, posY = pawR_pos
                            checked = True
                        if checked:
                            if self.board[posY][posX - 1] == self.chessB[imgID] and (posY, posX - 1) not in \
                                    direction[imgID]:
                                mes = "兵%s进一" % self.ChineseNum[posX]
                                self.board_new[posY][posX - 1] = '*'
                            elif posY <= 5 and self.board[posY - 1][posX - 2] == self.chessB[imgID] and (
                                    posY - 1, posX - 2) not in direction[imgID]:
                                mes = "兵%s平%s" % (self.ChineseNum[posX - 1], self.ChineseNum[posX])
                                self.board_new[posY - 1][posX - 2] = '*'
                            elif posY <= 5 and self.board[posY - 1][posX] == self.chessB[imgID] and (
                                    posY - 1, posX) not in direction[imgID]:
                                mes = "兵%s平%s" % (self.ChineseNum[posX + 1], self.ChineseNum[posX])
                                self.board_new[posY - 1][posX] = '*'
                    if mes != "":
                        self.Manual.append(mes)
                        self.board_new[posY - 1][posX - 1] = self.chessB[imgID]
                        if mes[-1].isdigit():
                            if len(self.Manual) <= 18:
                                self.ui.textBrowser.append("  " + mes)
                            else:
                                self.ui.textBrowser.append("   " + mes)
                        else:
                            self.ui.textBrowser.append("%d.%s" % (len(self.Manual) // 2 + 1, mes))
                        break
                    direction[imgID].append((posY - 1, posX - 1))
                else:
                    if y < len(imgSource) / 2:  # 计算棋子的平均R值，以判断红黑方
                        self.tempB.append(characterR)
                    else:
                        self.tempR.append(characterR)
                    self.circles_adjusted.append((x, y))
        self.pieceNum = len(circles[0])  # 记录棋盘上的棋子个数
        # 在界面上显示处理后的图像
        self.imshow(imgSource)

        if self.frame_count == 0:
            self.connectedRef = connected
            self.R = int((self.bottomRight[0] - self.topLeft[0]) / (16 / self.radiousRate))  # 棋子的内圈半径，用于识别图像
            self.actualR = [(self.topRight[0] - self.topLeft[0]) / 16, (self.bottomRight[0] - self.bottomLeft[0]) / 16,
                            (self.bottomLeft[1] - self.topLeft[1]) / 18, (self.bottomRight[1] - self.topRight[1]) / 18]
            # 棋子的外圈半径，4个元素分别为上、下、左、右的半径
            self.threshold[0], self.threshold[1] = np.average(self.tempB), np.average(self.tempR)

            imagesR, labelsR, imagesB, labelsB = [], [], [], []
            for i in self.circles_adjusted:
                posX, posY = getLocation(i, self.actualR, self.topLeft, self.bottomRight, self.bottomLeft, self.topRight)
                if (posX, posY) in self.sampleLoc:
                    R2 = self.R + 10
                    y1, y2 = i[1] - R2 if i[1] >= R2 else 0, i[1] + R2 if i[1] + R2 <= len(imgSource) else len(imgSource)
                    x1, x2 = i[0] - R2 if i[0] >= R2 else 0, i[0] + R2 if i[0] + R2 <= len(imgSource[0]) else \
                        len(imgSource[0])
                    img1 = r0[int(y1):int(y2), int(x1):int(x2)]
                    for j in range(0, 360, 30):
                        rotated_img = rotate_img(img1, j)
                        if posY <= 5:
                            imagesB.append(np.array(rotated_img[int(len(rotated_img) / 2) - self.R: int(len(rotated_img)
                                           / 2) + self.R, int(len(rotated_img) / 2) - self.R: int(len(rotated_img) / 2)
                                                                                              + self.R]))
                            labelsB.append(self.chessB.index(self.board[posY - 1][posX - 1]))  # 根据棋子位置获取黑棋图像标签
                        else:
                            imagesR.append(np.array(rotated_img[int(len(rotated_img) / 2) - self.R: int(len(rotated_img)
                                           / 2) + self.R, int(len(rotated_img) / 2) - self.R: int(len(rotated_img) / 2)
                                                                                              + self.R]))
                            labelsR.append(self.chessB.index(self.board[posY - 1][posX - 1]))  # 根据棋子位置获取红棋图像标签
            self.red = cv2.face.LBPHFaceRecognizer_create()
            self.red.train(imagesR, np.array(labelsR))  # 进行训练
            self.black = cv2.face.LBPHFaceRecognizer_create()
            self.black.train(imagesB, np.array(labelsB))
        else:
            self.board = copy.deepcopy(self.board_new)

    def getImage(self):
        try:
            self.files, filetype = QFileDialog.getOpenFileNames(self, "请选择图片文件", "data/images",
                                                                "*.jpg;;*.png;;*.bmp;;All Files(*)")
        except OSError as reason:
            print('文件打开出错啦！核对路径是否正确' + str(reason))
        if len(self.files) <= 1:
            if len(self.files) == 1:
                QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"请选择2个及以上的图片文件！")
            return
        if self.timer_video.isActive():  # 能获取图片但计时器被打开，说明打开了摄像头
            self.timer_video.stop()
            self.ui.pushButton_camera.setText("打开摄像头")
        self.ui.pushButton_save.setDisabled(True)
        self.ui.action_saveAs.setDisabled(True)
        self.ui.action_release.setDisabled(True)
        self.ui.filePath.setText("")
        self.ui.textBrowser.setText("＝＝开始＝＝")
        self.init_process()
        img = self.img_resize(cv2.imdecode(np.fromfile(self.files[0], dtype=np.uint8), cv2.IMREAD_COLOR))
        self.imshow(img)
        self.type = 1
        self.ui.progressBar.setValue(0)
        self.ui.nowTime.setText("1")
        self.ui.totalTime.setText(str(len(self.files)))

    def getVideo(self):
        self.video_name, _ = QFileDialog.getOpenFileName(self, "打开视频", "data/",
                                                    "*.mp4;;*.avi;;*.wmv;;*.mov;;*.mkv;;*.flv;;All Files(*)")
        if self.video_name == "":
            return
        flag = self.cap.open(self.video_name)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"打开视频失败")
        else:
            if self.timer_video.isActive():
                self.timer_video.stop()
                self.ui.pushButton_camera.setText("打开摄像头")
            self.ui.pushButton_save.setDisabled(True)
            self.ui.action_saveAs.setDisabled(True)
            self.ui.action_release.setDisabled(True)
            self.ui.filePath.setText(self.video_name)
            self.ui.textBrowser.setText("＝＝开始＝＝")
            self.init_process()  # 初始化
            self.cap.open(self.video_name)
            ret, img = self.cap.read()
            self.imshow(self.img_resize(img))
            self.type = 2
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)  # 读取视频的帧速率
            self.frame_num = self.cap.get(7)
            self.duration = self.frame_num / self.fps
            self.ui.totalTime.setText("%02d:%02d:%02d" % (self.duration // 3600, self.duration // 60,
                                                          int(self.duration % 60)))

    def openCamera(self):
        if self.type == 3:
            if self.cameraFlag:
                if self.MessageBox("中国象棋自动打谱工具", "关闭摄像头将结束检测，您确定要关闭吗？") == "是":
                    self.finish()
            else:
                self.ui.pushButton_camera.setText("打开摄像头")
                self.ui.textBrowser.clear()
                self.cap.release()
                self.ui.label.clear()
                self.timer_video.stop()
                self.type = 0
        else:
            self.ui.pushButton_save.setDisabled(True)
            self.ui.action_save.setDisabled(True)
            self.ui.action_release.setDisabled(True)
            self.ui.pushButton_camera.setText("关闭摄像头")
            self.ui.filePath.setText("")
            self.ui.textBrowser.setText("＝＝开始＝＝")
            self.init_process()  # 初始化
            self.cap.open(0)
            self.type = 3
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)  # 读取视频的帧速率
            self.timer_video.start(int(round(1000 / self.fps, 0)))

    def startDetect(self):
        if self.type == 1:  # 图片
            self.ui.pushButton_video.setDisabled(True)
            self.ui.pushButton_img.setDisabled(True)
            self.ui.pushButton_camera.setDisabled(True)
            self.ui.action_video.setDisabled(True)
            self.ui.action_image.setDisabled(True)
            self.ui.action_camera.setDisabled(True)
            self.ui.pushButton_start.setDisabled(True)
            self.ui.action_detect.setDisabled(True)
            self.ui.pushButton_save.setDisabled(False)
            self.ui.action_saveAs.setDisabled(False)
            self.ui.action_release.setDisabled(False)
            self.ui.progressBar.setMaximum(len(self.files))
            self.frame_count = -1
            self.start_time = time.time()
            for file in self.files:
                self.frame_count = self.frame_count + 1
                self.pendingImg = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_COLOR)
                self.ui.nowTime.setText(str(self.frame_count + 1))
                self.ui.progressBar.setValue(self.frame_count + 1)
                try:
                    self.process(self.pendingImg)
                except:
                    self.imshow(self.img_resize(self.pendingImg))
                    QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"检测失败，请检查上传的图片是否为棋盘图片！")
                    self.ui.label.clear()
                    self.generateLog(0, 0, 0, 1)  # res参数赋为1时代表检测失败
                    break
            else:
                rounds = int(len(self.Manual) / 2) if len(self.Manual) % 2 == 0 else int(len(self.Manual) / 2) + 1
                self.generateLog(rounds, 0, time.time() - self.start_time)
            self.ui.pushButton_video.setDisabled(False)
            self.ui.pushButton_img.setDisabled(False)
            self.ui.pushButton_camera.setDisabled(False)
            self.ui.action_video.setDisabled(False)
            self.ui.action_image.setDisabled(False)
            self.ui.action_camera.setDisabled(False)
            return
        elif self.type == 2:  # 视频
            self.skip_num = np.round(self.detectGap * self.fps, 0)  # 每隔多少帧截取一张图像
            self.frame_count = -1
            self.timer_video.start(int(round(1000 / self.fps, 0)))
            self.ui.progressBar.setDisabled(False)
            self.ui.pushButton_skip.setDisabled(False)
            self.ui.action_skip.setDisabled(False)
            self.ui.progressBar.setMaximum(int(np.round(self.duration, 0)))
        elif self.type == 3:  # 摄像头
            self.skip_num = np.round(self.detectGap * self.fps, 0)  # 每隔多少帧截取一张图像
            self.frame_count = -1
            self.cameraFlag = True
        # 开始识别时，关闭检测源按键点击功能，打开操作区按键点击功能
        self.ui.pushButton_video.setDisabled(True)
        self.ui.pushButton_img.setDisabled(True)
        self.ui.pushButton_camera.setDisabled(True)
        self.ui.action_video.setDisabled(True)
        self.ui.action_image.setDisabled(True)
        self.ui.action_camera.setDisabled(True)
        self.ui.pushButton_start.setDisabled(True)
        self.ui.pushButton_stop.setDisabled(False)
        self.ui.pushButton_finish.setDisabled(False)
        self.ui.action_detect.setDisabled(False)
        self.ui.action_stop.setDisabled(False)
        self.ui.action_finish.setDisabled(False)
        self.ui.pushButton_save.setDisabled(False)
        self.ui.action_saveAs.setDisabled(False)
        self.ui.action_release.setDisabled(False)
        self.ui.pushButton_stop.setText(u'暂停检测')
        self.start_time = time.time()

    def openFrame(self):
        if self.type == 3 and not self.cameraFlag:
            ret, img = self.cap.read()
            self.imshow(self.img_resize(img))
            return
        if self.skip:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count + self.fps * self.skipTime)
            self.frame_count += self.fps * self.skipTime
            self.skip = False
        else:
            if self.frame_count != -1 and self.type == 2:  # 只有视频且非第一帧的情况下方可进行跳帧检测
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count + self.skip_num)
                self.frame_count += self.skip_num
            else:
                self.frame_count += 1
        nowTime = (self.frame_count + 1) / self.fps
        self.ui.nowTime.setText("%02d:%02d:%02d" % (nowTime // 3600, nowTime // 60, int(nowTime % 60)))
        if self.type == 2:
            self.ui.progressBar.setValue(int(np.round(nowTime, 0)))
        elif self.type == 3:
            self.ui.totalTime.setText("%02d:%02d:%02d" % (nowTime // 3600, nowTime // 60, int(nowTime % 60)))
        ret, self.pendingImg = self.cap.read()
        if ret:
            try:
                self.process(self.pendingImg)
            except:
                QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"检测失败，请检查视频中是否包含棋盘图像！")
                self.generateLog(0, 0, 0, 1)
                self.finish(1)
        else:
            self.cap.release()
            self.timer_video.stop()  # 停止计时器
            self.ui.pushButton_video.setDisabled(False)
            self.ui.pushButton_img.setDisabled(False)
            self.ui.pushButton_camera.setDisabled(False)
            self.ui.action_video.setDisabled(False)
            self.ui.action_image.setDisabled(False)
            self.ui.action_camera.setDisabled(False)
            self.ui.pushButton_skip.setDisabled(True)
            self.ui.pushButton_stop.setDisabled(True)
            self.ui.pushButton_finish.setDisabled(True)
            self.ui.action_detect.setDisabled(True)
            self.ui.action_stop.setDisabled(True)
            self.ui.action_finish.setDisabled(True)
            self.frame_count = 0
            self.ui.progressBar.setValue(0)
            self.ui.nowTime.setText("00:00:00")
            self.ui.totalTime.setText("00:00:00")
            self.cameraFlag = False
            self.ui.filePath.clear()
            rounds = int(len(self.Manual) / 2) if len(self.Manual) % 2 == 0 else int(len(self.Manual) / 2) + 1
            duarion = np.round(self.frame_num / self.fps) if self.type == 2 else time.time() - self.start_time
            self.generateLog(rounds, duarion, time.time() - self.start_time)

    def stop(self):  # 暂停/继续检测，仅针对视频和摄像头
        # 暂停检测
        # 若QTimer已经触发，且激活
        if self.timer_video.isActive() and self.stopFlag % 2 == 1:
            self.ui.pushButton_stop.setText(u'继续检测')  # 当前状态为暂停状态
            self.stopFlag = self.stopFlag + 1  # 调整标记信号为偶数
            self.timer_video.blockSignals(True)
            self.ui.pushButton_skip.setDisabled(True)
            self.ui.action_skip.setDisabled(True)
        # 继续检测
        else:
            self.stopFlag = self.stopFlag - 1
            self.ui.pushButton_stop.setText(u'暂停检测')
            self.timer_video.blockSignals(False)
            if self.type == 2:
                self.ui.pushButton_skip.setDisabled(False)
                self.ui.action_skip.setDisabled(False)

    def fastForward(self):  # 快进，仅针对视频
        self.skip = True

    def finish(self, flag=0):  # 结束检测，仅针对视频和摄像头，flag代表是否生成系统日志，默认输出
        self.cap.release()  # 释放video_capture资源
        self.ui.label.clear()  # 清空label画布
        self.timer_video.stop()  # 停止计时器
        # 启动其他检测按键功能
        self.ui.pushButton_video.setDisabled(False)
        self.ui.pushButton_img.setDisabled(False)
        self.ui.pushButton_camera.setDisabled(False)
        self.ui.action_video.setDisabled(False)
        self.ui.action_image.setDisabled(False)
        self.ui.action_camera.setDisabled(False)
        self.ui.pushButton_skip.setDisabled(True)
        self.ui.pushButton_stop.setDisabled(True)
        self.ui.pushButton_finish.setDisabled(True)
        self.ui.action_skip.setDisabled(True)
        self.ui.action_stop.setDisabled(True)
        self.ui.action_finish.setDisabled(True)
        self.frame_count = 0
        self.type = 0
        self.ui.progressBar.setValue(0)
        self.ui.nowTime.setText("00:00:00")
        self.ui.totalTime.setText("00:00:00")
        self.cameraFlag = False
        self.ui.filePath.clear()
        self.ui.pushButton_camera.setText("打开摄像头")
        # 结束检测时，将暂停功能恢复至初始状态。若处于暂停状态，需要调整stopFlag并关闭计时器的阻塞信号
        self.ui.pushButton_stop.setText(u'暂停/继续')
        if self.stopFlag % 2 == 0:
            self.stopFlag = self.stopFlag + 1
            self.timer_video.blockSignals(False)
        rounds = int(len(self.Manual) / 2) if len(self.Manual) % 2 == 0 else int(len(self.Manual) / 2) + 1
        duarion = np.round(self.frame_num / self.fps) if self.type == 2 else time.time() - self.start_time
        if not flag:
            self.generateLog(rounds, duarion, time.time() - self.start_time)

    def save(self):
        if not self.Manual:
            QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"目前尚未有着法记录，请您耐心等候程序运行。")
            return
        if self.timer_video.isActive():
            if self.MessageBox("中国象棋自动打谱工具", "目前识别尚未结束，您确定要保存棋谱吗？保存棋谱不会影响程序运行。") == "否":
                return
        fileName, filetype = QFileDialog.getSaveFileName(self, "请选择保存路径", self.savePath,
                                                         "Text Files (*.txt);;All Files (*)")
        if fileName != "":
            try:
                with open(fileName, "w") as f:
                    f.write(self.generateNotation())
                f.close()
            except:
                QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"保存失败，请检查路径是否正确！")

    # 以下为菜单操作
    def viewNotation(self):
        self.ViewNotation = win_ViewNotation()
        self.ViewNotation.show()
        self.signal_str.connect(self.ViewNotation.get_data_notation)
        self.signal_str.emit(self.generateNotation())

    def editTag(self):
        self.EditTag = win_EditTag()
        self.EditTag.show()
        self.signal_list.connect(self.EditTag.get_data_notation)
        self.signal_list.emit(self.tag)
        self.EditTag.signal_notation.connect(self.getData_notation)

    def viewLog(self):
        try:
            os.startfile(self.logPath + "/syslog.txt")
        except:
            QtWidgets.QMessageBox.warning(self, u"中国象棋自动打谱工具", u"打开失败，系统日志不存在！")

    def quit(self):
        if self.MessageBox("退出", "您确定要退出程序吗？") == "是":
            sys.exit(app.exec_())

    def release(self):
        self.ReleaseNotation = win_ReleaseNotation()
        self.ReleaseNotation.show()
        self.signal_int.connect(self.ReleaseNotation.get_data_resize)
        self.signal_int.emit(self.std)
        self.signal_list2.connect(self.ReleaseNotation.get_data)
        self.signal_list2.emit([self.generateNotation(), self.generateBoard()])
        self.signal_img.connect(self.ReleaseNotation.get_data_image)
        self.signal_img.emit(self.pendingImg)

    def options(self):
        self.Options = win_Options()
        self.Options.show()
        self.signal_opt.connect(self.Options.get_data)
        self.signal_opt.emit(self.skipTime, self.detectGap, self.format, self.savePath, self.houghmin, self.houghmax,
                             self.para1, self.para2, self.radiousRate)
        self.Options.signal_options.connect(self.getData_options)

    def manual(self):
        self.win_Manual = win_Manual()
        self.win_Manual.show()

    def feedback(self):
        self.Feedback = win_Feedback()
        self.Feedback.show()

    def about(self):
        self.about = win_About()
        self.about.show()

    def getData_notation(self, ls):
        self.tag = ls

    def getData_options(self, data1, data2, data3, data4, data5, data6, data7, data8, data9):
        self.skipTime, self.detectGap, self.format, self.savePath, self.houghmin = data1, data2, data3, data4, data5
        self.houghmax, self.para1, self.para2, self.radiousRate = data6, data7, data8, data9

    def closeEvent(self, event):  # 函数名固定不可变
        if self.MessageBox("退出", "您确定要退出程序吗？") == "是":
            sys.exit(app.exec_())
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load("./qm/widgets_zh_CN_all.qm")
    app.installTranslator(translator)
    Main = win_Main()
    Main.show()
    sys.exit(app.exec_())
