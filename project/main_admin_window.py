# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_web_admin.ui'
#
# Created: Thu Feb 23 01:58:04 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_visitorWindow(object):
    def setupUi(self, visitorWindow):
        visitorWindow.setObjectName(_fromUtf8("visitorWindow"))
        visitorWindow.resize(691, 651)
        self.visitorTab = QtGui.QTabWidget(visitorWindow)
        self.visitorTab.setGeometry(QtCore.QRect(9, 38, 671, 611))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.visitorTab.setFont(font)
        self.visitorTab.setTabsClosable(False)
        self.visitorTab.setMovable(False)
        self.visitorTab.setObjectName(_fromUtf8("visitorTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 651, 551))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.searchLine = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.searchLine.setFont(font)
        self.searchLine.setObjectName(_fromUtf8("searchLine"))
        self.horizontalLayout_2.addWidget(self.searchLine)
        self.searchButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.searchButton.setFont(font)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.fastcommentButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.fastcommentButton.setFont(font)
        self.fastcommentButton.setObjectName(_fromUtf8("fastcommentButton"))
        self.horizontalLayout_2.addWidget(self.fastcommentButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.heatBox = QtGui.QComboBox(self.layoutWidget)
        self.heatBox.setMinimumSize(QtCore.QSize(91, 22))
        self.heatBox.setMaximumSize(QtCore.QSize(91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.heatBox.setFont(font)
        self.heatBox.setObjectName(_fromUtf8("heatBox"))
        self.heatBox.addItem(_fromUtf8(""))
        self.heatBox.addItem(_fromUtf8(""))
        self.heatBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.heatBox)
        self.evaluateBox = QtGui.QComboBox(self.layoutWidget)
        self.evaluateBox.setMinimumSize(QtCore.QSize(91, 22))
        self.evaluateBox.setMaximumSize(QtCore.QSize(91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.evaluateBox.setFont(font)
        self.evaluateBox.setObjectName(_fromUtf8("evaluateBox"))
        self.evaluateBox.addItem(_fromUtf8(""))
        self.evaluateBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.evaluateBox)
        self.expenseBox = QtGui.QComboBox(self.layoutWidget)
        self.expenseBox.setMinimumSize(QtCore.QSize(91, 22))
        self.expenseBox.setMaximumSize(QtCore.QSize(91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.expenseBox.setFont(font)
        self.expenseBox.setObjectName(_fromUtf8("expenseBox"))
        self.expenseBox.addItem(_fromUtf8(""))
        self.expenseBox.addItem(_fromUtf8(""))
        self.expenseBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.expenseBox)
        self.searchButton_2 = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.searchButton_2.setFont(font)
        self.searchButton_2.setObjectName(_fromUtf8("searchButton_2"))
        self.horizontalLayout_3.addWidget(self.searchButton_2)
        spacerItem1 = QtGui.QSpacerItem(28, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.uploadButton = QtGui.QPushButton(self.layoutWidget)
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.horizontalLayout_6.addWidget(self.uploadButton)
        self.updatetimeButton = QtGui.QPushButton(self.layoutWidget)
        self.updatetimeButton.setObjectName(_fromUtf8("updatetimeButton"))
        self.horizontalLayout_6.addWidget(self.updatetimeButton)
        self.updateticketButton = QtGui.QPushButton(self.layoutWidget)
        self.updateticketButton.setObjectName(_fromUtf8("updateticketButton"))
        self.horizontalLayout_6.addWidget(self.updateticketButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.webView = QtWebKit.QWebView(self.layoutWidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 1, 0, 1, 1)
        self.visitorTab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 651, 421))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 651, 81))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.planTimeLable = QtGui.QLabel(self.layoutWidget1)
        self.planTimeLable.setObjectName(_fromUtf8("planTimeLable"))
        self.horizontalLayout_5.addWidget(self.planTimeLable)
        self.visitTimeBox = QtGui.QComboBox(self.layoutWidget1)
        self.visitTimeBox.setObjectName(_fromUtf8("visitTimeBox"))
        self.visitTimeBox.addItem(_fromUtf8(""))
        self.visitTimeBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.visitTimeBox)
        self.planButton = QtGui.QPushButton(self.layoutWidget1)
        self.planButton.setObjectName(_fromUtf8("planButton"))
        self.horizontalLayout_5.addWidget(self.planButton)
        self.halfautoButton = QtGui.QPushButton(self.layoutWidget1)
        self.halfautoButton.setObjectName(_fromUtf8("halfautoButton"))
        self.horizontalLayout_5.addWidget(self.halfautoButton)
        self.recommendButton = QtGui.QPushButton(self.layoutWidget1)
        self.recommendButton.setObjectName(_fromUtf8("recommendButton"))
        self.horizontalLayout_5.addWidget(self.recommendButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.layoutWidget2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 530, 651, 32))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.vectorButton = QtGui.QPushButton(self.layoutWidget2)
        self.vectorButton.setObjectName(_fromUtf8("vectorButton"))
        self.horizontalLayout_4.addWidget(self.vectorButton)
        self.rasterButton = QtGui.QPushButton(self.layoutWidget2)
        self.rasterButton.setObjectName(_fromUtf8("rasterButton"))
        self.horizontalLayout_4.addWidget(self.rasterButton)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.loadButton = QtGui.QPushButton(self.layoutWidget2)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.horizontalLayout_8.addWidget(self.loadButton)
        self.saveButton = QtGui.QPushButton(self.layoutWidget2)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_8.addWidget(self.saveButton)
        self.visitorTab.addTab(self.tab_2, _fromUtf8(""))
        self.label = QtGui.QLabel(visitorWindow)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 661, 21))
        self.label.setMinimumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(".designer/backup/地图.jpg")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(visitorWindow)
        self.visitorTab.setCurrentIndex(0)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.openSpot)
        QtCore.QObject.connect(self.searchButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.searchPlot)
        QtCore.QObject.connect(self.planButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.planRoutine)
        QtCore.QObject.connect(self.recommendButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.recommendRoutine)
        QtCore.QObject.connect(self.fastcommentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.openCommend)
        QtCore.QObject.connect(self.vectorButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.addShp)
        QtCore.QObject.connect(self.rasterButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.addRas)
        QtCore.QObject.connect(self.saveButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.saveRoute)
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.loadRoute)
        QtCore.QObject.connect(self.uploadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.insertScene)
        QtCore.QObject.connect(self.halfautoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.halfAutoPlan)
        QtCore.QObject.connect(self.updatetimeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.updatetime)
        QtCore.QObject.connect(self.updateticketButton, QtCore.SIGNAL(_fromUtf8("clicked()")), visitorWindow.updateticket)
        QtCore.QMetaObject.connectSlotsByName(visitorWindow)

    def retranslateUi(self, visitorWindow):
        visitorWindow.setWindowTitle(_translate("visitorWindow", "走着", None))
        self.searchButton.setText(_translate("visitorWindow", "查看评价", None))
        self.fastcommentButton.setText(_translate("visitorWindow", "&快速添加评价", None))
        self.heatBox.setItemText(0, _translate("visitorWindow", "全部景区", None))
        self.heatBox.setItemText(1, _translate("visitorWindow", "热门景区", None))
        self.heatBox.setItemText(2, _translate("visitorWindow", "冷门景区", None))
        self.evaluateBox.setItemText(0, _translate("visitorWindow", "全部景区", None))
        self.evaluateBox.setItemText(1, _translate("visitorWindow", "好评景区", None))
        self.expenseBox.setItemText(0, _translate("visitorWindow", "全部景区", None))
        self.expenseBox.setItemText(1, _translate("visitorWindow", "收费景区", None))
        self.expenseBox.setItemText(2, _translate("visitorWindow", "免费景区", None))
        self.searchButton_2.setText(_translate("visitorWindow", "搜索", None))
        self.label_2.setText(_translate("visitorWindow", "管理员功能：", None))
        self.uploadButton.setText(_translate("visitorWindow", "添加景点", None))
        self.updatetimeButton.setText(_translate("visitorWindow", "更新游玩时间", None))
        self.updateticketButton.setText(_translate("visitorWindow", "更新票价信息", None))
        self.visitorTab.setTabText(self.visitorTab.indexOf(self.tab), _translate("visitorWindow", "景点", None))
        self.planTimeLable.setText(_translate("visitorWindow", "预计浏览时间:   ", None))
        self.visitTimeBox.setItemText(0, _translate("visitorWindow", "半天", None))
        self.visitTimeBox.setItemText(1, _translate("visitorWindow", "一天", None))
        self.planButton.setText(_translate("visitorWindow", "自主规划路线", None))
        self.halfautoButton.setText(_translate("visitorWindow", "半自主规划路线", None))
        self.recommendButton.setText(_translate("visitorWindow", "随机推荐路线", None))
        self.vectorButton.setText(_translate("visitorWindow", "&矢量格式", None))
        self.rasterButton.setText(_translate("visitorWindow", "&栅格格式", None))
        self.loadButton.setText(_translate("visitorWindow", "&加载路线", None))
        self.saveButton.setText(_translate("visitorWindow", "&路线保存", None))
        self.visitorTab.setTabText(self.visitorTab.indexOf(self.tab_2), _translate("visitorWindow", "路线", None))

from PyQt4 import QtWebKit
