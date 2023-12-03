# -*- coding: utf-8 -*-

"""
Module implementing QmyMainWindow.
"""
import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QProgressBar, QSpinBox, QFontComboBox, QActionGroup)
from PyQt5.QtGui import QFont
from ui_MainWindow import Ui_MainWindow


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

        self.__buildUI()
        self.__spinFontSize.valueChanged[int].connect(self.do_fontSize_Changed)
        self.__comboFontName.currentIndexChanged[str].connect(self.do_fontName_Changed)
        self.setCentralWidget(self.ui.textEdit)

    ##  ============自定义功能函数================================
    def __buildUI(self):
        self.__labFile = QLabel(self)
        self.__labFile.setMinimumWidth(150)
        self.__labFile.setText("文件名： ")
        self.ui.statusBar.addWidget(self.__labFile)

        self.__progressBar1 = QProgressBar(self)
        self.__progressBar1.setMaximumWidth(200)
        self.__progressBar1.setMinimum(5)
        self.__progressBar1.setMaximum(50)
        sz = self.ui.textEdit.font().pointSize()
        self.__progressBar1.setValue(sz)
        self.ui.statusBar.addWidget(self.__progressBar1)

        self.__LabInfo = QLabel(self)
        self.__LabInfo.setText("选择字体名称： ")
        self.ui.statusBar.addPermanentWidget(self.__LabInfo)

        actionGroup = QActionGroup(self)
        actionGroup.addAction(self.ui.actLang_CN)
        actionGroup.addAction(self.ui.actLang_EN)
        actionGroup.setExclusive(True)
        self.ui.actLang_CN.setChecked(True)

        self.__spinFontSize = QSpinBox(self)
        self.__spinFontSize.setMinimum(5)
        self.__spinFontSize.setMaximum(50)
        sz = self.ui.textEdit.font().pointSize()
        self.__spinFontSize.setValue(sz)
        self.__spinFontSize.setMinimumWidth(50)
        self.ui.mainToolBar.addWidget(self.__spinFontSize)

        self.__comboFontName = QFontComboBox(self)
        self.__comboFontName.setMinimumWidth(100)
        self.ui.mainToolBar.addWidget(self.__comboFontName)

        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actClose)

    @pyqtSlot()
    def on_actFile_New_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.__labFile.setText(" 新建文件 ")

    @pyqtSlot()
    def on_actFile_Open_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.__labFile.setText(" 打开的文件 ")

    @pyqtSlot()
    def on_actFile_Save_triggered(self):
        """
               Slot documentation goes here.
               """
        # TODO: not implemented yet
        self.__labFile.setText(" 文件已保存 ")


    @pyqtSlot(bool)
    def on_actFont_Bold_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        fmt = self.ui.textEdit.currentCharFormat()
        if(checked==True):
            fmt.setFontWeight(QFont.Bold)
        else:
            fmt.setFontWeight(QFont.Normal)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def on_actFont_Italic_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def on_actFont_UnderLine_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)

    def on_textEdit_copyAvaliable(self,avi):
        self.ui.actEdit_Cut.setEnabled(avi)
        self.ui.actEdit_Copy.setEnabled(avi)
        self.ui.actEdit_Paste.setEnabled(self.ui.textEdit.canPaste())

    def on_textEdit_selectionChanged(self):
        fmt=self.ui.textEdit.currentCharFormat()
        self.ui.actFont_Bold.setChecked(fmt.font().bold())
        self.ui.actFont_Italic.setChecked(fmt.fontItalic())
        self.ui.actFont_UnderLine.setChecked(fmt.fontUnderline())

    def on_textEdit_customContextMenuRequested(self,pos):
        popMenu=self.ui.textEdit.createStandardContextMenu()
        popMenu.exec_(pos)

    @pyqtSlot(bool)
    def on_actSys_ToggleText_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        if(checked):
            st=Qt.ToolButtonTextUnderIcon
        else:
            st=Qt.ToolButtonIconOnly
        self.ui.mainToolBar.setToolButtonStyle(st)

    @pyqtSlot(int)
    def do_fontSize_Changed(self,fontSize):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontPointSize(fontSize)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
        self.__progressBar1.setValue(fontSize)

    @pyqtSlot(str)
    def do_fontName_Changed(self,fontName):
        fmt=self.ui.textEdit.currentCharFormat()
        fmt.setFontFamily(fontName)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
        self.__LabInfo.setText("字体名称：%s   "%fontName)

##  ===========窗体测试程序=================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
