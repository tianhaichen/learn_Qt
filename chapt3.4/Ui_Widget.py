# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\PycharmProjects\pythonProject\learn_Qt\chapt3.4\Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(600, 307)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnGetTime.setObjectName("btnGetTime")
        self.gridLayout.addWidget(self.btnGetTime, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(20, 23, 0)))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 2, 1, 1)
        self.editTime = QtWidgets.QLineEdit(self.groupBox)
        self.editTime.setObjectName("editTime")
        self.gridLayout.addWidget(self.editTime, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 2, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 2), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 2, 2, 1)
        self.btnSetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetTime.setObjectName("btnSetTime")
        self.gridLayout.addWidget(self.btnSetTime, 2, 3, 1, 1)
        self.editDate = QtWidgets.QLineEdit(self.groupBox)
        self.editDate.setObjectName("editDate")
        self.gridLayout.addWidget(self.editDate, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 2), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 4, 2, 1, 1)
        self.btnSetDate = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDate.setObjectName("btnSetDate")
        self.gridLayout.addWidget(self.btnSetDate, 4, 3, 1, 1)
        self.editDateTime = QtWidgets.QLineEdit(self.groupBox)
        self.editDateTime.setObjectName("editDateTime")
        self.gridLayout.addWidget(self.editDateTime, 5, 3, 1, 1)
        self.btnSetDateTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDateTime.setObjectName("btnSetDateTime")
        self.gridLayout.addWidget(self.btnSetDateTime, 6, 3, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.editCalendar = QtWidgets.QLineEdit(self.groupBox_2)
        self.editCalendar.setObjectName("editCalendar")
        self.gridLayout_2.addWidget(self.editCalendar, 0, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "日期时间"))
        self.groupBox.setTitle(_translate("Widget", "日期时间"))
        self.btnGetTime.setText(_translate("Widget", "读取当前日期时间"))
        self.label_4.setText(_translate("Widget", "字符串显示"))
        self.label.setText(_translate("Widget", "时   间"))
        self.timeEdit.setDisplayFormat(_translate("Widget", "HH:mm:ss"))
        self.editTime.setInputMask(_translate("Widget", "99:99:99;_"))
        self.label_2.setText(_translate("Widget", "日   期"))
        self.dateEdit.setDisplayFormat(_translate("Widget", "yyyy年M月d日"))
        self.btnSetTime.setText(_translate("Widget", "设置时间"))
        self.editDate.setInputMask(_translate("Widget", "9999-99-99"))
        self.label_3.setText(_translate("Widget", "日期时间"))
        self.btnSetDate.setText(_translate("Widget", "设置日期"))
        self.editDateTime.setInputMask(_translate("Widget", "9999-99-99 99:99:99"))
        self.btnSetDateTime.setText(_translate("Widget", "设置日期时间"))
        self.groupBox_2.setTitle(_translate("Widget", "日历选择"))
        self.label_5.setText(_translate("Widget", "选择的日期："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
