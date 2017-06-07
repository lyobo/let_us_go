# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spot_window_web.ui'
#
# Created: Sat Feb 18 23:17:31 2017
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

class Ui_spotWindow(object):
    def setupUi(self, spotWindow):
        spotWindow.setObjectName(_fromUtf8("spotWindow"))
        spotWindow.resize(559, 499)
        self.spotFrame = QtGui.QFrame(spotWindow)
        self.spotFrame.setGeometry(QtCore.QRect(9, 87, 531, 211))
        self.spotFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.spotFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.spotFrame.setObjectName(_fromUtf8("spotFrame"))
        self.spotView = QtWebKit.QWebView(self.spotFrame)
        self.spotView.setGeometry(QtCore.QRect(0, 0, 531, 221))
        self.spotView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.spotView.setObjectName(_fromUtf8("spotView"))
        self.commentLable_2 = QtGui.QLabel(spotWindow)
        self.commentLable_2.setGeometry(QtCore.QRect(10, 360, 531, 51))
        self.commentLable_2.setObjectName(_fromUtf8("commentLable_2"))
        self.commentLable_3 = QtGui.QLabel(spotWindow)
        self.commentLable_3.setGeometry(QtCore.QRect(9, 420, 531, 51))
        self.commentLable_3.setObjectName(_fromUtf8("commentLable_3"))
        self.layoutWidget = QtGui.QWidget(spotWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 50, 531, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.expenseLable = QtGui.QLabel(self.layoutWidget)
        self.expenseLable.setMinimumSize(QtCore.QSize(0, 20))
        self.expenseLable.setMaximumSize(QtCore.QSize(16777215, 20))
        self.expenseLable.setObjectName(_fromUtf8("expenseLable"))
        self.horizontalLayout_2.addWidget(self.expenseLable)
        self.expenseLable_2 = QtGui.QLabel(self.layoutWidget)
        self.expenseLable_2.setText(_fromUtf8(""))
        self.expenseLable_2.setObjectName(_fromUtf8("expenseLable_2"))
        self.horizontalLayout_2.addWidget(self.expenseLable_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.timeLable = QtGui.QLabel(self.layoutWidget)
        self.timeLable.setObjectName(_fromUtf8("timeLable"))
        self.horizontalLayout_2.addWidget(self.timeLable)
        self.timeLable_2 = QtGui.QLabel(self.layoutWidget)
        self.timeLable_2.setText(_fromUtf8(""))
        self.timeLable_2.setObjectName(_fromUtf8("timeLable_2"))
        self.horizontalLayout_2.addWidget(self.timeLable_2)
        spacerItem1 = QtGui.QSpacerItem(178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.layoutWidget1 = QtGui.QWidget(spotWindow)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 320, 531, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.commentLable = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(12)
        self.commentLable.setFont(font)
        self.commentLable.setObjectName(_fromUtf8("commentLable"))
        self.horizontalLayout_3.addWidget(self.commentLable)
        spacerItem2 = QtGui.QSpacerItem(478, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.widget = QtGui.QWidget(spotWindow)
        self.widget.setGeometry(QtCore.QRect(11, 11, 531, 28))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spotNameLable = QtGui.QLabel(self.widget)
        self.spotNameLable.setMinimumSize(QtCore.QSize(0, 26))
        self.spotNameLable.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.spotNameLable.setFont(font)
        self.spotNameLable.setObjectName(_fromUtf8("spotNameLable"))
        self.horizontalLayout.addWidget(self.spotNameLable)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.spotMarkLable = QtGui.QLabel(self.widget)
        self.spotMarkLable.setObjectName(_fromUtf8("spotMarkLable"))
        self.horizontalLayout.addWidget(self.spotMarkLable)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.commentButton = QtGui.QPushButton(self.widget)
        self.commentButton.setObjectName(_fromUtf8("commentButton"))
        self.horizontalLayout.addWidget(self.commentButton)

        self.retranslateUi(spotWindow)
        QtCore.QObject.connect(self.commentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), spotWindow.openCommend)
        QtCore.QMetaObject.connectSlotsByName(spotWindow)

    def retranslateUi(self, spotWindow):
        spotWindow.setWindowTitle(_translate("spotWindow", "走着", None))
        self.commentLable_2.setText(_translate("spotWindow", "1. ", None))
        self.commentLable_3.setText(_translate("spotWindow", "2. ", None))
        self.expenseLable.setText(_translate("spotWindow", "门票价格：", None))
        self.timeLable.setText(_translate("spotWindow", "推荐游览时间：", None))
        self.commentLable.setText(_translate("spotWindow", "评价：", None))
        self.spotNameLable.setText(_translate("spotWindow", "景区名称", None))
        self.spotMarkLable.setText(_translate("spotWindow", "评分:", None))
        self.commentButton.setText(_translate("spotWindow", "上传评价", None))

from PyQt4 import QtWebKit
