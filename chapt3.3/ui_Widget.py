# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\PycharmProjects\pythonProject\learn_Qt\chatp3.3\ui_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(393, 235)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.slider = QtWidgets.QSlider(self.groupBox)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.scrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.scrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.scrollBar.setObjectName("scrollBar")
        self.gridLayout.addWidget(self.scrollBar, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chkBox_Visible = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBox_Visible.setChecked(True)
        self.chkBox_Visible.setObjectName("chkBox_Visible")
        self.gridLayout_2.addWidget(self.chkBox_Visible, 0, 0, 1, 1)
        self.chkBox_Inverted = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBox_Inverted.setObjectName("chkBox_Inverted")
        self.gridLayout_2.addWidget(self.chkBox_Inverted, 0, 1, 1, 1)
        self.radio_Percent = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_Percent.setChecked(True)
        self.radio_Percent.setObjectName("radio_Percent")
        self.gridLayout_2.addWidget(self.radio_Percent, 1, 0, 1, 1)
        self.radio_Value = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_Value.setObjectName("radio_Value")
        self.gridLayout_2.addWidget(self.radio_Value, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.label.setText(_translate("Widget", "Slider"))
        self.label_2.setText(_translate("Widget", "ScrollBar"))
        self.label_3.setText(_translate("Widget", "ProgrammBar"))
        self.groupBox_2.setTitle(_translate("Widget", "ProgressBar设置"))
        self.chkBox_Visible.setText(_translate("Widget", "textVisible"))
        self.chkBox_Inverted.setText(_translate("Widget", "InvertedAppearance"))
        self.radio_Percent.setText(_translate("Widget", "显示格式--百分比"))
        self.radio_Value.setText(_translate("Widget", "显示格式--当前值"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Widget = QtWidgets.QWidget()
#     ui = Ui_Widget()
#     ui.setupUi(Widget)
#     Widget.show()
#     sys.exit(app.exec_())
