# -*- coding: utf-8 -*-

"""
Module implementing QmyMainWindow.
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QLabel, QTableWidgetItem, QAbstractItemView)
from enum import Enum
from PyQt5.QtCore import pyqtSlot, Qt, QDate

from PyQt5.QtGui import QFont, QBrush, QIcon

from ui_MainWindow import Ui_MainWindow


class CellType(Enum):  ##各单元格的类型
    ctName = 1000
    ctSex = 1001
    ctBirth = 1002
    ctNation = 1003
    ctScore = 1004
    ctPartyM = 1005


class FieldColNum(Enum):  ##各字段在表格中的列号
    colName = 0
    colSex = 1
    colBirth = 2
    colNation = 3
    colScore = 4
    colPartyM = 5


class QmyMainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Demo3_10,QTableWidget的使用")

        self.LabCellIndex = QLabel("当前单元格坐标：", self)
        self.LabCellIndex.setMinimumWidth(250)
        self.LabCellType = QLabel("当前单元格类型:", self)
        self.LabCellType.setMinimumWidth(200)
        self.LabStudID = QLabel("学生ID：", self)
        self.LabStudID.setMinimumWidth(200)

        self.ui.statusBar.addWidget(self.LabCellIndex)  # 加到状态栏
        self.ui.statusBar.addWidget(self.LabCellType)
        self.ui.statusBar.addWidget(self.LabStudID)

        self.ui.tableInfo.setAlternatingRowColors(True)
        self.__tableInitialized = False

    ##  ==============自定义功能函数============
    def __createItemsARow(self, rowNo, name, sex, birth, nation, isParty, score):
        StudID = 201805000 + rowNo  # 学号

        # 姓名
        item = QTableWidgetItem(name, CellType.ctName.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        item.setData(Qt.UserRole, StudID)
        self.ui.tableInfo.setItem(rowNo, FieldColNum.colName.value, item)

        # 性别
        if (sex == "男"):
            icon = QIcon(":/icons/images/boy.ico")
        else:
            icon = QIcon(":/icons/images/girl.ico")
        item = QTableWidgetItem(sex, CellType.ctSex.value)
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.tableInfo.setItem(rowNo, FieldColNum.colSex.value, item)

        # 出生日期
        strBirth = birth.toString("yyyy-MM-dd")
        item = QTableWidgetItem(strBirth, CellType.ctBirth.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.tableInfo.setItem(rowNo, FieldColNum.colBirth.value, item)

        # 民族
        item = QTableWidgetItem(nation, CellType.ctNation.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if (nation != "汉族"):
            item.setForeground(QBrush(Qt.blue))
        self.ui.tableInfo.setItem(rowNo, FieldColNum.colNation.value, item)

        # 分数
        strScore = str(score)
        item = QTableWidgetItem(strScore, CellType.ctScore.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.tableInfo.setItem(rowNo, FieldColNum.colScore.value, item)

        # 党员
        item = QTableWidgetItem("党员", CellType.ctPartyM.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if (isParty == True):
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)  # 不允许编辑文字
        item.setBackground(QBrush(Qt.yellow))  # Qt::green  lightGray  yellow
        self.ui.tableInfo.setItem(rowNo, FieldColNum.colPartyM.value, item)  # 为单元格设置Item

    ##  ==========由connectSlotsByName() 自动连接的槽函数==================
    @pyqtSlot()
    def on_btnSetHeader_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        headerText = ["姓 名", "性 别", "出生日期", "民 族", "分数", "是否党员"]
        self.ui.tableInfo.setColumnCount(len(headerText))

        for i in range(len(headerText)):
            headerItem = QTableWidgetItem(headerText[i])
            font = headerItem.font()
            font.setPointSize(11)
            headerItem.setFont(font)
            headerItem.setForeground(QBrush(Qt.red))
            self.ui.tableInfo.setHorizontalHeaderItem(i, headerItem)

    @pyqtSlot()  ##设置行数
    def on_btnSetRows_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.tableInfo.setRowCount(self.ui.spinRowCount.value())  # 设置数据区行数
        self.ui.tableInfo.setAlternatingRowColors(self.ui.chkBoxRowColor.isChecked())  # 设置交替行背景颜色

    @pyqtSlot()  ##初始化表格数据
    def on_btnIniData_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.tableInfo.clearContents()

        birth = QDate(1998, 6, 24)
        isParty = True
        nation = "汉族"
        score = 70

        rowCount = self.ui.tableInfo.rowCount()
        for i in range(rowCount):
            strName = "学生%d" % i
            if ((i % 2) == 0):
                strSex = "男"
            else:
                strSex = "女"
            self.__createItemsARow(i, strName, strSex,
                                   birth, nation, isParty, score)
            birth = birth.addDays(20)
            isParty = not isParty

        self.__tableInitialized = True

    @pyqtSlot()##插入行
    def on_btnInsertRow_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        curRow = self.ui.tableInfo.currentRow()
        self.ui.tableInfo.insertRow(curRow)
        birth = QDate.fromString("1998-4-5", "yyyy-M-d")
        self.__createItemsARow(curRow,"新学生", "男", birth, "苗族", True, 65)

    @pyqtSlot()##添加行
    def on_btnAppendRow_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        curRow = self.ui.tableInfo.rowCount()
        self.ui.tableInfo.insertRow(curRow)
        birth = QDate.fromString("1999-1-10", "yyyy-M-d")
        self.__createItemsARow(curRow,"新生", " 女", birth, "土家族", False, 86)

    @pyqtSlot()
    def on_btnDelCurRow_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        curRow = self.ui.tableInfo.currentRow()
        self.ui.tableInfo.removeRow(curRow)

    @pyqtSlot()
    def on_btnClearContents_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.tableInfo.clearContents()

    @pyqtSlot()
    def on_btnAutoHeight_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.tableInfo.resizeRowsToContents()

    @pyqtSlot()
    def on_btnAutoWidth_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.tableInfo.resizeColumnsToContents()

    @pyqtSlot(bool)  ##表格可编辑
    def on_chkBoxEditable_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        if(checked):
            trig=QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked
        else:
            trig = QAbstractItemView.NoEditTriggers
        self.ui.tableInfo.setEditTriggers(trig)

    @pyqtSlot(bool)  ##交替行颜色
    def on_chkBoxRowColor_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.ui.tableInfo.setAlternatingRowColors(checked)

    @pyqtSlot(bool)##是否显示水平表头
    def on_chkBoxHeaderH_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.ui.tableInfo.horizontalHeader().setVisible(checked)

    @pyqtSlot(bool)# 是否显示垂直表头
    def on_chkBoxHeaderV_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.ui.tableInfo.verticalHeader().setVisible(checked)

    @pyqtSlot()##选择行为：行选择
    def on_radioSelectRow_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        selMode = QAbstractItemView.SelectRows
        self.ui.tableInfo.setSelectionBehavior(selMode)

    @pyqtSlot()##选择行为：单元格选择
    def on_radioSelectItem_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        selMode = QAbstractItemView.SelectItems
        self.ui.tableInfo.setSelectionBehavior(selMode)

    @pyqtSlot()##读取表格到文本
    def on_btnReadToText_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.textEdit.clear()
        rowCount = self.ui.tableInfo.rowCount()
        colCount = self.ui.tableInfo.columnCount()
        for i in range(rowCount):
            strText = "第 %d 行： " % (i + 1)
            for j in range(colCount-1):
                cellItem = self.ui.tableInfo.item(i,j)
                strText=strText+cellItem.text()+"   "
            cellItem = self.ui.tableInfo.item(i,colCount-1)
            if(cellItem.checkState()==Qt.Checked):
                strText=strText+"党员"
            else:
                strText = strText + "群众"
            self.ui.textEdit.appendPlainText(strText)

    @pyqtSlot(int, int, int, int)##当前单元格发生变化
    def on_tableInfo_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (self.__tableInitialized == False):
            return
        item = self.ui.tableInfo.item(currentRow, currentColumn)
        if (item == None):
            return

        self.LabCellIndex.setText("当前单元格：%d 行，%d 列"
                                  % (currentRow, currentColumn))
        itemCellType = item.type()
        self.LabCellType.setText("当前单元格类型：%d" % itemCellType)

        item2 = self.ui.tableInfo.item(currentRow, FieldColNum.colName.value)
        stuID = item2.data(Qt.UserRole)
        self.LabStudID.setText("学生ID:%d" % stuID)





##  ===========窗体测试程序=================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
