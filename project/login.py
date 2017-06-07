# -*- coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys,os
import psycopg2 as pg
import time

import main_admin
import main
import login_window

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


class loginWindow(QDialog,login_window.Ui_loginWindow):
    def __init__(self):
        super(loginWindow,self).__init__()
        self.setupUi(self)
        time.sleep(0.25)
        csspath = guiPath + '\\qss\\login_css.qss'
        file = QtCore.QFile(csspath)
        file.open(QtCore.QFile.ReadOnly)
        style_sheet = file.readAll()
        style_sheet = unicode(style_sheet, encoding='utf8')
        self.setStyleSheet(style_sheet)

    def login(self):
        u'''
        获得文本框输入的帐号密码，进行数据库连接，进行必要的异常检查
        :return:
        '''
        account = self.accountLine.text()
        password = self.passwordLine.text()
        conn = NULL
        conn = self.connect(account,password)
        # link to main.py
        if conn == 1:
            return 1
        else:
            self.link2main(conn)

    def connect(self,account,psd):
        u'''
        连接数据库
        :param account: 用户名
        :param psd: 密码
        :return: 有异常返回1，否则返回conn
        '''
        try:
            conn = pg.connect(database='letsgo', password=psd, user=account,host='localhost', port='5432')
            #print('connect success')
            return conn
        except Exception,e:
            QMessageBox.critical(self, u"提示",u"帐号 密码不符，请重新输入。")
            self.accountLine.setText('')
            self.passwordLine.setText('')
            return 1

    def link2main(self,flag):
        u'''
        进行页面之间的转换，并传递conn,用户名等参数，同时由于用户属性不同，打开不同页面
        :param flag: 如果无异常，为conn,有异常是1
        :return:
        '''
        if flag !=0:
            if flag.get_parameter_status('is_superuser') == 'off':
                self.openMainwindow = main.mainWindow()
                self.openMainwindow.show()
                self.accept()
                account = self.accountLine.text()
                self.parameterTransform(flag,account)
            else:
                self.openMainwindow = main_admin.adminWindow()
                self.openMainwindow.show()
                self.accept()
                account = self.accountLine.text()
                self.parameterTransform(flag, account)

    def parameterTransform(self,conn,account):
        u'''
        参数传递
        :param conn:
        :param account:
        :return:
        '''
        self.openMainwindow.getConn(conn)
        self.openMainwindow.getAccount(account)

    def register(self):
        u'''
        对用户进行注册，权限设置，并写入用户信息表中
        :return:
        '''
        re_account = self.registeraccount.text()
        re_psd = self.registerpsd.text()
        recon = self.registercon.text()
        remail = self.mailEdit.text()
        split = remail.split('@')
        flag = self.reValid(re_account, re_psd, recon, remail)
        flag0 = 0
        if (flag):
            if not re_account.isdigit():
                if len(split) == 2:
                    if(re_psd == recon):
                        try:
                            conn = pg.connect(database='letsgo', password='admin', user='admin', host='localhost', port='5432')
                            cur = conn.cursor()
                            strSQL = "INSERT INTO scmLSG.userInfo (userName,password,mailbox) VALUES('%s','%s','%s');" % (re_account, re_psd, remail)
                            cur.execute(strSQL)
                            cur.close()
                            conn.commit()
                            conn.close()
                        except:
                            QMessageBox.critical(self, u"提示", u"该帐号已经被其他人用啦~请您重新选择一个吧")
                            self.registerpsd.setText('')
                            self.registeraccount.setText('')
                            self.registercon.setText('')
                            self.mailEdit.setText('')
                            return 1
                        else:
                            conn = pg.connect(database='letsgo', password='admin', user='admin', host='localhost', port='5432')
                            cur = conn.cursor()
                            str = 'create user %s;' % re_account
                            cur.execute(str)
                            str = "alter user %s with password '%s';" % (re_account, re_psd)
                            cur.execute(str)
                            str = 'grant usage on schema scmLSG to %s;'%re_account
                            cur.execute(str)
                            str = "grant insert,update,select on scmLSG.uploadInfo to %s;" % re_account
                            cur.execute(str)
                            str = "grant select on scmLSG.sceneInfo to %s;" % re_account
                            cur.execute(str)
                            cur.close()
                            conn.commit()
                            flag0 = 1
                            QMessageBox.information(self, u"提示", u"恭喜您注册成功，快开始您的旅程吧！",QMessageBox.Yes | QMessageBox.No)
                    else:
                        QMessageBox.critical(self, u"提示!", u"密码与确认密码不一致！")
                        self.registercon.setText('')
                        self.registerpsd.setText('')
                        return 1
                else:
                    QMessageBox.critical(self, u"提示!",u"您输入的邮箱格式不正确!")
                    self.mailEdit.setText('')
                    return 1
            else:
                QMessageBox.critical(self, u"提示!", u"您输入的账户是纯数字!请至少包含一个字母!")
                self.registeraccount.setText('')
                return 1
        else:
            QMessageBox.critical(self, u"提示!", u"您填写的信息不完整！")
            return 1

    def reValid(self,a,b,c,d):
        '''
        判断abcd是否均有值
        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        '''
        if a.strip() =='':
            return 0
        elif b.strip()=='':
            return 0
        elif c.strip() =='':
            return 0
        elif d.strip() =='':
            return 0
        else:
            return 1

    def find(self):
        u'''
        遗忘密码时提供解决方案
        :return:
        '''
        QMessageBox.information(self, u"说明", u"请通过邮箱联系作者:201411172010@mail.bnu.edu.cn，随时帮您解决问题")
        print('find')


app = QApplication([])
picPath = guiPath + '\\pic\\loadingPic.jpg'
splash = QSplashScreen(QPixmap(picPath))
splash.show()
app.processEvents()
qgisPath = 'C:\\Program Files (x86)\\QGIS 2.16.0\\apps\\qgis'
QgsApplication.setPrefixPath(qgisPath,True)
QgsApplication.initQgis()
main_win = loginWindow()
main_win.show()
splash.finish(main_win)
sys.exit(app.exec_())