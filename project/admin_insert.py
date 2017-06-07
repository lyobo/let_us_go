# -*- coding: utf-8 -*-
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys,os

import admin_insert_window

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


class admininsertWindow(QDialog,admin_insert_window.Ui_adminInsertDialog):
    def __init__(self):
        super(admininsertWindow,self).__init__()
        self.setupUi(self)
        self.picPath = ''

        csspath = guiPath + '\\qss\\admin_insert_css.qss'
        file = QtCore.QFile(csspath)
        file.open(QtCore.QFile.ReadOnly)
        style_sheet = file.readAll()
        style_sheet = unicode(style_sheet, encoding='utf8')
        self.setStyleSheet(style_sheet)

    def uploadScene(self):
        u'''
        提交数据
        :return:
        '''
        scene = self.sceneLine.text()
        ticket = self.ticketLine.text()
        time = self.timeLine.text()
        lon = self.lonLine.text()
        lat = self.latLine.text()
        conn = self.conn_insert
        spotlist = self.getcurrentSpot(conn)
        if scene in spotlist:
            QMessageBox.critical(self, u'错误', u'该景点已经存在!')
            return 1

        if not scene == '' :
            try:
                str1 = 'scenename'
                str2 = "'%s'" % scene
            except TypeError, error:
                QMessageBox.critical(self, u'错误', u'景点名称格式不正确!')
                self.sceneLine.setText('')
                return 1

            else:
                if not lon == '' or lat == '':
                    try:
                        lon_temp = float(lon)
                        lat_temp = float(lat)

                        str1 = str1 + ',coordinate'
                        str2 = str2 + ",ST_GeomFromText('POINT(%s %s)',4326)" %(lon_temp,lat_temp)
                    except ValueError, error:
                        QMessageBox.critical(self, u'错误', u'经纬度输入格式不正确!')
                        self.lonLine.setText('')
                        self.latLine.setText('')
                        return 1

                    else:
                        if not time == '':
                            try:
                                str1 = str1 + ',visittime'
                                str2 = str2 + ',%s' % float(time)
                            except ValueError, error:
                                QMessageBox.critical(self, u'错误', u'时间输入格式不正确!')
                                self.timeLine.setText('')
                                return 1

                        else:
                            QMessageBox.critical(self, u'错误', u'信息不完整，请输入时间!')
                            return 1
                else:
                    QMessageBox.critical(self, u'错误', u'信息不完整，请输入经纬度!')
                    return 1

        else:
            QMessageBox.critical(self, u'错误', u'请输入景点名!')
            return 1

        if self.Valid(ticket):
            str1 = str1 + ',ticket'
            str2 = str2 + ',%s' % float(ticket)


        cur = conn.cursor()
        str = 'insert into scmLSG.sceneinfo (%s) values (%s);'%(str1,str2)
        cur.execute(str)
        conn.commit()
        cur.close()
        QMessageBox.information(self, u"信息", u"您输入的数据已成功导入数据库！", QMessageBox.Yes)
        self.accept()

    def Valid(self,a):
        u'''
        判断数据是否为空（不含空格）
        :param a: 用户输入
        :return:
        '''
        if a.strip()  =='':
            return 0
        else:
            return 1

    def getConn(self,conn):
        u'''
        传递conn参数
        :param conn:
        :return:
        '''
        self.conn_insert = conn
        return conn

    def getAccount(self,account):
        u'''
        传递用户名参数
        :param account:
        :return:
        '''
        self.account = account
        return account

    def getSpot(self,spot):
        u'''
        传递景点名称
        :param spot:
        :return:
        '''
        self.spotName = spot
        self.spotNameLable.setText(spot)
        return spot

    def getcurrentSpot(self,conn):
        u'''
        获得数据库景点表内现有景点名列表
        :param conn:
        :return:
        '''
        conn_temp = conn
        cur = conn_temp.cursor()
        str = "select sceneName from scmLSG.sceneInfo;"
        cur.execute(str)
        name_list = cur.fetchall()
        spot_list = []
        for i in range(len(name_list)):
            name = name_list[i][0]
            u_name = unicode(name,"utf-8")
            spot_list.append(u_name)
        return spot_list