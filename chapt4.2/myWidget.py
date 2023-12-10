# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""
import sys

from PyQt5.QtCore import pyqtSlot, QStringListModel,Qt
from PyQt5.QtWidgets import QWidget,QApplication,QAbstractItemView

from ui_myWidget import Ui_Widget


class QmyWidget(QWidget, Ui_Widget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(QmyWidget, self).__init__(parent)
        self.ui=Ui_Widget()
        self.ui.setupUi(self)

        self.__provinces=["北京","上海","天津","河北",
                       "山东","四川","重庆","广东","河南"]

        self.model = QStringListModel(self)
        self.model.setStringList(self.__provinces)
        self.ui.listView.setModel(self.model)

        self.ui.listView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)


    @pyqtSlot()
    def on_btnList_Reset_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.model.setStringList(self.__provinces)
    
    @pyqtSlot()
    def on_btnList_Append_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        lastRow=self.model.rowCount()
        self.model.insertRow(lastRow)
        index = self.model.index(lastRow,0)
        self.model.setData(index,"new item",Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)

    
    @pyqtSlot()
    def on_btnList_Insert_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        index = self.ui.listView.currentIndex()
        self.model.insertRow(index.row())
        self.model.setData(index,"inserted item",Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)
    
    @pyqtSlot()
    def on_btnList_Delete_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        index = self.ui.listView.currentIndex()
        self.model.removeRow(index.row())
    
    @pyqtSlot()
    def on_btnList_Clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        count=self.model.rowCount()
        self.model.removeRows(0,count)

    @pyqtSlot()
    def on_btnText_Clear_clicked(self):
        self.ui.plainTextEdit.clear()

    def on_listView_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        self.ui.LabInfo.setText("当前项index: row=%d, column=%d"
                             %(index.row(),index.column()))
    def on_btnText_Display_clicked(self):
        strList=self.model.stringList()
        self.ui.plainTextEdit.clear()
        for strLine in strList:
            self.ui.plainTextEdit.appendPlainText(strLine)

##  ============窗体测试程序 ===============================
if  __name__ == "__main__":         #用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form=QmyWidget()                #创建窗体
    form.show()
    sys.exit(app.exec_())