# -*- coding: utf-8 -*-

"""
Module implementing QmyMainWindow.
"""
import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QTreeWidgetItem, QLabel, QFileDialog, QDockWidget)

from enum import Enum

from PyQt5.QtCore import pyqtSlot, Qt, QDir, QFileInfo

from PyQt5.QtGui import QIcon, QPixmap

from ui_MainWindow import Ui_MainWindow

class TreeItemType(Enum):
    itTopItem = 1001
    itGroupItem = 1002
    itImageItem = 1003


class TreeColNum(Enum):
    colItem = 0
    colItemType = 1


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curPixmap = QPixmap()
        self.pixRatio = 1
        self.itemFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
                          | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate)
        self.setCentralWidget(self.ui.scrollArea)
        self.__iniTree()

        # 以下的属性设置在UI Designer里已经设置，这里是代码设置方法
        self.ui.dockWidget.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.ui.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.ui.scrollArea.setWidgetResizable(True)  # 自动调整内部组件大小
        self.ui.scrollArea.setAlignment(Qt.AlignCenter)
        self.ui.LabPicture.setAlignment(Qt.AlignCenter)

        ##  =================自定义功能函数================================

    def __iniTree(self):
        self.ui.treeFiles.clear()
        icon = QIcon(":/images/icons/15.ico")
        item = QTreeWidgetItem(TreeItemType.itTopItem.value)
        item.setIcon(TreeColNum.colItem.value, icon)
        item.setText(TreeColNum.colItem.value, "图片文件")
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value, Qt.Checked)

        item.setData(TreeColNum.colItem.value, Qt.UserRole, "")
        self.ui.treeFiles.addTopLevelItem(item)

    def __displayImage(self, item):
        filename = item.data(TreeColNum.colItem.value, Qt.UserRole)
        self.ui.statusBar.showMessage(filename)

        self.curPixmap.load(filename)
        self.on_actZoomFitH_triggered()

        self.ui.actZoomFitH.setEnabled(True)
        self.ui.actZoomFitW.setEnabled(True)
        self.ui.actZoomIn.setEnabled(True)
        self.ui.actZoomOut.setEnabled(True)
        self.ui.actZoomRealSize.setEnabled(True)

    def __changeItemCaption(self, item):
        title = "*" + item.text(TreeColNum.colItem.value)
        item.setText(TreeColNum.colItem.value, title)
        if (item.childCount() > 0):
            for i in range(item.childCount()):
                self.__changeItemCaption(item.child(i))

    ##  ===========connectSlotsByName() 自动连接的槽函数=================
    @pyqtSlot()
    def on_actTree_AddFolder_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dirStr = QFileDialog.getExistingDirectory()
        if (dirStr == ""):
            return
        parItem = self.ui.treeFiles.currentItem()
        if (parItem == None):
            parItem = self.ui.treeFiles.topLevelItem(0)

        icon = QIcon(":/images/icons/open3.bmp")

        dirObj = QDir(dirStr)
        nodeText = dirObj.dirName()

        item = QTreeWidgetItem(TreeItemType.itGroupItem.value)
        item.setIcon(TreeColNum.colItem.value, icon)
        item.setText(TreeColNum.colItem.value, nodeText)
        item.setText(TreeColNum.colItemType.value, "Group")
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value, Qt.Checked)

        item.setData(TreeColNum.colItem.value, Qt.UserRole, dirStr)
        parItem.addChild(item)
        parItem.setExpanded(True)

    @pyqtSlot()
    def on_actTree_AddFiles_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        fileList, flt = QFileDialog.getOpenFileNames(self,
                                                     "选择一个或多个文件", "", "Images(*.jpg)")
        if (len(fileList) < 1):
            return

        item = self.ui.treeFiles.currentItem()
        if (item.type() == TreeItemType.itImageItem.value):
            parItem = item.parent()
        else:
            parItem = item

        icon = QIcon(":/images/icons/31.ico")
        for i in range(len(fileList)):
            fullFileName = fileList[i]
            fileinfo = QFileInfo(fullFileName)
            nodeText = fileinfo.fileName()

            item = QTreeWidgetItem(TreeItemType.itImageItem.value)
            item.setIcon(TreeColNum.colItem.value, icon)
            item.setText(TreeColNum.colItem.value, nodeText)
            item.setText(TreeColNum.colItemType.value, "Image")
            item.setFlags(self.itemFlags)
            item.setCheckState(TreeColNum.colItem.value, Qt.Checked)

            item.setData(TreeColNum.colItem.value, Qt.UserRole, fullFileName)
            parItem.addChild(item)

        parItem.setExpanded(True)

    @pyqtSlot()
    def on_actTree_DeleteItem_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        item = self.ui.treeFiles.currentItem()
        parItem = item.parent()
        parItem.removeChild(item)

    @pyqtSlot()
    def on_actTree_ScanItems_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        count = self.ui.treeFiles.topLevelItemCount()
        for i in range(count):
            item = self.ui.treeFiles.topLevelItem(i)
            self.__changeItemCaption(item)


    def on_treeFiles_currentItemChanged(self, current, previous):

        # TODO: not implemented yet
        if(current==None):
            return
        nodeType=current.type()

        if(nodeType==TreeItemType.itTopItem.value):
            self.ui.actTree_AddFolder.setEnabled(True)
            self.ui.actTree_AddFiles.setEnabled(True)
            self.ui.actTree_DeleteItem.setEnabled(False)

        elif(nodeType==TreeItemType.itGroupItem.value):
            self.ui.actTree_AddFolder.setEnabled(True)
            self.ui.actTree_AddFiles.setEnabled(True)
            self.ui.actTree_DeleteItem.setEnabled(True)

        elif(nodeType==TreeItemType.itImageItem.value):
            self.ui.actTree_AddFolder.setEnabled(False)
            self.ui.actTree_AddFiles.setEnabled(True)
            self.ui.actTree_DeleteItem.setEnabled(True)
            self.__displayImage(current)

    @pyqtSlot()
    def on_actZoomFitH_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        H = self.ui.scrollArea.height()
        realH = self.curPixmap.height()
        self.pixRatio = float(H) / realH
        pix = self.curPixmap.scaledToHeight(H - 30)
        self.ui.LabPicture.setPixmap(pix)

    @pyqtSlot()
    def on_actZoomFitW_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        W = self.ui.scrollArea.width() - 20
        realW = self.curPixmap.width()
        self.pixRatio = float(W) / realW
        pix = self.curPixmap.scaledToWidth(W - 30)
        self.ui.LabPicture.setPixmap(pix)

    @pyqtSlot()  ##实际大小
    def on_actZoomRealSize_triggered(self):
        self.pixRatio = 1  # 恢复显示比例为1
        self.ui.LabPicture.setPixmap(self.curPixmap)

    @pyqtSlot()
    def on_actZoomIn_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.pixRatio = self.pixRatio * 1.2
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.LabPicture.setPixmap(pix)

    @pyqtSlot()
    def on_actZoomOut_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.pixRatio = self.pixRatio * 0.8
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.LabPicture.setPixmap(pix)

    @pyqtSlot(bool)
    def on_actDockFloat_triggered(self, checked):
        self.ui.dockWidget.setFloating(checked)

    @pyqtSlot(bool)
    def on_dockWidget_topLevelChanged(self, topLevel):
        self.ui.actDockFloat.setChecked(topLevel)

    @pyqtSlot(bool)  ##设置停靠区可见性
    def on_actDockVisible_triggered(self, checked):
        self.ui.dockWidget.setVisible(checked)

    @pyqtSlot(bool)
    def on_dockWidget_visibilityChanged(self, visible):
        self.ui.actDockVisible.setChecked(visible)

##  ===========窗体测试程序=================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
