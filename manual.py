from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Manual(object):
    def setupUi(self, Manual):
        Manual.setObjectName("Manual")
        Manual.resize(1341, 845)
        Manual.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/用户手册.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Manual.setWindowIcon(icon)
        self.treeWidget = QtWidgets.QTreeWidget(Manual)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 191, 845))
        self.treeWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.textBrowser = QtWidgets.QTextBrowser(Manual)
        self.textBrowser.setGeometry(QtCore.QRect(219, 20, 1115, 823))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Manual)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 0, 1151, 845))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.raise_()
        self.treeWidget.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Manual)
        QtCore.QMetaObject.connectSlotsByName(Manual)

    def retranslateUi(self, Manual):
        _translate = QtCore.QCoreApplication.translate
        Manual.setWindowTitle(_translate("Manual", "用户手册"))
        self.treeWidget.headerItem().setText(0, _translate("Manual", "导航"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Manual", "用户手册"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Manual", "系统概述"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Manual", "项目背景"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Manual", "项目目标"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("Manual", "工作原理"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("Manual", "系统整体介绍"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Manual", "打谱相关功能说明"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Manual", "选择检测源"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Manual", "修改圆检测参数"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Manual", "打谱"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("Manual", "定位"))
        self.treeWidget.topLevelItem(2).child(4).setText(0, _translate("Manual", "结束检测"))
        self.treeWidget.topLevelItem(2).child(5).setText(0, _translate("Manual", "保存棋谱"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("Manual", "辅助功能说明"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("Manual", "查看棋谱文本"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("Manual", "编辑棋谱标签"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("Manual", "查看系统日志"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("Manual", "发布棋谱"))
        self.treeWidget.topLevelItem(3).child(4).setText(0, _translate("Manual", "设置"))
        self.treeWidget.topLevelItem(3).child(5).setText(0, _translate("Manual", "意见反馈"))
        self.treeWidget.topLevelItem(3).child(6).setText(0, _translate("Manual", "关于"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("Manual", "快捷键一览"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("Manual",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"756\" cellspacing=\"0\" cellpadding=\"0\">\n"
                                            "<tr>\n"
                                            "<td width=\"98\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
                                            "<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/logo.png\" width=\"83\" height=\"82\" style=\"vertical-align: top;\" /> </p></td>\n"
                                            "<td width=\"658\" style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
                                            "<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:36pt; font-weight:600;\">中国象棋自动打谱系统</span> </p></td></tr></table>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/user's manual.png\" width=\"1088\" height=\"613\" /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本号：V1.0</p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">制作人：戴林鑫 </p></body></html>"))


class win_Manual(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(win_Manual, self).__init__(parent)
        self.ui = Ui_Manual()
        self.ui.setupUi(self)
        self.init_slots()

    def init_slots(self):
        self.ui.treeWidget.clicked.connect(self.onClicked)

    def onClicked(self, index):
        if self.ui.treeWidget.currentItem().text(0) == "用户手册":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: "
                "pre-wrap; }\n</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; "
                "font-style:normal;\">\n<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                "0px; margin-right:0px;\" width=\"756\" cellspacing=\"0\" cellpadding=\"0\">\n<tr>\n<td width=\"98\" "
                "style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n<p "
                "style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                "text-indent:0px;\"><img src=\"images/logo.png\" width=\"83\" height=\"82\" style=\"vertical-align: top"
                ";\" /> </p></td>\n<td width=\"658\" style=\" padding-left:0; padding-right:0; padding-top:0; "
                "padding-bottom:0;\">\n<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:"
                "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:36pt; "
                "font-weight:600;\">中国象棋自动打谱系统</span> </p></td></tr></table>\n<p style=\" margin-top:12px; "
                "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                "<img src=\"images/user's manual.png\" width=\"1088\" height=\"613\" /></p>\n<p style=\"-qt-paragraph-"
                "type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                "; text-indent:0px;\"><br /></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; "
                "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本号：V1.0</p>\n<p align=\""
                "center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-"
                "indent:0; text-indent:0px;\">制作人：戴林鑫 </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "项目背景":
            self.ui.textBrowser.setText(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">项目背景</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　中国象棋拥有悠久的历史，因为其丰富的竞技、益智与娱乐属性，在国内拥有庞大的用户基础。而棋谱是前人象棋智慧的结晶，通过对棋谱的研究与总结，可以丰富棋手的布局体系，提升象棋攻杀能力，进而提升自身棋艺。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　古人打谱自然只能通过手写的方式记录，而今人打谱则大多依靠计算机中的象棋软件进行记录。在大型象棋比赛中一般有</span><span style=\" font-family:\'Times New Roman,serif\';\">3</span><span style=\" font-family:\'宋体\';\">种打谱方式：第一种是由棋手记录棋谱，即每下一步棋便记录其着法，这种打谱方式效率低下，且仅适用于慢棋时间较充裕的阶段，但由于成本低廉且准确率高，因此该方法仍为许多高水平赛事使用；第二种是由裁判根据比赛情况实时在计算机中打谱，这种打谱方式可以消除对棋手的影响，却增加了裁判员的执裁压力，但由于裁判可以通过录像回放的方式进行准确判断，因此该方法在大型赛事中使用最为广泛；第三种是借助可以自动感应棋子空间位置的智能棋盘，将棋盘上的行棋数据通过串行通讯传给</span><span style=\" font-family:\'Times New Roman,serif\';\">PC</span><span style=\" font-family:\'宋体\';\">机，这种方式极大地分担了裁判员的执裁任务，但较高的成本使其只能运用于少数比赛中。对于小型比赛或私人对弈，则只能在对弈后凭记忆在象棋软件中进行复盘。目前亟需一种兼具自动程度高、成本低廉、使用方便特点的打谱方式。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "项目目标":
            self.ui.textBrowser.setText(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">项目目标</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　针对以上现状，本项目拟研究一种基于计算机视觉的象棋自动打谱方法，通过棋局图像采集与预处理，自动判别对弈双方每一步的着法，最终输出完整的棋谱，并基于此理念开发出一个功能完善的自动打谱系统，以期应用于各类象棋赛事和私人对弈中，实现对现有的棋谱记录方式的变革。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "工作原理":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">工作原理</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　大部分的中国象棋甲级赛事中，主办方都会在棋盘上方放置摄像头以对比赛进行直播录像。本文研发的自动打谱系统可通过调用摄像头实时处理棋局图像，只需将摄像头信号传入计算机中即可实现自动打谱。在私人对弈时，也可用手机替代工业摄像头，实现低成本的自动打谱。标准的自动打谱系统结构示意如图</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">所示。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/structural representation.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 1</span><span style=\" font-family:\'宋体\';\"> 象棋自动打谱系统结构示意</span> </p>\n"
                "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　系统调用摄像头后，根据需求逐帧或隔帧采集棋盘图像信息，并通过对图像中的棋子进行定位与识别，获取棋子的位置与种类信息，将该棋子的位置信息与上一帧进行比较，若检测到棋子位置发生变动，则停止对其他棋子的检测并生成这一步的着法。由于系统对图像的采集和识别是动态进行的，因此对算法的效率具有更高要求。系统工作的整体流程图如图</span><span style=\" font-family:\'Times New Roman,serif\';\">2</span><span style=\" font-family:\'宋体\';\">所示。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/flow chart.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 2</span><span style=\" font-family:\'宋体\';\"> 系统工作整体流程图</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "系统整体介绍":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">系统整体介绍</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　如图</span><span style=\" font-family:\'Times New Roman,serif\';\">3</span><span style=\" font-family:\'宋体\';\">所示，本系统可分为检测源区、主操作界面区、导航菜单区</span><span style=\" font-family:\'Times New Roman,serif\';\">3</span><span style=\" font-family:\'宋体\';\">个区域。检测源区用于打开检测源，包括视频、图片和摄像头；主操作界面区是本系统的核心功能区，用于展示检测图像和着法列表，以及在检测过程中的操作；导航菜单区是系统所有功能的菜单入口，点击相应功能菜单即可打开相应的功能界面。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/main interface.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 3</span><span style=\" font-family:\'宋体\';\"> 系统主界面分区</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "选择检测源":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">选择检测源</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　本系统可将视频、图片或摄像头作为打谱的检测对象，因此在检测源区域设有“打开视频”、“打开图片”、“打开摄像头”三个按钮。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\';\">　　Ø</span><span style=\" font-size:7pt;\">  </span><span style=\" font-family:\'宋体\';\">打开视频：弹出文件选择器（单选），在文件选择器中可以浏览</span><span style=\" font-family:\'Times New Roman,serif\';\">mp4, avi</span><span style=\" font-family:\'宋体\';\">文件类型以及所有类型的文件。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\';\">　　Ø</span><span style=\" font-size:7pt;\">  </span><span style=\" font-family:\'宋体\';\">打开图片：弹出文件选择器（多选），在文件选择器中可以浏览</span><span style=\" font-family:\'Times New Roman,serif\';\">mp4, avi, wmv, mov, mkv, flv</span><span style=\" font-family:\'宋体\';\">文件类型以及所有类型的文件。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\';\">　　Ø</span><span style=\" font-size:7pt;\">  </span><span style=\" font-family:\'宋体\';\">打开摄像头：从摄像头获取视频流。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　除了主操作界面区外，用户还可通过菜单区的</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">文件</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">打开</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">视频</span><span style=\" font-family:\'Times New Roman,serif\';\">…]/[</span><span style=\" font-family:\'宋体\';\">图片</span><span style=\" font-family:\'Times New Roman,serif\';\">…]/[</span><span style=\" font-family:\'宋体\';\">摄像头</span><span style=\" font-family:\'Times New Roman,serif\';\">…]</span><span style=\" font-family:\'宋体\';\">选择并打开检测源。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　注意：通过文件选择器选取的图片必须在</span><span style=\" font-family:\'Times New Roman,serif\';\">2</span><span style=\" font-family:\'宋体\';\">张及以上，否则系统会报错并停止输入图片。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "修改圆检测参数":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">修改圆检测参数</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　为提高系统识别的准确度和健壮性，用户可自行修改Hough圆检测的参数，可修改的参数包括检测到的圆的最小半径和最大半径、Carny边缘检测的最大阈值、圆心的累加器阈值、识别半径与棋子实际半径的比例，详见设置界面。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "打谱":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">打谱</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　选择检测源后，在主操作界面区或菜单区的</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">操作</span><span style=\" font-family:\'Times New Roman,serif\';\">]</span><span style=\" font-family:\'宋体\';\">栏中点击“开始检测”按钮即可开始图像识别与打谱，识别所得结果会实时在着法列表中显示，若检测源为视频或图片，可通过进度条查看文件读取的进度（见图</span><span style=\" font-family:\'Times New Roman,serif\';\">4</span><span style=\" font-family:\'宋体\';\">）。此时，系统会自动关闭检测源区的三个按钮，并开启“暂停检测”“快进”“结束检测”“保存棋谱”的功能。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/notation process1.png\"/><img src=\"images/notation process2.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 4</span><span style=\" font-family:\'宋体\';\"> 打谱过程演示</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">注意：</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　（</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">）开始检测后，若输入的视频或图像被系统判定为非棋盘图像，系统会报错并结束检测；</span></p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">　　<span style=\" font-family:\'宋体\';\">（</span><span style=\" font-family:\'Times New Roman,serif\';\">2</span><span style=\" font-family:\'宋体\';\">）若检测源为图片或摄像头则不会开启“快进”功能。</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "定位":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">定位</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　定位功能分为暂停、继续与快进，其按钮可在主操作界面区和菜单区的[操作]中找到。暂停、继续功能通过同一按钮实现，检测状态下，该按钮显示“暂停检测”，暂停状态下，该按钮则会显示“继续检测”。快进功能可使视频跳跃到数秒后的位置，跳跃幅度可在设置中进行调整，初始赋值为10秒。为避免着法顺序混乱，本系统设定无法通过拖动进度条实现视频/图像定位，也无法进行快退。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　注意：快进可能会导致漏检着法，因此应谨慎使用快进功能或将快进幅度调整为合理区间。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "结束检测":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">结束检测</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　通过“结束检测”按钮可以中止对当前检测源的打谱操作。结束后棋谱不会消失，棋谱会保存至下一次检测源被打开。结束检测后，系统会自动关闭“暂停/继续检测”“快进”“结束检测”功能。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　注意：按下“结束检测”后，系统不会弹出询问窗口，因此用户结束检测前需谨慎考虑。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "保存棋谱":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">保存棋谱</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　通过“保存棋谱”按钮可将着法列表中的着法保存至本地。本系统提供3种棋谱格式用以保存与查看，分别为一行一步、一行两步以及仅输出一行，详见设置界面。若在生成第一步着法前点击“保存棋谱”，系统会出现提示并停止保存操作，若在视频/图像读取完毕前点击“保存棋谱”，系统会询问是否保存，选择“是”方能执行保存操作。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "查看棋谱文本":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">查看棋谱文本</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　查看棋谱文本功能可从菜单栏的</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">文件</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">查看棋谱文本</span><span style=\" font-family:\'Times New Roman,serif\';\">]</span><span style=\" font-family:\'宋体\';\">进入。棋谱文本不同于着法列表所展示的棋谱，其为保存棋谱时输出的最终样式，包含以下几个部分（见表</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">）。不同棋谱格式下的棋谱文本界面如图</span><span style=\" font-family:\'Times New Roman,serif\';\">5</span><span style=\" font-family:\'宋体\';\">所示，其格式从左到右依次为一行一步、一行两步、仅输出一行。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">表</span><span style=\" font-family:\'Times New Roman,serif\';\"> 1</span><span style=\" font-family:\'宋体\';\"> 输出棋谱文本内容</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/tags.png\"/></p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/notation1.png\"/><img src=\"images/notation2.png\"/></p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 5</span><span style=\" font-family:\'宋体\';\"> 查看棋谱文本界面</span> </p>\n"
                "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　在该界面中，可以通过“复制”按钮将棋谱文本复制到电脑剪贴板，方便用户在检测结束前获取棋谱。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "编辑棋谱标签":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">编辑标签</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　标签是棋谱的重要组成部分，是棋谱得以分类和流传的关键要素。本系统可以通过菜单栏中的</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">文件</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">编辑标签</span><span style=\" font-family:\'Times New Roman,serif\';\">…]</span><span style=\" font-family:\'宋体\';\">实现对标签的编辑，其界面如图</span><span style=\" font-family:\'Times New Roman,serif\';\">6</span><span style=\" font-family:\'宋体\';\">所示。完成对标签的更改后，棋谱文本中的标签信息也会同步更新（见图</span><span style=\" font-family:\'Times New Roman,serif\';\">7</span><span style=\" font-family:\'宋体\';\">）。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/tags edit.png\"/><img src=\"images/notation4.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 6</span><span style=\" font-family:\'宋体\';\">　编辑标签界面</span> 　　　 　　　　 　　　　　<span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 7</span><span style=\" font-family:\'宋体\';\"> 更新后的棋谱文本</span> </p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　注意：保存标签时，系统会对标签的格式进行检查，格式要求包括选手的姓名中不得出现数字、</span><span style=\" font-family:\'Times New Roman,serif\';\">ECCO</span><span style=\" font-family:\'宋体\';\">必须为一位字母＋两位数字、开局为纯中文。若不满足以上任何一项要求，系统会报错并停止保存操作。各项标签可以不输入任何字符。</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "查看系统日志":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">查看系统日志</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">    当系统结束检测时，无论检测结果如何，系统都会将检测结果记录到日志中。若检测成功（包括手动结束和完整检测），输出的内容包括检测结束的日期时间、检测源及其类型、棋谱标签、回合数、图片数量</span><span style=\" font-family:\'Times New Roman,serif\';\">/</span><span style=\" font-family:\'宋体\';\">视频时长、系统运行时长；若检测失败（即系统判别为非棋盘图像），则只会输出日期时间、检测源及其类型（见图</span><span style=\" font-family:\'Times New Roman,serif\';\">8</span><span style=\" font-family:\'宋体\';\">）。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">    本系统支持在系统内打开系统日志文件</span><span style=\" font-family:\'Times New Roman,serif\';\">(.txt)</span><span style=\" font-family:\'宋体\';\">，打开方式为在菜单栏中选择</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">文件</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">查看系统日志</span><span style=\" font-family:\'Times New Roman,serif\';\">]</span><span style=\" font-family:\'宋体\';\">。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/syslog.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 8</span><span style=\" font-family:\'宋体\';\"> 系统日志示例</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "发布棋谱":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">发布棋谱</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　发布棋谱功能可从菜单栏的</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">操作</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">发布棋谱</span><span style=\" font-family:\'Times New Roman,serif\';\">/</span><span style=\" font-family:\'宋体\';\">图片</span><span style=\" font-family:\'Times New Roman,serif\';\">…]</span><span style=\" font-family:\'宋体\';\">进入。该功能包含两个子功能，分别为另存为当前图像和发布棋谱或当前局面，其界面如图</span><span style=\" font-family:\'Times New Roman,serif\';\">9</span><span style=\" font-family:\'宋体\';\">所示。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/release.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 9</span><span style=\" font-family:\'宋体\';\"> 发布棋谱界面</span> </p>\n"
                "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　用户另存为的图像可选择以原图、调整后大小（主界面的视频区域大小）或自定义大小输出，点击“浏览”按钮可以选择另存为的地址。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　该系统允许用户以文本形式复制棋谱和当前局面，供用户选择的发布站点包括百度知道、百度贴吧象棋吧、知乎、新浪微博、</span><span style=\" font-family:\'Times New Roman,serif\';\">QQ</span><span style=\" font-family:\'宋体\';\">空间。点击“发布”后，系统会根据用户的选择复制棋谱或当前局面，并打开发布站点的</span><span style=\" font-family:\'Times New Roman,serif\';\">URL</span><span style=\" font-family:\'宋体\';\">，若用户在发布站点中选择了“其他”，则只复制棋谱或当前局面而不打开网页。</span></p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">　　 <span style=\" font-family:\'宋体\';\">注意：图片自定义的宽度、高度大小范围为</span><span style=\" font-family:\'Times New Roman,serif\';\">1~10000</span><span style=\" font-family:\'宋体\';\">，若超出该范围系统会报错且中止另存为操作。</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "设置":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">设置</span> </p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　设置的功能从</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">选项</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">设置</span><span style=\" font-family:\'Times New Roman,serif\';\">…]</span><span style=\" font-family:\'宋体\';\">进入，分为基础设置和圆检测设置两部分，其界面如图</span><span style=\" font-family:\'Times New Roman,serif\';\">10</span><span style=\" font-family:\'宋体\';\">所示。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/options.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 10</span><span style=\" font-family:\'宋体\';\"> 设置界面</span> </p>\n"
                "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　基础设置包含快进幅度、检测间隔、棋谱保存格式、默认保存路径</span><span style=\" font-family:\'Times New Roman,serif\';\">4</span><span style=\" font-family:\'宋体\';\">部分。快进幅度指每点一次“快进”视频向前跳跃的幅度，此值不宜过大，建议设在</span><span style=\" font-family:\'Times New Roman,serif\';\">10</span><span style=\" font-family:\'宋体\';\">以下。检测间隔指每隔多少秒检测一次，此值不宜过大，建议设在</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">以下，设为</span><span style=\" font-family:\'Times New Roman,serif\';\">0</span><span style=\" font-family:\'宋体\';\">则对每一帧进行检测。棋谱保存格式分为</span><span style=\" font-family:\'Times New Roman,serif\';\">3</span><span style=\" font-family:\'宋体\';\">种，第一种为每行输出一步，其示例如图</span><span style=\" font-family:\'Times New Roman,serif\';\">10</span><span style=\" font-family:\'宋体\';\">中的棋谱示例文本框所示；第二种为每行输出一回合，其示例如图</span><span style=\" font-family:\'Times New Roman,serif\';\">11</span><span style=\" font-family:\'宋体\';\">（左）所示；第三种为仅输出一行，其示例如图</span><span style=\" font-family:\'Times New Roman,serif\';\">11</span><span style=\" font-family:\'宋体\';\">（右）所示，系统默认的保存格式为每行输出一回合。默认保存路径是指保存棋谱时弹出的文件选择器的初始路径，若路径为空，则默认保存路径为系统文件所在文件夹。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/format1.png\"/><img src=\"images/format2.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 11</span><span style=\" font-family:\'宋体\';\"> 棋谱保存格式示例</span> </p>\n"
                "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　圆检测设置包括最小圆半径、最大圆半径、</span><span style=\" font-family:\'Times New Roman,serif\';\">Canny</span><span style=\" font-family:\'宋体\';\">边缘检测的最大阈值、圆心的累加器阈值和识别半径与棋子实际半径的比例。前</span><span style=\" font-family:\'Times New Roman,serif\';\">4</span><span style=\" font-family:\'宋体\';\">个参数分别对应</span><span style=\" font-family:\'Times New Roman,serif\';\">OpenCV</span><span style=\" font-family:\'宋体\';\">库</span><span style=\" font-family:\'Times New Roman,serif\';\">HoughCircles</span><span style=\" font-family:\'宋体\';\">函数的第</span><span style=\" font-family:\'Times New Roman,serif\';\">5~8</span><span style=\" font-family:\'宋体\';\">个参数。最小圆半径和最大圆半径分别指利用</span><span style=\" font-family:\'Times New Roman,serif\';\">HoughCircles</span><span style=\" font-family:\'宋体\';\">函数能检测到的圆的最小半径和最大半径，其取决于棋子的半径大小。由于</span><span style=\" font-family:\'Times New Roman,serif\';\">HoughCircles</span><span style=\" font-family:\'宋体\';\">函数的边缘检测是基于</span><span style=\" font-family:\'Times New Roman,serif\';\">Canny</span><span style=\" font-family:\'宋体\';\">算子的，因此需确定</span><span style=\" font-family:\'Times New Roman,serif\';\">Canny</span><span style=\" font-family:\'宋体\';\">算子的阈值，函数中只需确定其最大阈值，该值越小，圆越容易被检出，但检测出假圆的概率会随值增大，该值越大圆越难以被检出，从而容易漏检，其推荐取值为</span><span style=\" font-family:\'Times New Roman,serif\';\">100~1000</span><span style=\" font-family:\'宋体\';\">。圆心的累加器阈值用于判别检测目标为圆的概率以及圆心的位置，若</span><span style=\" font-family:\'Times New Roman,serif\';\">Hough</span><span style=\" font-family:\'宋体\';\">空间内累加和大于该阈值，该点则对应于圆心，因此该值越大，能通过检测的圆就更接近完美的圆形，其与</span><span style=\" font-family:\'Times New Roman,serif\';\">Canny</span><span style=\" font-family:\'宋体\';\">边缘检测的最大阈值类似，过大或过小都会降低圆检测的准确率，推荐取值为</span><span style=\" font-family:\'Times New Roman,serif\';\">20</span><span style=\" font-family:\'宋体\';\">。识别半径指程序训练所用样本及识别所用图像的半径，其一般要小于棋子的实际半径，通过调整其与棋子实际半径的比例，可以调整训练所用样本及识别所用图像的大小，该比例为</span><span style=\" font-family:\'Times New Roman,serif\';\">0.6</span><span style=\" font-family:\'宋体\';\">时提取的部分棋子（预处理）图像样本如图</span><span style=\" font-family:\'Times New Roman,serif\';\">12</span><span style=\" font-family:\'宋体\';\">所示，此时程序识别精度较高。该比例的推荐取值为</span><span style=\" font-family:\'Times New Roman,serif\';\">0.5~0.6</span><span style=\" font-family:\'宋体\';\">。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/samples.png\" /> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 12</span><span style=\" font-family:\'宋体\';\"> 识别半径与棋子实际半径的比例为</span><span style=\" font-family:\'Times New Roman,serif\';\">0.6</span><span style=\" font-family:\'宋体\';\">时的训练样本示例</span> </p>\n"
                "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　注意：</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　（</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">）点击“保存”时，系统会对参数值进行检测，其中快进幅度和检测间隔要求为数值且≥</span><span style=\" font-family:\'Times New Roman,serif\';\">0</span><span style=\" font-family:\'宋体\';\">，其他数值型参数则要求＞</span><span style=\" font-family:\'Times New Roman,serif\';\">0</span><span style=\" font-family:\'宋体\';\">，若不满足以上要求系统会报错并停止保存操作。</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　（</span><span style=\" font-family:\'Times New Roman,serif\';\">2</span><span style=\" font-family:\'宋体\';\">）当参数值过大或过小时，系统会通过询问窗口向用户做出提醒。如当识别半径与棋子实际半径的比例大于</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">时，系统会询问“识别半径与棋子实际半径的比例大于</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">时会严重削弱程序的识别准确率，您确定要作此调整吗？”。虽然该询问仅为提示性质，但建议用户不要将该比例设为大于</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">的数值。</span> </p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "意见反馈":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">意见反馈</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　为了收集用户反馈，不断对系统进行改善，本系统设置了意见反馈功能，用户可从</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">帮助</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">意见反馈</span><span style=\" font-family:\'Times New Roman,serif\';\">…]</span><span style=\" font-family:\'宋体\';\">打开意见反馈界面。该界面包含</span><span style=\" font-family:\'Times New Roman,serif\';\">3</span><span style=\" font-family:\'宋体\';\">项必填信息，分别为用户</span><span style=\" font-family:\'Times New Roman,serif\';\">Email</span><span style=\" font-family:\'宋体\';\">、意见内容、和验证码（见图</span><span style=\" font-family:\'Times New Roman,serif\';\">13</span><span style=\" font-family:\'宋体\';\">）。收集用户</span><span style=\" font-family:\'Times New Roman,serif\';\">Email</span><span style=\" font-family:\'宋体\';\">是为了及时对用户的反馈予以回复并保持联系。设置验证码是为了防止用户恶意灌水，但出于节省时间的考虑，仅设置</span><span style=\" font-family:\'Times New Roman,serif\';\">4</span><span style=\" font-family:\'宋体\';\">位验证码，且可以通过点击验证码对其进行更换。用户对意见进行提交后，意见内容会直接发送至作者邮箱，从而对用户的意见进行收集。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/feedback.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 13</span><span style=\" font-family:\'宋体\';\"> 意见反馈界面</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　注意：</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　（</span><span style=\" font-family:\'Times New Roman,serif\';\">1</span><span style=\" font-family:\'宋体\';\">）验证码区分大小写；</span></p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　（</span><span style=\" font-family:\'Times New Roman,serif\';\">2</span><span style=\" font-family:\'宋体\';\">）点击“提交”按钮时，系统会自动对邮箱格式进行检验，若邮箱格式有误则报错并停止提交操作。</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "关于":
            self.ui.textBrowser.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">关于</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　从</span><span style=\" font-family:\'Times New Roman,serif\';\">[</span><span style=\" font-family:\'宋体\';\">帮助</span><span style=\" font-family:\'Times New Roman,serif\';\">]-[</span><span style=\" font-family:\'宋体\';\">关于</span><span style=\" font-family:\'Times New Roman,serif\';\">]</span><span style=\" font-family:\'宋体\';\">可打开“关于”界面，在该界面中可看到系统的</span><span style=\" font-family:\'Times New Roman,serif\';\">logo</span><span style=\" font-family:\'宋体\';\">、版本号、简要说明和版权所有人，其界面如图</span><span style=\" font-family:\'Times New Roman,serif\';\">14</span><span style=\" font-family:\'宋体\';\">所示。</span> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"images/about.png\"/> </p>\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">图</span><span style=\" font-family:\'Times New Roman,serif\';\"> 14</span><span style=\" font-family:\'宋体\';\"> “关于”界面</span></p></body></html>")
        elif self.ui.treeWidget.currentItem().text(0) == "快捷键一览":
            self.ui.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:x-large; font-weight:600;\">快捷键一览</span> </p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">　　中国象棋自动打谱系统的常用快捷键如下：<p>　　F1：用户手册</p><p>　　F5：开始检测</p><p>　　Ctrl+Enter+S：棋谱另存为</p><p>　　Ctrl+V：查看棋谱文本</p><p>　　Ctrl+P：暂停/继续检测</p><p>　　→：快进</p><p>　　Esc：结束检测</span> </p></body></html>")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = win_Manual()
    Main.show()
    sys.exit(app.exec_())
