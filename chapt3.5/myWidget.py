# -*- coding: utf-8 -*-

"""
Module implementing QmyWidget.
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtCore import pyqtSlot
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

        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.do_timer_timeout)

        self.counter = QTime()

    @pyqtSlot()
    def on_btnStart_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.timer.start()
        self.counter.start()

        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        self.ui.btnSetIntv.setEnabled(False)

    @pyqtSlot()
    def on_btnStop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.timer.stop()
        tmMs = self.counter.elapsed()  # 计时器流逝的毫秒数

        ms = tmMs % 1000
        sec = tmMs / 1000
        timeStr = "流逝的时间：%d 秒，%d 毫秒" % (sec, ms)
        self.ui.LabElapsedTime.setText(timeStr)

        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnSetIntv.setEnabled(True)

    @pyqtSlot()
    def on_btnSetIntv_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.timer.setInterval(self.ui.spinBoxIntv.value())

    ##  ==========自定义槽函数==================================
    def do_timer_timeout(self):
        curTime = QTime.currentTime()
        self.ui.LCDHour.display(curTime.hour())
        self.ui.LCDMin.display(curTime.minute())
        self.ui.LCDSec.display(curTime.second())


##  ============窗体测试程序 ===============================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWidget()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
