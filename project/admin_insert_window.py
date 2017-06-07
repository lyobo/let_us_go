# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_insert.ui'
#
# Created: Thu Feb 23 02:04:42 2017
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

class Ui_adminInsertDialog(object):
    def setupUi(self, adminInsertDialog):
        adminInsertDialog.setObjectName(_fromUtf8("adminInsertDialog"))
        adminInsertDialog.setWindowModality(QtCore.Qt.NonModal)
        adminInsertDialog.resize(592, 449)
        self.widget = QtGui.QWidget(adminInsertDialog)
        self.widget.setGeometry(QtCore.QRect(100, 60, 401, 251))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sceneLabel = QtGui.QLabel(self.widget)
        self.sceneLabel.setObjectName(_fromUtf8("sceneLabel"))
        self.horizontalLayout.addWidget(self.sceneLabel)
        self.sceneLine = QtGui.QLineEdit(self.widget)
        self.sceneLine.setObjectName(_fromUtf8("sceneLine"))
        self.horizontalLayout.addWidget(self.sceneLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ticketLabel = QtGui.QLabel(self.widget)
        self.ticketLabel.setObjectName(_fromUtf8("ticketLabel"))
        self.horizontalLayout_2.addWidget(self.ticketLabel)
        self.ticketLine = QtGui.QLineEdit(self.widget)
        self.ticketLine.setObjectName(_fromUtf8("ticketLine"))
        self.horizontalLayout_2.addWidget(self.ticketLine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.timeLabel = QtGui.QLabel(self.widget)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout_3.addWidget(self.timeLabel)
        self.timeLine = QtGui.QLineEdit(self.widget)
        self.timeLine.setObjectName(_fromUtf8("timeLine"))
        self.horizontalLayout_3.addWidget(self.timeLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lonLabel = QtGui.QLabel(self.widget)
        self.lonLabel.setObjectName(_fromUtf8("lonLabel"))
        self.horizontalLayout_4.addWidget(self.lonLabel)
        self.lonLine = QtGui.QLineEdit(self.widget)
        self.lonLine.setObjectName(_fromUtf8("lonLine"))
        self.horizontalLayout_4.addWidget(self.lonLine)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.latLabel = QtGui.QLabel(self.widget)
        self.latLabel.setObjectName(_fromUtf8("latLabel"))
        self.horizontalLayout_5.addWidget(self.latLabel)
        self.latLine = QtGui.QLineEdit(self.widget)
        self.latLine.setObjectName(_fromUtf8("latLine"))
        self.horizontalLayout_5.addWidget(self.latLine)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.uploadButton = QtGui.QPushButton(self.widget)
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.horizontalLayout_6.addWidget(self.uploadButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.retranslateUi(adminInsertDialog)
        QtCore.QObject.connect(self.uploadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), adminInsertDialog.uploadScene)
        QtCore.QMetaObject.connectSlotsByName(adminInsertDialog)

    def retranslateUi(self, adminInsertDialog):
        adminInsertDialog.setWindowTitle(_translate("adminInsertDialog", "插入景点信息", None))
        self.sceneLabel.setText(_translate("adminInsertDialog", "景点名称", None))
        self.ticketLabel.setText(_translate("adminInsertDialog", "票价", None))
        self.timeLabel.setText(_translate("adminInsertDialog", "游玩时间", None))
        self.lonLabel.setText(_translate("adminInsertDialog", "经度", None))
        self.latLabel.setText(_translate("adminInsertDialog", "纬度", None))
        self.uploadButton.setText(_translate("adminInsertDialog", "上传", None))

