# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\PycharmProjects\pythonProject\learn_Qt\chapt3.5\Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(255, 245)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btnStart = QtWidgets.QPushButton(self.groupBox)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 0, 0, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.groupBox)
        self.btnStop.setEnabled(False)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 0, 1, 1, 1)
        self.btnSetIntv = QtWidgets.QPushButton(self.groupBox)
        self.btnSetIntv.setObjectName("btnSetIntv")
        self.gridLayout.addWidget(self.btnSetIntv, 1, 0, 1, 1)
        self.spinBoxIntv = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxIntv.setMaximum(99000000)
        self.spinBoxIntv.setProperty("value", 1000)
        self.spinBoxIntv.setObjectName("spinBoxIntv")
        self.gridLayout.addWidget(self.spinBoxIntv, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LCDHour = QtWidgets.QLCDNumber(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LCDHour.setFont(font)
        self.LCDHour.setDigitCount(2)
        self.LCDHour.setProperty("value", 10.0)
        self.LCDHour.setObjectName("LCDHour")
        self.horizontalLayout.addWidget(self.LCDHour)
        self.LCDMin = QtWidgets.QLCDNumber(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LCDMin.setFont(font)
        self.LCDMin.setDigitCount(2)
        self.LCDMin.setProperty("value", 26.0)
        self.LCDMin.setObjectName("LCDMin")
        self.horizontalLayout.addWidget(self.LCDMin)
        self.LCDSec = QtWidgets.QLCDNumber(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LCDSec.setFont(font)
        self.LCDSec.setDigitCount(2)
        self.LCDSec.setProperty("value", 15.0)
        self.LCDSec.setObjectName("LCDSec")
        self.horizontalLayout.addWidget(self.LCDSec)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.LabElapsedTime = QtWidgets.QLabel(Widget)
        self.LabElapsedTime.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabElapsedTime.setFont(font)
        self.LabElapsedTime.setObjectName("LabElapsedTime")
        self.verticalLayout.addWidget(self.LabElapsedTime)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "定时器"))
        self.groupBox.setTitle(_translate("Widget", "定时器"))
        self.btnStart.setText(_translate("Widget", "开始"))
        self.btnStop.setText(_translate("Widget", "停止"))
        self.btnSetIntv.setText(_translate("Widget", "设置周期"))
        self.spinBoxIntv.setSuffix(_translate("Widget", " ms"))
        self.groupBox_2.setTitle(_translate("Widget", "当前时间（小时：分：秒）"))
        self.LabElapsedTime.setText(_translate("Widget", "流逝的时间"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Widget = QtWidgets.QWidget()
#     ui = Ui_Widget()
#     ui.setupUi(Widget)
#     Widget.show()
#     sys.exit(app.exec_())
