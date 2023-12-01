# -*- coding: utf-8 -*-

"""
Module implementing Widget.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication

from Ui_Widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Widget, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btnCalculate_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Widget()
    ui.show()
    sys.exit(app.exec_())