# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""
import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QApplication

from Ui_Widget import Ui_Widget


class QmyWidget(QWidget, Ui_Widget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(QmyWidget, self).__init__(parent)
        self.ui=Ui_Widget()
        self.ui.setupUi(self)
    
    @pyqtSlot()
    def on_btnAlign_Left_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.editInput.setAlignment(Qt.AlignLeft)
    
    @pyqtSlot()
    def on_btnAlign_Center_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.editInput.setAlignment(Qt.AlignCenter)
    
    @pyqtSlot()
    def on_btnAlign_Right_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.editInput.setAlignment(Qt.AlignRight)
    
    @pyqtSlot(bool)
    def on_btnFont_Bold_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        font = self.ui.editInput.font()
        font.setBold(checked)
        self.ui.editInput.setFont(font)
    
    @pyqtSlot(bool)
    def on_btnFont_Italic_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        font = self.ui.editInput.font()
        font.setItalic(checked)
        self.ui.editInput.setFont(font)
    
    @pyqtSlot(bool)
    def on_btnFont_UnderLine_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        font = self.ui.editInput.font()
        font.setUnderline(checked)
        self.ui.editInput.setFont(font)
    
    @pyqtSlot(bool)
    def on_chkBox_Readonly_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.editInput.setReadOnly(checked)
    
    @pyqtSlot(bool)
    def on_chkbox_Enable_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.editInput.setEnabled(checked)
    
    @pyqtSlot(bool)
    def on_chkBox_ClearButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.editInput.setClearButtonEnabled(checked)

##  ============窗体测试程序 ===============================
if  __name__ == "__main__":         #用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form=QmyWidget()                #创建窗体
    form.show()
    sys.exit(app.exec_())