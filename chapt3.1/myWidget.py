# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication

from Ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    @pyqtSlot()
    def on_btnCalculate_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        num = int(self.ui.editCount.text())
        price = float(self.ui.editPrice.text())
        total = num * price
        self.ui.editTotal.setText("%.2f" %total)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())