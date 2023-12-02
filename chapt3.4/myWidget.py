# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""
import sys
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate, QTime
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
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_btnGetTime_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        curDateTime = QDateTime.currentDateTime()
        self.ui.timeEdit.setTime(curDateTime.time())
        self.ui.editTime.setText(curDateTime.toString("hh:mm:ss"))

        self.ui.dateEdit.setDate(curDateTime.date())
        self.ui.editDate.setText(curDateTime.toString("yyyy-MM-dd"))

        self.ui.dateTimeEdit.setDateTime(curDateTime)
        self.ui.editDateTime.setText(curDateTime.toString("yyyy-MM-dd hh:mm:ss"))

    @pyqtSlot()
    def on_btnSetTime_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        tmStr = self.ui.editTime.text()
        tm = QTime.fromString(tmStr, "hh:mm:ss")
        self.ui.timeEdit.setTime(tm)

    @pyqtSlot()
    def on_btnSetDate_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dtStr = self.ui.editDate.text()
        dt = QDate.fromString(dtStr, "yyyy-MM-dd")
        self.ui.dateEdit.setDate(dt)

    @pyqtSlot()
    def on_btnSetDateTime_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dttmStr = self.ui.editDateTime.text()
        dttm = QDateTime.fromString(dttmStr, "yyyy-MM-dd hh:mm:ss")
        self.ui.dateTimeEdit.setDateTime(dttm)

    @pyqtSlot()
    def on_calendarWidget_selectionChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        date = self.ui.calendarWidget.selectedDate()
        self.ui.editCalendar.setText(date.toString("yyyy年M月d日"))


##  ============窗体测试程序 ===============================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWidget()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
