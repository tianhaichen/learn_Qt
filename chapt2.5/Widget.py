# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(393, 266)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(Widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sliderSetAge = QtWidgets.QSlider(self.groupBox)
        self.sliderSetAge.setMaximum(100)
        self.sliderSetAge.setProperty("value", 50)
        self.sliderSetAge.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSetAge.setObjectName("sliderSetAge")
        self.gridLayout.addWidget(self.sliderSetAge, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editAgeInt = QtWidgets.QLineEdit(self.groupBox)
        self.editAgeInt.setObjectName("editAgeInt")
        self.gridLayout.addWidget(self.editAgeInt, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.editAgeStr = QtWidgets.QLineEdit(self.groupBox)
        self.editAgeStr.setObjectName("editAgeStr")
        self.gridLayout.addWidget(self.editAgeStr, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.editNameInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.editNameInput.setObjectName("editNameInput")
        self.gridLayout_2.addWidget(self.editNameInput, 0, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 2)
        self.editNameHello = QtWidgets.QLineEdit(self.groupBox_2)
        self.editNameHello.setObjectName("editNameHello")
        self.gridLayout_2.addWidget(self.editNameHello, 1, 2, 1, 2)
        self.btnSetName = QtWidgets.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/images/322.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetName.setIcon(icon1)
        self.btnSetName.setChecked(False)
        self.btnSetName.setObjectName("btnSetName")
        self.gridLayout_2.addWidget(self.btnSetName, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(Widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem1 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Widget)
        self.btnClose.clicked.connect(Widget.close)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "资源文件、自定义信号"))
        self.groupBox.setTitle(_translate("Widget", "年龄设置"))
        self.label.setText(_translate("Widget", "设置年龄(0~100)"))
        self.label_2.setText(_translate("Widget", "ageChanged(int)响应"))
        self.label_3.setText(_translate("Widget", "ageChanged(str)响应"))
        self.groupBox_2.setTitle(_translate("Widget", "姓名设置"))
        self.label_4.setText(_translate("Widget", "输入姓名"))
        self.editNameInput.setInputMask(_translate("Widget", "Mike"))
        self.label_5.setText(_translate("Widget", "nameChanged(str)响应"))
        self.btnSetName.setText(_translate("Widget", "设置姓名"))
        self.btnClose.setText(_translate("Widget", "关闭"))
import res_rc