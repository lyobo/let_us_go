# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment_window.ui'
#
# Created: Thu Feb 23 01:47:42 2017
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

class Ui_markWindow(object):
    def setupUi(self, markWindow):
        markWindow.setObjectName(_fromUtf8("markWindow"))
        markWindow.resize(564, 408)
        self.layoutWidget = QtGui.QWidget(markWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 542, 28))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.spotNameLable = QtGui.QLabel(self.layoutWidget)
        self.spotNameLable.setMinimumSize(QtCore.QSize(0, 26))
        self.spotNameLable.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.spotNameLable.setFont(font)
        self.spotNameLable.setObjectName(_fromUtf8("spotNameLable"))
        self.horizontalLayout_6.addWidget(self.spotNameLable)
        spacerItem = QtGui.QSpacerItem(458, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.layoutWidget1 = QtGui.QWidget(markWindow)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 43, 261, 211))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.expenseLable = QtGui.QLabel(self.layoutWidget1)
        self.expenseLable.setObjectName(_fromUtf8("expenseLable"))
        self.horizontalLayout.addWidget(self.expenseLable)
        self.expenseLine = QtGui.QLineEdit(self.layoutWidget1)
        self.expenseLine.setObjectName(_fromUtf8("expenseLine"))
        self.horizontalLayout.addWidget(self.expenseLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.timeLable = QtGui.QLabel(self.layoutWidget1)
        self.timeLable.setObjectName(_fromUtf8("timeLable"))
        self.horizontalLayout_3.addWidget(self.timeLable)
        self.timeLine = QtGui.QLineEdit(self.layoutWidget1)
        self.timeLine.setObjectName(_fromUtf8("timeLine"))
        self.horizontalLayout_3.addWidget(self.timeLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.markLable = QtGui.QLabel(self.layoutWidget1)
        self.markLable.setObjectName(_fromUtf8("markLable"))
        self.horizontalLayout_4.addWidget(self.markLable)
        self.markBox = QtGui.QComboBox(self.layoutWidget1)
        self.markBox.setObjectName(_fromUtf8("markBox"))
        self.markBox.addItem(_fromUtf8(""))
        self.markBox.setItemText(0, _fromUtf8(""))
        self.markBox.addItem(_fromUtf8(""))
        self.markBox.addItem(_fromUtf8(""))
        self.markBox.addItem(_fromUtf8(""))
        self.markBox.addItem(_fromUtf8(""))
        self.markBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.markBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.widget = QtGui.QWidget(markWindow)
        self.widget.setGeometry(QtCore.QRect(10, 260, 542, 131))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.commentLable = QtGui.QLabel(self.widget)
        self.commentLable.setObjectName(_fromUtf8("commentLable"))
        self.horizontalLayout_5.addWidget(self.commentLable)
        self.commentText = QtGui.QTextEdit(self.widget)
        self.commentText.setObjectName(_fromUtf8("commentText"))
        self.horizontalLayout_5.addWidget(self.commentText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.commentButton = QtGui.QPushButton(self.widget)
        self.commentButton.setObjectName(_fromUtf8("commentButton"))
        self.horizontalLayout_7.addWidget(self.commentButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.splitter = QtGui.QSplitter(markWindow)
        self.splitter.setGeometry(QtCore.QRect(277, 43, 271, 211))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.picLabel = QtGui.QLabel(self.splitter)
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pictureButton = QtGui.QPushButton(self.widget1)
        self.pictureButton.setObjectName(_fromUtf8("pictureButton"))
        self.horizontalLayout_2.addWidget(self.pictureButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.retranslateUi(markWindow)
        QtCore.QObject.connect(self.pictureButton, QtCore.SIGNAL(_fromUtf8("clicked()")), markWindow.addPhoto)
        QtCore.QObject.connect(self.commentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), markWindow.addCommend)
        QtCore.QMetaObject.connectSlotsByName(markWindow)

    def retranslateUi(self, markWindow):
        markWindow.setWindowTitle(_translate("markWindow", "走着", None))
        self.spotNameLable.setText(_translate("markWindow", "景区名称", None))
        self.expenseLable.setText(_translate("markWindow", "消费：", None))
        self.timeLable.setText(_translate("markWindow", "游览时间：", None))
        self.markLable.setText(_translate("markWindow", "评分：", None))
        self.markBox.setItemText(1, _translate("markWindow", "5", None))
        self.markBox.setItemText(2, _translate("markWindow", "4", None))
        self.markBox.setItemText(3, _translate("markWindow", "3", None))
        self.markBox.setItemText(4, _translate("markWindow", "2", None))
        self.markBox.setItemText(5, _translate("markWindow", "1", None))
        self.commentLable.setText(_translate("markWindow", "评价：", None))
        self.commentButton.setText(_translate("markWindow", "上传评价", None))
        self.pictureButton.setText(_translate("markWindow", "上传照片", None))

