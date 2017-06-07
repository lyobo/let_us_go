# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'halfautoPlan_window.ui'
#
# Created: Tue Feb 21 16:32:41 2017
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

class Ui_halfautoPlan(object):
    def setupUi(self, halfautoPlan):
        halfautoPlan.setObjectName(_fromUtf8("halfautoPlan"))
        halfautoPlan.resize(582, 617)
        self.planView = QtWebKit.QWebView(halfautoPlan)
        self.planView.setGeometry(QtCore.QRect(0, 80, 581, 421))
        self.planView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.planView.setObjectName(_fromUtf8("planView"))
        self.resultLabel = QtGui.QLabel(halfautoPlan)
        self.resultLabel.setGeometry(QtCore.QRect(0, 510, 581, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(12)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.layoutWidget = QtGui.QWidget(halfautoPlan)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 581, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spotLabel = QtGui.QLabel(self.layoutWidget)
        self.spotLabel.setObjectName(_fromUtf8("spotLabel"))
        self.horizontalLayout.addWidget(self.spotLabel)
        self.spotLine = QtGui.QLineEdit(self.layoutWidget)
        self.spotLine.setObjectName(_fromUtf8("spotLine"))
        self.horizontalLayout.addWidget(self.spotLine)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.addButton = QtGui.QToolButton(self.layoutWidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout_2.addWidget(self.addButton)
        self.resetButton = QtGui.QToolButton(self.layoutWidget)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.timeLabel = QtGui.QLabel(self.layoutWidget)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout_3.addWidget(self.timeLabel)
        self.timeEdit = QtGui.QLineEdit(self.layoutWidget)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.horizontalLayout_3.addWidget(self.timeEdit)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.showLabel = QtGui.QLabel(self.layoutWidget)
        self.showLabel.setObjectName(_fromUtf8("showLabel"))
        self.horizontalLayout_5.addWidget(self.showLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.halfautoPlan_2 = QtGui.QPushButton(self.layoutWidget)
        self.halfautoPlan_2.setObjectName(_fromUtf8("halfautoPlan_2"))
        self.horizontalLayout_5.addWidget(self.halfautoPlan_2)
        self.saveButton = QtGui.QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_5.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(halfautoPlan)
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), halfautoPlan.add)
        QtCore.QObject.connect(self.resetButton, QtCore.SIGNAL(_fromUtf8("clicked()")), halfautoPlan.reset)
        QtCore.QObject.connect(self.halfautoPlan_2, QtCore.SIGNAL(_fromUtf8("clicked()")), halfautoPlan.halfautoPlan)
        QtCore.QObject.connect(self.saveButton, QtCore.SIGNAL(_fromUtf8("clicked()")), halfautoPlan.save)
        QtCore.QMetaObject.connectSlotsByName(halfautoPlan)

    def retranslateUi(self, halfautoPlan):
        halfautoPlan.setWindowTitle(_translate("halfautoPlan", "半随机推荐路线", None))
        self.resultLabel.setText(_translate("halfautoPlan", "规划结果：", None))
        self.spotLabel.setText(_translate("halfautoPlan", "请输入您想去的景点：", None))
        self.addButton.setText(_translate("halfautoPlan", "添加", None))
        self.resetButton.setText(_translate("halfautoPlan", "重置", None))
        self.timeLabel.setText(_translate("halfautoPlan", "预计游览", None))
        self.label.setText(_translate("halfautoPlan", "小时", None))
        self.showLabel.setText(_translate("halfautoPlan", "目前已输入的景点名：", None))
        self.halfautoPlan_2.setText(_translate("halfautoPlan", "开始规划", None))
        self.saveButton.setText(_translate("halfautoPlan", "保存规划结果", None))

from PyQt4 import QtWebKit
