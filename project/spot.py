# -*- coding: utf-8 -*-
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys,os
from PyQt4.QtCore import QUrl

import spot_window
import comment

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

class spotWindow(QDialog, spot_window.Ui_spotWindow):
    def __init__(self):
        super(spotWindow,self).__init__()
        self.setupUi(self)
        url_path = 'file:///' + guiPath + '/spot_search_test.html'
        self.spotView.setUrl(QUrl(url_path))
        self.spotView.show()

        csspath = guiPath + '\\qss\\spot_css.qss'
        file = QtCore.QFile(csspath)
        file.open(QtCore.QFile.ReadOnly)
        style_sheet = file.readAll()
        style_sheet = unicode(style_sheet, encoding='utf8')
        self.setStyleSheet(style_sheet)

    def setSpotContent(self,conn):
        u'''
        通过搜索框，进行地图搜索，评分等数据的显示
        :param conn: conn为数据库连接指针
        :return: 无返回值
        '''
        cur = self.conn_spot.cursor()
        SQL1="SELECT sceneName FROM scmLSG.sceneInfo WHERE sceneName LIKE \'%%%s%%\';"%self.spotName
        cur.execute(SQL1)
        name = cur.fetchall()
        sname = ''.join(name[0])
        sname = unicode(sname,"utf-8")
        self.spotNameLable.setText(sname)
        SQL2 = "SELECT ticket FROM scmLSG.sceneInfo WHERE sceneName LIKE \'%%%s%%\';" % self.spotName
        cur.execute(SQL2)
        ticket = cur.fetchall()
        sticket = ticket[0][0]
        sticket = str('%.2f'%sticket) + '元'
        sticket = unicode(sticket,"utf-8")
        self.expenseLable_2.setText(sticket)
        SQL3 = "SELECT visittime FROM scmLSG.sceneInfo WHERE sceneName LIKE \'%%%s%%\';" % self.spotName
        cur.execute(SQL3)
        time = cur.fetchall()
        stime = time[0][0]
        stime = str('%.2f'%stime) + '小时'
        stime = unicode(stime,"utf-8")
        self.timeLable_2.setText(stime)
        SQL4 = "SELECT avg(rcmMark) FROM scmLSG.uploadInfo WHERE sceneName LIKE \'%%%s%%\';"% self.spotName
        cur.execute(SQL4)
        mark = cur.fetchall()
        smark = mark[0][0]
        if smark == 'None':
            smark = '暂无评分'
        else:
            smark = str('%.2f'%smark) + ' 分'
        smark = unicode(smark,"utf-8")
        self.spotMarkLable.setText(smark)
        SQL5 = "SELECT rcmcomment FROM scmLSG.uploadInfo WHERE sceneName LIKE \'%%%s%%\' LIMIT 1;" % self.spotName
        cur.execute(SQL5)
        cmd1 = cur.fetchall()
        scmd1 = ''.join(str(cmd1[0][0]))
        scmd1 = '1.   ' + scmd1
        scmd1 = unicode(scmd1,"utf-8")
        self.commentLable_2.setText(scmd1)
        SQL6 = "SELECT rcmcomment FROM scmLSG.uploadInfo WHERE sceneName LIKE \'%%%s%%\' ORDER BY uploadtime DESC LIMIT 1;" % self.spotName
        cur.execute(SQL6)
        cmd2 = cur.fetchall()
        scmd2 = ''.join(str(cmd2[0][0]))
        scmd2 = '2.   ' + scmd2
        scmd2 = unicode(scmd2,"utf-8")
        self.commentLable_3.setText(scmd2)
        self.conn_spot.commit()
        cur.close()

    def openCommend(self):
        u'''
        单击评价按钮进行评价页面的转换，并传递用户名和景点到comment中
        :return:
        '''
        self.openCommendwindow = comment.commentWindow()
        self.openCommendwindow.getConn(self.conn_spot)
        self.openCommendwindow.getAccount(self.account)
        self.openCommendwindow.getSpot(self.spotName)
        self.openCommendwindow.show()

    def getConn(self,conn):
        u'''
        获得conn，作为类内参数
        :param conn:
        :return:
        '''
        self.conn_spot = conn
    def getSpot(self,spot):
        u'''
        获得景点名，作为类内参数
        :param spot:
        :return:
        '''
        self.spotNameLable.setText(u'景区名称：%s'%spot)
        self.spotName = spot
        return spot

    def getAccount(self,account):
        u'''
        获得用户名，作为类内参数
        :param account:
        :return:
        '''
        self.account = account
        return account

    def spot_search_html(self, a):
        u'''
        通过修改html文件来进行地图的搜索功能
        :param a:
        :return:
        '''
        f = open('spot_search.html', 'r+')
        flist = f.readlines()
        flist[25] = '    local.search("%s");\n' %a
        f = open('spot_search_test.html', 'w+')
        f.writelines(flist)
        f.close()
