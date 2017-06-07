# -*- coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import QUrl
import sys,os
import random
import urllib

import halfautoRoute
import main_window
import comment
import spot

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


class mainWindow(QDialog, main_window.Ui_visitorWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        self.setupUi(self)
        # WebView initalization
        url_path = 'file:///' + guiPath + '\map_loading.html'
        self.webView.setUrl(QUrl(url_path))
        self.webView.show()
        # Map canvas initalization
        self.map_canvas = QgsMapCanvas()
        self.map_canvas.setCanvasColor(QColor(255,255,255))
        self.gridLayout_2.addWidget(self.map_canvas,0,0,1,1)
        self.layerList = []
        # "Plan" button initalization
        self.actionPoly = QAction("Polyline", self)
        self.actionPoly.setCheckable(True)
        self.connect(self.actionPoly, QtCore.SIGNAL(_fromUtf8("triggered()")), self.planRoutine)
        self.planButton.addAction(self.actionPoly)
        self.toolPoly = PlanMapTool(self.map_canvas)
        self.toolPoly.setAction(self.actionPoly)

        csspath = guiPath + '\\qss\\main_css.qss'
        file = QtCore.QFile(csspath)
        file.open(QtCore.QFile.ReadOnly)
        style_sheet = file.readAll()
        style_sheet = unicode(style_sheet, encoding='utf8')
        style1 = "QComboBox::down-arrow {image:url(%s/pic/jiantou.png);}\n"%guiUrl
        self.setStyleSheet(style_sheet+style1)

    def searchPlot(self):
        u'''
        通过筛选条件，进行数据库景点名的查询，并显示在地图上
        ：参数：无
        ：返回值：None
        '''
        conn_temp = self.conn_main
        cur = conn_temp.cursor()
        a=self.heatscene(cur)
        b=self.goodscene(cur)
        c=self.exscene(cur)
        conn_temp.commit()
        cur.close()
        tmp1=[val for val in a if val in b]
        tmp2=[val for val in tmp1 if val in c]
        multiSpotList = []
        for i in range(len(tmp2)):
            temp_tuple = tmp2[i]
            temp_str = temp_tuple[0]
            multiSpotList.append(temp_str)
        if multiSpotList == []:
            QMessageBox.critical(self, u"错误!", u"未找到合适的景点，数据库有待您的完善")
            return 1
        else:
            str = '"%s"' % multiSpotList[0]
            str2 = multiSpotList[0]
            for i in range(1, len(multiSpotList)):
                str = str + ',' + '"%s"' % multiSpotList[i]
                str2 = str2 + ',' + multiSpotList[i]
            self.spot_search_html(str)
            url_path = 'file:///' + guiPath + '/multiSpotSearch_test.html'
            self.webView.setUrl(QUrl(url_path))
            self.webView.show()
            QMessageBox.information(self, u"景点筛选结果!", u"筛选的结果为：%s"%unicode(str2,"utf-8"))

    def spot_search_html(self,a):
        u'''
        通过修改html文件来进行地图的搜索功能
        :param a:
        :return:
        '''
        f = open('multiSpotSearch.html', 'r+')
        flist = f.readlines()
        flist[22] = '    var myKeys = [%s];\n'%a
        f = open('multiSpotSearch_test.html', 'w+')
        f.writelines(flist)
        f.close()

    def heatscene(self,cur):
        u'''
        筛选热门冷门景区，采取景区内取前三名的方式
        :param cur:游标
        :return:
        '''
        if self.heatBox.currentText() == u'热门景区':
            #heatstr = "SELECT sceneName FROM scmLSG.uploadInfo;"
            heatstr = "SELECT sceneName from (SELECT sceneName,count(sceneName)  AS NUM FROM scmLSG.uploadInfo GROUP BY sceneName ORDER BY NUM DESC) AS BIAO LIMIT 3;"
            cur.execute(heatstr)
            heat = cur.fetchall()
            ifheat = heat
            return ifheat
        elif self.heatBox.currentText() == u'冷门景区':
            notheatstr = "SELECT sceneName from (SELECT sceneName,count(sceneName) AS NUM FROM scmLSG.uploadInfo GROUP BY sceneName ORDER BY NUM ASC) AS BIAO LIMIT 3;"
            cur.execute(notheatstr)
            notheat = cur.fetchall()
            ifheat=notheat
            return ifheat
        else:
            allstr = "SELECT DISTINCT sceneName FROM scmLSG.uploadInfo;"
            cur.execute(allstr)
            all = cur.fetchall()
            ifheat = all
            return ifheat

    def goodscene(self,cur):
        u'''
        筛选好评景区，采取取评价大于4的景区
        :param cur: 游标
        :return:
        '''
        if self.heatBox.currentText() == u'好评景区':
            goodstr = "SELECT sceneName from (SELECT sceneName,avg(rcmMark) AS MA FROM scmLSG.uploadInfo GROUP BY sceneName) AS GOOD WHERE GOOD.MA >=4;"
            cur.execute(goodstr)
            good = cur.fetchall()
            ifgood = good
            return ifgood
        else:
            allstr = "SELECT DISTINCT sceneName FROM scmLSG.uploadInfo;"
            cur.execute(allstr)
            all = cur.fetchall()
            ifgood = all
            return ifgood

    def exscene(self,cur):
        u'''
        选取收费或不收费景区，直接运用判断语句
        :param cur: 游标
        :return:
        '''
        if self.heatBox.currentText() == u'收费景区':
            expstr = "SELECT sceneName FROM scmLSG.sceneInfo WHERE ticket > 0;"
            cur.execute(expstr)
            exp = cur.fetchall()
            ifexp = exp
            return ifexp
        elif self.heatBox.currentText() == u'免费景区':
            notexpstr = "SELECT sceneName FROM scmLSG.sceneInfo WHERE ticket = 0;"
            cur.execute(notexpstr)
            notexp = cur.fetchall()
            ifexp = notexp
            return ifexp
        else:
            allstr = "SELECT DISTINCT sceneName FROM scmLSG.uploadInfo;"
            cur.execute(allstr)
            all = cur.fetchall()
            ifexp = all
            return ifexp

    def getConn(self,conn):
        u'''
        得到login.py中传递过来的conn
        :param conn:
        :return:
        '''
        self.conn_main = conn

    def getAccount(self,account):
        u'''
        得到login.py传递的用户名，并显示在main界面的最上方
        :param account:
        :return:
        '''
        print(type(account))
        self.label.setText(u'欢迎%s！让我们陪伴您，用不同的视野看世界！'%account)
        self.account = account
        print('account transform success')

    def openSpot(self):
        u'''
        在搜索框输入后，转换到spot页面，并进行conn,用户名和景点的参数传递
        :return: 如果出错，返回1，否则返回0
        '''
        spotList = self.getcurrentSpot(self.conn_main)
        try:
            if self.searchLine.text().strip() =='':
                QMessageBox.critical(self, u"错误!", u"请输入您想查看评价的地点")
                return 1
            elif self.searchLine.text() not in spotList:
                QMessageBox.critical(self, u"错误!", u"抱歉，数据库中暂无该景点，请输入全名或者更换景点")
                return 1
            else:
                self.openSpotwindow = spot.spotWindow()
                self.openSpotwindow.getConn(self.conn_main)
                self.openSpotwindow.getAccount(self.account)
                self.openSpotwindow.getSpot(self.searchLine.text())
                # rewrite the html to setURL
                self.openSpotwindow.spot_search_html(self.searchLine.text().encode("utf-8") )
                self.openSpotwindow.setSpotContent(self.conn_main)
                self.openSpotwindow.show()
                return 0
        except Exception,e:
            QMessageBox.critical(self, u"错误!", u"抱歉，数据库中暂无该景点的评价，欢迎点评")

    def addSpot(self):
        u'''
        添加地点
        :return:
        '''
        print('addSpot')

    def planRoutine(self):
        u'''
        进行鼠标交互操作，供用户绘制路线
        :return: 如果没加载底图，返回1，否则正常进行临时图层的描绘，无返回值
        '''
        if self.layerList==[]:
            QMessageBox.critical(self, u'错误!', u'请先选择底图格式!')
            return 1
        else:
            self.toolPoly.reset()
            self.map_canvas.setMapTool(self.toolPoly)

    def recommendRoutine(self):
        u'''
        根据用户所选时间，随机推荐路线，并显示在地图上
        :return: 如果没加载底图，返回1，否则显示随机推荐的路线，无返回值
        '''
        if self.layerList==[]:
            QMessageBox.critical(self, u'错误!', u'请先选择底图格式!')
        else:
            schema_name = 'recommendRoute'
            table_name = self.randSelectRoute(3)
            layer = self.addFile(table_name,schema_name)
            canvas_layer = QgsMapCanvasLayer(layer)
            layer_list_temp = self.layerList
            layer_list_temp.insert(0,canvas_layer)
            self.map_canvas.setLayerSet(layer_list_temp)
            self.map_canvas.zoomToFullExtent()

    def randSelectRoute(self,i):
        u'''
        随机选择数据库中存储的推荐路线
        :param i: 数据库内的可推荐路线数量
        :return: 返回数据库中的推荐路线表的名称
        '''
        text = self.visitTimeBox.currentText()
        if text == u'半天':
            flag = 2
        else:
            flag = 1
        r = random.randint(1,i)
        table_name = 'day'+ '_' + '%s'%flag + '_' + '%s'%r
        return table_name

    def addShp(self):
        u'''
        添加矢量底图（共两个图层，line&polygon）
        :return: 无返回值
        '''
        table1 = 'beijing_china_osm_line'
        table2 = 'beijing_china_osm_polygon'
        schema = 'basemap'
        layer1 = self.addFile(table1,schema)
        layer2 = self.addFile(table2,schema)
        self.canvas_layer1 = QgsMapCanvasLayer(layer1)
        self.canvas_layer2 = QgsMapCanvasLayer(layer2)
        self.layerList=[self.canvas_layer1,self.canvas_layer2]
        self.map_canvas.setLayerSet(self.layerList)
        self.map_canvas.zoomToFullExtent()

    def addFile(self, tablename, schema):
        u'''
        从数据库中加载layer
        :param tablename:数据库内表名
        :param schema:数据库内架构名
        :return:返回图层
        '''
        host = 'localhost'
        port = '5432'
        database = 'letsgo'
        user = 'admin'
        pswd = 'admin'
        column = 'geom'
        uri = QgsDataSourceURI()
        uri.setConnection(host, port, database, user, pswd)
        uri.setDataSource(schema, tablename, column)
        layer = QgsVectorLayer(uri.uri(), tablename, 'postgres')
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        return layer

    def addRas(self):
        u'''
        加载栅格图层，由于QGIS中无法导入tif，因此直接从project文件夹内读取
        :return:
        '''
        raster__file = guiPath + u'\\rasdata\\北京市_卫图_Level_11.tif'
        [path_file_name, file_ext] = os.path.splitext(raster__file)
        file_name = os.path.basename(raster__file)
        self.layer = QgsRasterLayer(raster__file, file_name)
        QgsMapLayerRegistry.instance().addMapLayer(self.layer)
        self.canvas_layer_ras = QgsMapCanvasLayer(self.layer)
        self.layerList=[self.canvas_layer_ras]
        self.map_canvas.setLayerSet(self.layerList)
        self.map_canvas.zoomToFullExtent()

    def saveRoute(self):
        u'''
        将canvas截图保存成png图像，允许用户交互选择存储位置
        :return:
        '''
        savefilePath = QFileDialog.getSaveFileName(self,u'保存project',guiPath, "png(*.png)")
        if savefilePath is not None:
            p = QPixmap.grabWidget(self,QtCore.QRect(15, 170, 670, 430))
            p.save(savefilePath);

    def loadRoute(self):
        u'''
        加载shp文件，并显示在画布上
        :return: 如果没加载底图，则返回1，否则无返回值
        '''
        if self.layerList==[]:
            QMessageBox.critical(self, u'错误!', u'请先选择底图格式!')
            return 1
        else:
            full_file = QFileDialog.getOpenFileName(self, u"打开路径文件", guiPath, "shapefile(*.shp)")
            file_name = os.path.basename(full_file)
            [path_file_name, file_ext] = os.path.splitext(full_file)
            layer_load = QgsVectorLayer(full_file, file_name, 'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(layer_load)
            canvas_layer_load = QgsMapCanvasLayer(layer_load)
            layer_list_temp = self.layerList
            layer_list_temp.insert(0,canvas_layer_load)
            self.map_canvas.setLayerSet(layer_list_temp)
            self.map_canvas.zoomToFullExtent()

    def openCommend(self):
        u'''
        根据搜索框的输入，打开评价页面，并传递conn和用户名
        :return:有错误，返回1，否则无返回值
        '''
        self.openCommendwindow = comment.commentWindow()
        self.openCommendwindow.getConn(self.conn_main)
        self.openCommendwindow.getAccount(self.account)
        spotList = self.getcurrentSpot(self.conn_main)
        if self.searchLine.text().strip() =='':
            QMessageBox.critical(self, u"错误!", u"请输入您想评价的地点!")
            return 1
        elif self.searchLine.text() not in spotList:
            QMessageBox.critical(self, u"错误!", u"抱歉，数据库中暂无该景点，请输入全名或者更换景点!")
            return 1
        else:
            self.openCommendwindow.getSpot(self.searchLine.text())
            self.openCommendwindow.show()

    def halfAutoPlan(self):
        self.halfWindow = halfautoRoute.halfautoWindow()
        self.halfWindow.show()
        self.halfWindow.getConn(self.conn_main)

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

class PlanMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberband = QgsRubberBand(self.canvas, QGis.Line)
        self.rubberband.reset()
        self.rubberband.setColor(QColor(255,0,0))
        self.rubberband.setWidth(1)
        self.point = None
        self.points = []

    def canvasPressEvent(self, e):
        u'''
        根据鼠标点击进行临时图层的绘制和实时显示
        :param e:鼠标操作指针
        :return:None
        '''
        self.point = self.toMapCoordinates(e.pos())
        m = QgsVertexMarker(self.canvas)
        m.setCenter(self.point)
        m.setColor(QColor(0,255,0))
        m.setIconSize(5)
        m.setIconType(QgsVertexMarker.ICON_NONE)
        m.setPenWidth(3)
        self.points.append(self.point)
        self.isEmittingPoint = True
        self.showPoly()

    def showPoly(self):
        u'''
        显示临时图层
        :return: 无返回值
        '''
        self.rubberband.reset(QGis.Line)
        for point in self.points[:-1]:
            self.rubberband.addPoint(point, False)
        self.rubberband.addPoint(self.points[-1], True)
        self.rubberband.show()

    def reset(self):
        u'''
        每一次单击按钮时，进行 rubberband 的重置。
        :return: None
        '''
        self.rubberband.reset()
        self.point = None
        self.points = []


