# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication

from ui_Widget import Ui_Widget


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
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.slider.setMaximum(200)
        self.ui.scrollBar.setMaximum(200)
        self.ui.progressBar.setMaximum(200)

        self.ui.slider.valueChanged.connect(self.do_valueChanged)
        self.ui.scrollBar.valueChanged.connect(self.do_valueChanged)
    
    @pyqtSlot(bool)
    def on_chkBox_Visible_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.ui.progressBar.setTextVisible(checked)
    
    @pyqtSlot(bool)
    def on_chkBox_Inverted_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.ui.progressBar.setInvertedAppearance(checked)
    
    @pyqtSlot()
    def on_radio_Percent_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.progressBar.setFormat("%p%")
    
    @pyqtSlot()
    def on_radio_Value_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.progressBar.setFormat("%v")

    def do_valueChanged(self,value):
        self.ui.progressBar.setValue(value)

##  ============窗体测试程序 ===============================
if  __name__ == "__main__":         #用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form=QmyWidget()                #创建窗体
    form.show()
    sys.exit(app.exec_())