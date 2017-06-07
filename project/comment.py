# -*- coding: utf-8 -*-
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys,os
import psycopg2 as pg
import urllib

import comment_window

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

guiPath = os.getcwd()
sys.path.append(guiPath)
guiUrl = urllib.pathname2url(guiPath)
guiUrl = guiUrl[3:]


class commentWindow(QDialog,comment_window.Ui_markWindow):
    def __init__(self):
        super(commentWindow,self).__init__()
        self.setupUi(self)
        self.picPath = ''

        csspath = guiPath + '\\qss\\comment_css.qss'
        file = QtCore.QFile(csspath)
        file.open(QtCore.QFile.ReadOnly)
        style_sheet = file.readAll()
        style_sheet = unicode(style_sheet, encoding='utf8')
        style1 = "QComboBox::down-arrow {image:url(%s/pic/jiantou.png);}\n"%guiUrl
        self.setStyleSheet(style_sheet+style1)

    def addPhoto(self):
        u'''
        上传图片，保留文件地址，并显示在框中
        :return:
        '''
        cur_path = os.getcwd()
        # fileName is the whole url of pic
        self.picPath =''
        self.picPath = QtGui.QFileDialog.getOpenFileName(self, 'open a file', cur_path, 'pic(*.jpg;*.tif;*.png;*.tiff)')
        # display the picture in picLabel and zoom to proper extent
        self.picLabel.setPixmap(QPixmap(self.picPath))
        self.picLabel.setScaledContents(True)

    def addCommend(self):
        str1 = 'uploadTime'
        str2 = '(select current_timestamp)'

        expense = self.expenseLine.text()
        time = self.timeLine.text()
        mark = self.markBox.currentText()
        comment = self.commentText.toPlainText()

        if not expense == '':
            try:
                expanse_temp = float(expense)
                str1 = str1 + ',rcmTicket'
                str2 = str2 + ',%s' % expanse_temp
            except ValueError, error:
                QMessageBox.critical(self,u'错误', u'消费金额应是数字!')
                self.expenseLine.setText('')
                return 1

            else:
                if not time == '':
                    try:
                        time_temp = float(time)
                        if time_temp <= 0:
                            QMessageBox.critical(self, u'错误', u'输入时间不能小于等于零！!')
                            return 1
                        else:
                            str1 = str1 + ',rcmTime'
                            str2 = str2 + ',%s' % time_temp
                    except ValueError, error:
                        QMessageBox.critical(self, u'错误', u'时间输入格式不正确，时间按小时输入!')
                        self.timeLine.setText('')
                        return 1

                    else:
                        if not mark == '':
                            str1 = str1 + ',rcmMark'
                            str2 = str2 + ',%s' % int(mark)

                        else:
                            if not comment == '':
                                str1 = str1 + ',rcmComment'
                                str2 = str2 + ",'%s'" % comment

                            else:
                                QMessageBox.critical(self, u'错误', u'信息不完整!')
                                # self.expenseLine.setText('')
                                return 1

        else:
            QMessageBox.critical(self, u'错误', u'信息不完整!')
            self.expenseLine.setText('')
            return 1

        if self.Valid(self.picPath):
            fin = open(self.picPath, "rb")
            img = fin.read()
            binary = pg.Binary(img)
            fin.close()
            str1 = str1 + ',pic'
            str2 = str2 + ',%s' % binary

        if self.Valid(comment):
            str1 = str1 + ',rcmComment'
            str2 = str2 + ",'%s'" % comment

        str1 = str1 + ',userName'
        str2 = str2 + ",'%s'" % self.account

        str1 = str1 + ',sceneName'
        str2 = str2 + ",'%s'" % self.spotName
        conn1 = self.conn_comment
        cur = conn1.cursor()
        str = 'insert into scmLSG.uploadInfo (%s) values(%s);' % (str1, str2)
        cur.execute(str)
        conn1.commit()
        cur.close()
        QMessageBox.information(self, u"提示", u"您的评价已成功上传", QMessageBox.Yes)
        self.accept()

    def Valid(self,a):
        u'''
        判断输入是否为空
        :param a: 输入字符串
        :return: 为空，返回0，否则返回1
        '''
        # 判断的时候忽略前后空格
        if a.strip()  =='':
            return 0
        else:
            return 1

    def getConn(self,conn):
        u'''
        conn参数传递
        :param conn:
        :return:
        '''
        self.conn_comment = conn
        return conn

    def getAccount(self,account):
        u'''
        用户名参数传递
        :param account:
        :return:
        '''
        self.account = account
        return account

    def getSpot(self,spot):
        u'''
        景点名称参数传递
        :param spot:
        :return:
        '''
        self.spotName = spot
        self.spotNameLable.setText(spot)
        return spot