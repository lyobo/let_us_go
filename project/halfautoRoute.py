# -*- coding: utf-8 -*-
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys,os
import psycopg2 as pg
from PyQt4.QtCore import QUrl

import halfautoPlan_window

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


class halfautoWindow(QDialog,halfautoPlan_window.Ui_halfautoPlan):
    def __init__(self):
        super(halfautoWindow,self).__init__()
        self.setupUi(self)
        self.spotList = []
        #self.originalList = (u'天安门广场',u'故宫',u'玉渊潭公园',u'景山公园',u'香山公园',u'颐和园',u'天坛公园',u'八达岭长城')
        self.planList = []
        self.plantime = 0
        # WebView initalization
        url_path = 'file:///' + guiPath + '/map_loading.html'
        self.planView.setUrl(QUrl(url_path))
        self.planView.show()

        csspath = guiPath + '\\qss\\halfautoRoute_css.qss'
        file = QtCore.QFile(csspath)
        file.open(QtCore.QFile.ReadOnly)
        style_sheet = file.readAll()
        style_sheet = unicode(style_sheet, encoding='utf8')
        self.setStyleSheet(style_sheet)

    def add(self):
        u'''
        输入景点名称，判断其在数据库中是否存在，并放到下面的label中
        :return:
        '''
        spot_temp = self.spotLine.text()
        originalList = self.getcurrentSpot(self.conn_half)
        if spot_temp not in originalList:
            QMessageBox.critical(self, u"错误!", u"抱歉，数据库中暂无该景点，请输入全名或者更换景点")
            self.spotLine.setText('')
        elif spot_temp in self.spotList:
            QMessageBox.critical(self, u"错误!", u"不能输入重复景点")
            self.spotLine.setText('')
        else:
            self.spotList.append(spot_temp)
            str = ','.join(self.spotList)
            self.showLabel.setText(u'目前已输入的景点名：%s'%str)
            self.spotLine.setText('')

    def getTime(self):
        u'''
        得到用户输入计划旅游时间，并进行合理性判断
        :return:
        '''
        temp = self.timeEdit.text()
        if temp == '':
            QMessageBox.information(self, u"提示!", u"游览时间不能为空")
            return 0
        elif temp.isdigit():
            if float(temp) > 12:
                QMessageBox.information(self, u"提示!", u"计划游览时间过长,旅游虽好，也要注意休息哟！推荐游览时间为4到9小时")
                return 0
            elif float(temp) < 3:
                QMessageBox.information(self, u"提示!", u"计划游览时间过短，可能不会玩得尽兴哟！推荐游览时间为4到9小时")
                return 0
            else:
                return float(temp)
        else:
            QMessageBox.information(self, u"提示!", u"游览时间要求为输入4-12的阿拉伯数字")
            return 0
    def reset(self):
        '''
        重置页面，便于二次操作
        :return:
        '''
        self.spotLine.setText('')
        self.showLabel.setText(u'目前已输入的景点名：')
        self.spotList = []
        self.planList = []
        self.plantime = 0

    def halfautoPlan(self):
        u'''
        判断用户输入景点数，判断合理性，并进行联想景点搜索以及路线规划。
        :return:
        '''
        if self.spotList ==[]:
            QMessageBox.information(self, u"提示!", u"请至少输入一个景点哟。")
        else:
            conn = pg.connect(database='letsgo', password='admin', user='admin', host='localhost', port='5432')
            cur = conn.cursor()
            length = len(self.spotList)
            time = self.getTime()
            if time == 0:
                return 1
            if length == 0:
                QMessageBox.critical(self, u"错误!", u"请至少输入一个景点！")
            elif length == 1:
                self.oneSpotPlan(cur,time)
            elif length == 2:
                self.twoSpotsPlan(cur, time)
            elif length == 3:
                self.triSpotsPlan(cur,time)
            else:
                QMessageBox.information(self, u"提示!", u"您想游览的景点太多啦~")
            self.reset()
            conn.commit()
            cur.close()
            conn.close()
    def save(self):
        u'''
        将地图截图保存成png图像，允许用户交互选择存储位置
        :return:
        '''
        savefile_path = QFileDialog.getSaveFileName(self,u'保存project',guiPath, "png(*.png)")
        if savefile_path is not None:
            p = QPixmap.grabWidget(self,QtCore.QRect(0, 80, 581, 421))
            p.save(savefile_path);

    def selectNearest(self,cur,spot):
        u'''
        根据景点名获得离它最近的景点
        :param cur: 游标
        :param spot: 景点名
        :return:
        '''
        str = "select * from scmLSG.relation where startName = '%s' or endName = '%s' order by roadTime;" % (spot,spot)
        cur.execute(str)
        relation_list = cur.fetchall()
        for i in range(len(relation_list)):
            tuple_temp = relation_list[i]
            nearspot,roadtime = self.searchSpot(tuple_temp,spot)
            if nearspot not in self.planList:
                break
                #self.planList.append(nearSpot)
                #self.plantime = self.plantime + roadtime
        return nearspot, roadtime

    def searchSpot(self,tuple,spot):
        u'''
        由于起点和终点的顺序可能相反，通过该函数找出不是输入点的另一个最近邻点
        :param tuple: 输入元组
        :param spot: 景点名
        :return:
        '''
        if unicode(tuple[1],"Utf-8") == spot:
            return unicode(tuple[2],"Utf-8"),tuple[3]
        elif unicode(tuple[2],"Utf-8") == spot:
            return unicode(tuple[1],"Utf-8"),tuple[3]

    def getticket(self,cur,spot):
        u'''
        从数据库中得到spot景点的票价
        :param cur:
        :param spot:
        :return:
        '''
        str = "select ticket from scmLSG.sceneInfo where sceneName = '%s';" % spot
        cur.execute(str)
        list = cur.fetchall()
        return list[0][0]

    def getvisitTime(self,cur,spot):
        u'''
        获得景点的推荐游览时间
        :param cur:
        :param spot:
        :return:
        '''
        str = "select visitTime from scmLSG.sceneInfo where sceneName = '%s'"% spot
        cur.execute(str)
        time_temp = cur.fetchall()
        time = time_temp[0][0]
        return time

    def changeHTML(self,planlist):
        u'''
        修改HTML,使得其显示景点表的驾车路线
        :param planlist:
        :return:
        '''
        if(len(planlist) > 2):
            #multipoint driving path
            str = '"%s"'%planlist[1]
            if len(planlist) > 3:
                for i in range (2,len(planlist)-1):
                    str = str + ',' + '"%s"'%planlist[i]
            f = open('routePlan.html', 'r+')
            flist = f.readlines()
            flist[26] = 'driving.search(p1, p2,{waypoints:[%s]});'%str.encode("utf-8")
            flist[23] = ''
            flist[22] = 'var p1 = "%s"\nvar p2 = "%s"\n'% (planlist[0].encode("utf-8"),planlist[-1].encode("utf-8"))
            f = open('routePlan_test.html', 'w+')
            f.writelines(flist)
            f.close()
            url_path = 'file:///' + guiPath + '/routePlan_test.html'
        elif(len(planlist) == 2):
            # two points driving path
            f = open('routePlan.html', 'r+')
            flist = f.readlines()
            flist[26] = 'driving.search(p1, p2);'
            flist[23] = ''
            flist[22] = 'var p1 = "%s"\nvar p2 = "%s"\n'% (planlist[0].encode("utf-8"),planlist[-1].encode("utf-8"))
            f = open('routePlan_test.html', 'w+')
            f.writelines(flist)
            f.close()
            url_path = 'file:///' + guiPath + '/routePlan_test.html'
        else:
            # one point search(No path)
            f = open('spot_search.html', 'r+')
            flist = f.readlines()
            flist[25] = '	local.search("%s");\n' % planlist[0].encode("utf-8")
            f = open('spotSearch_test.html', 'w+')
            f.writelines(flist)
            f.close()
            url_path = 'file:///' + guiPath + '/spotSearch_test.html'
        self.planView.setUrl(QUrl(url_path))
        self.planView.show()

    def oneSpotPlan(self, cur, whole_time):
        u'''
        单点联想搜索，并进行地图展示
        :param cur:
        :param whole_time:
        :return:
        '''
        list = self.spotList
        listindex = 0
        ticket = 0
        roadtime = 0
        self.planList.extend(list)
        while (self.plantime + self.getvisitTime(cur, self.planList[listindex]) <= whole_time):
            visittime = self.getvisitTime(cur, self.planList[listindex])
            self.plantime = self.plantime + visittime
            ticket = self.getticket(cur, self.planList[listindex]) + ticket
            nearspot, roadtime = self.selectNearest(cur, self.planList[listindex])
            self.planList.append(nearspot)
            self.plantime = self.plantime + roadtime
            listindex = listindex + 1
        # delete the last index of planlist because plantime is bigger than the time that user has set.
        del self.planList[-1]
        self.plantime = self.plantime - roadtime
        result1_str = u' -> '.join(self.planList)
        self.resultLabel.setText(u'规划结果：\n推荐景点游览顺序：%s\n预计游览时间：%s 小时\n预计平均花费：%s 元' % (result1_str, self.plantime, ticket))
        self.changeHTML(self.planList)



    def twoSpotsPlan(self,cur,time):
        u'''
        两点联想搜索
        :param cur:
        :param time:
        :return:
        '''
        visittime1 = self.getvisitTime(cur, self.spotList[0])
        visittime2 = self.getvisitTime(cur, self.spotList[1])
        roadtime = self.spotsRoadtime(cur, self.spotList[0], self.spotList[1])
        self.planList.extend(self.spotList)
        currenttime = visittime1 + visittime2 + roadtime
        if currenttime > time:
            QMessageBox.critical(self, u"警告!", u"计划时间内很难游览完景点！")
        else:
            temp1 = self.spotList[0]
            temp2 = self.spotList[1]
            list1 = [self.spotList[0]]
            list2 = [self.spotList[1]]
            ticket = self.getticket(cur, self.spotList[0]) + self.getticket(cur, self.spotList[1])
            while (1):
                nearest_1, roadtime_1 = self.selectNearest(cur, temp1)
                visittime1_1 = self.getvisitTime(cur, temp1)
                totaltime_1 = visittime1_1 + roadtime_1 + currenttime
                nearest_2, roadtime_2 = self.selectNearest(cur, temp2)
                visittime2_1 = self.getvisitTime(cur, temp2)
                totaltime_2 = visittime2_1 + roadtime_2 + currenttime
                # because the time is judged before iteration,there is no need to delete the last feature of planlist
                if ((totaltime_1 >= totaltime_2) and (totaltime_2 <= time)):
                    currenttime = totaltime_2
                    list2.append(nearest_2)
                    self.planList.append(nearest_2)
                    temp2 = nearest_2
                    ticket = self.getticket(cur, nearest_2) + ticket
                elif ((totaltime_1 < totaltime_2) and (totaltime_2 <= time)):
                    currenttime = totaltime_1
                    list2.append(nearest_1)
                    self.planList.append(nearest_2)
                    ticket = self.getticket(cur, nearest_1) + ticket
                    temp2 = nearest_1
                else:
                    break
            self.planList = list1 + list2
            self.changeHTML(self.planList)
            result = u' , '.join(self.planList)
            self.resultLabel.setText(u'规划结果：\n推荐游览景点：%s\n预计游览时间：%s 小时\n预计平均花费：%s 元' % (result, currenttime, ticket))

    def triSpotsPlan(self,cur,time):
        u'''
        三点联想搜索，做的不那么完善（尤其是导航部分），因此下面只写推荐景点，而不是路线
        :param cur:
        :param time:
        :return:
        '''
        self.planList.extend(self.spotList)
        visittime1 = self.getvisitTime(cur, self.spotList[0])
        visittime2 = self.getvisitTime(cur, self.spotList[1])
        visittime3 = self.getvisitTime(cur, self.spotList[2])
        roadtime_1 = self.spotsRoadtime(cur, self.spotList[0], self.spotList[1])
        roadtime_2 = self.spotsRoadtime(cur, self.spotList[1], self.spotList[2])
        roadtime_3 = self.spotsRoadtime(cur, self.spotList[2], self.spotList[0])
        roadtime = min(roadtime_1,roadtime_2,roadtime_3)
        currenttime = visittime1 + visittime2 + visittime3 + roadtime
        ticket = self.getticket(cur, self.spotList[0]) + self.getticket(cur, self.spotList[1]) + self.getticket(cur, self.spotList[2])
        if currenttime > time:
            QMessageBox.critical(self, u"警告!", u"计划时间内很难游览完景点！")
        else:
            temp = self.spotList
            list1 = [self.spotList[0]]
            list2 = [self.spotList[1]]
            list3 = [self.spotList[2]]
            listlist = [list1,list2,list3]
            # similiar to the function twoSpotsPlan()
            while (1):
                nearest_1, roadtime_1 = self.selectNearest(cur, temp[0])
                visittime1_1 = self.getvisitTime(cur, temp[0])
                totaltime_1 = visittime1_1 + roadtime_1 + currenttime
                nearest_2, roadtime_2 = self.selectNearest(cur, temp[1])
                visittime2_1 = self.getvisitTime(cur, temp[1])
                totaltime_2 = visittime2_1 + roadtime_2 + currenttime
                nearest_3, roadtime_3 = self.selectNearest(cur, temp[2])
                visittime3_1 = self.getvisitTime(cur, temp[2])
                totaltime_3 = visittime3_1 + roadtime_3 + currenttime
                nearest_list = [nearest_1,nearest_2,nearest_3]
                totaltime_list = [totaltime_1,totaltime_2,totaltime_3]
                min_value = min(totaltime_list)
                min_index = totaltime_list.index(min_value)
                if  totaltime_list[min_index] <= time:
                    currenttime = totaltime_list[min_index]
                    listlist[min_index].append(nearest_list[min_index])
                    temp[min_index] = nearest_list[min_index]
                    self.planList.append(nearest_list[min_index])
                    ticket = self.getticket(cur,nearest_list[min_index]) + ticket
                else:
                    break
            self.planList = list1 + list2 + list3
            self.changeHTML(self.planList)
            result = u' , '.join(self.planList)
            self.resultLabel.setText(u'规划结果：\n推荐游览景点：%s\n游览时间约%s 小时\n预计平均花费：%s 元' % (result, currenttime, ticket))

    def spotsRoadtime(self, cur, start, end):
        u'''
        获得两个地点之间的交通时间
        :param cur:
        :param start:
        :param end:
        :return:
        '''
        str = "select roadtime from scmLSG.relation where (startName = '%s' and endName = '%s') or (startName = '%s' and endName = '%s');" % (
        start, end, end, start)
        cur.execute(str)
        roadtime_list = cur.fetchall()
        roadtime = roadtime_list[0][0]
        return roadtime

    def getcurrentSpot(self,conn):
        u'''
        获得数据库景点表内现有景点名列表
        :param conn:
        :return:
        '''
        conn_temp = conn
        cur = conn_temp.cursor()
        str = "select distinct sceneName from scmLSG.sceneInfo;"
        cur.execute(str)
        name_list = cur.fetchall()
        spot_list = []
        for i in range(len(name_list)):
            name = name_list[i][0]
            u_name = unicode(name,"utf-8")
            spot_list.append(u_name)
        return spot_list

    def getConn(self,conn):
        self.conn_half = conn
        return conn