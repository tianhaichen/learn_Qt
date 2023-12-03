# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
from ui_Widget import Ui_Widget


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
        super(QmyWidget, self).__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_btnIniItems_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        icon = QIcon(":/icons/images/aim.ico")
        self.ui.comboBox.clear()
        provinces = ["山东", "河北", "河南", "湖北", "湖南", "广东"]
        for i in range(len(provinces)):
            self.ui.comboBox.addItem(icon, provinces[i])

    @pyqtSlot()
    def on_btnClearItems_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.ui.comboBox.clear()

    @pyqtSlot(bool)
    def on_chkBoxEditable_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.ui.comboBox.setEditable(checked)

    @pyqtSlot(str)
    def on_comboBox_currentIndexChanged(self, curText):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.ui.lineEdit.setText(curText)

    @pyqtSlot()
    def on_btnIni2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        icon = QIcon(":/icons/images/unit.ico")
        self.ui.comboBox2.clear()
        cities = {"北京": 10, "上海": 21, "天津": 22,
                  "徐州": 516, "福州": 591, "青岛": 532}
        for k in cities:
            self.ui.comboBox2.addItem(icon, k, cities[k])

    @pyqtSlot(str)
    def on_comboBox2_currentTextChanged(self, curText):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.ui.lineEdit.setText(curText)
        zone = self.ui.comboBox2.currentData()
        if (zone != None):
            self.ui.lineEdit.setText(curText + ":区号=%d" % zone)


##  ============窗体测试程序 ===============================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWidget()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
