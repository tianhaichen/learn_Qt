# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\PycharmProjects\pythonProject\learn_Qt\chapt3.10\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 479)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSetHeader = QtWidgets.QPushButton(self.groupBox)
        self.btnSetHeader.setObjectName("btnSetHeader")
        self.gridLayout.addWidget(self.btnSetHeader, 0, 0, 1, 2)
        self.btnSetRows = QtWidgets.QPushButton(self.groupBox)
        self.btnSetRows.setObjectName("btnSetRows")
        self.gridLayout.addWidget(self.btnSetRows, 1, 0, 1, 1)
        self.spinRowCount = QtWidgets.QSpinBox(self.groupBox)
        self.spinRowCount.setMinimum(0)
        self.spinRowCount.setProperty("value", 8)
        self.spinRowCount.setObjectName("spinRowCount")
        self.gridLayout.addWidget(self.spinRowCount, 1, 1, 1, 1)
        self.btnIniData = QtWidgets.QPushButton(self.groupBox)
        self.btnIniData.setObjectName("btnIniData")
        self.gridLayout.addWidget(self.btnIniData, 2, 0, 1, 2)
        self.btnInsertRow = QtWidgets.QPushButton(self.groupBox)
        self.btnInsertRow.setObjectName("btnInsertRow")
        self.gridLayout.addWidget(self.btnInsertRow, 3, 0, 1, 1)
        self.btnAppendRow = QtWidgets.QPushButton(self.groupBox)
        self.btnAppendRow.setObjectName("btnAppendRow")
        self.gridLayout.addWidget(self.btnAppendRow, 3, 1, 1, 1)
        self.btnDelCurRow = QtWidgets.QPushButton(self.groupBox)
        self.btnDelCurRow.setObjectName("btnDelCurRow")
        self.gridLayout.addWidget(self.btnDelCurRow, 4, 0, 1, 1)
        self.btnClearContents = QtWidgets.QPushButton(self.groupBox)
        self.btnClearContents.setObjectName("btnClearContents")
        self.gridLayout.addWidget(self.btnClearContents, 4, 1, 1, 1)
        self.btnAutoHeight = QtWidgets.QPushButton(self.groupBox)
        self.btnAutoHeight.setObjectName("btnAutoHeight")
        self.gridLayout.addWidget(self.btnAutoHeight, 5, 0, 1, 1)
        self.btnAutoWidth = QtWidgets.QPushButton(self.groupBox)
        self.btnAutoWidth.setObjectName("btnAutoWidth")
        self.gridLayout.addWidget(self.btnAutoWidth, 5, 1, 1, 1)
        self.btnReadToText = QtWidgets.QPushButton(self.groupBox)
        self.btnReadToText.setObjectName("btnReadToText")
        self.gridLayout.addWidget(self.btnReadToText, 6, 0, 1, 2)
        self.chkBoxEditable = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxEditable.setChecked(True)
        self.chkBoxEditable.setObjectName("chkBoxEditable")
        self.gridLayout.addWidget(self.chkBoxEditable, 7, 0, 1, 1)
        self.chkBoxRowColor = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxRowColor.setChecked(True)
        self.chkBoxRowColor.setObjectName("chkBoxRowColor")
        self.gridLayout.addWidget(self.chkBoxRowColor, 7, 1, 1, 1)
        self.chkBoxHeaderH = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxHeaderH.setChecked(True)
        self.chkBoxHeaderH.setObjectName("chkBoxHeaderH")
        self.gridLayout.addWidget(self.chkBoxHeaderH, 8, 0, 1, 1)
        self.chkBoxHeaderV = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxHeaderV.setChecked(True)
        self.chkBoxHeaderV.setObjectName("chkBoxHeaderV")
        self.gridLayout.addWidget(self.chkBoxHeaderV, 8, 1, 1, 1)
        self.radioSelectRow = QtWidgets.QRadioButton(self.groupBox)
        self.radioSelectRow.setObjectName("radioSelectRow")
        self.gridLayout.addWidget(self.radioSelectRow, 9, 0, 1, 1)
        self.radioSelectItem = QtWidgets.QRadioButton(self.groupBox)
        self.radioSelectItem.setChecked(True)
        self.radioSelectItem.setObjectName("radioSelectItem")
        self.gridLayout.addWidget(self.radioSelectItem, 9, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableInfo = QtWidgets.QTableWidget(self.splitter)
        self.tableInfo.setObjectName("tableInfo")
        self.tableInfo.setColumnCount(5)
        self.tableInfo.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/boy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableInfo.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableInfo.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/girl.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tableInfo.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableInfo.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInfo.setItem(4, 3, item)
        self.textEdit = QtWidgets.QPlainTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSetHeader.setText(_translate("MainWindow", "设置表头"))
        self.btnSetRows.setText(_translate("MainWindow", "设置行数"))
        self.btnIniData.setText(_translate("MainWindow", "初始化表格数据"))
        self.btnInsertRow.setText(_translate("MainWindow", "插入行"))
        self.btnAppendRow.setText(_translate("MainWindow", "添加行"))
        self.btnDelCurRow.setText(_translate("MainWindow", "删除当前行"))
        self.btnClearContents.setText(_translate("MainWindow", "清空表格内容"))
        self.btnAutoHeight.setText(_translate("MainWindow", "自动调节行高"))
        self.btnAutoWidth.setText(_translate("MainWindow", "自动调节列宽"))
        self.btnReadToText.setText(_translate("MainWindow", "读取表格内容到文本"))
        self.chkBoxEditable.setText(_translate("MainWindow", "表格可编辑"))
        self.chkBoxRowColor.setText(_translate("MainWindow", "间隔行底色"))
        self.chkBoxHeaderH.setText(_translate("MainWindow", "显示行表头"))
        self.chkBoxHeaderV.setText(_translate("MainWindow", "显示列表头"))
        self.radioSelectRow.setText(_translate("MainWindow", "行选择"))
        self.radioSelectItem.setText(_translate("MainWindow", "单元格选择"))
        item = self.tableInfo.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableInfo.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableInfo.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableInfo.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableInfo.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "列1"))
        item = self.tableInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "列2"))
        item = self.tableInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "列3"))
        item = self.tableInfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "列4"))
        item = self.tableInfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "列5"))
        __sortingEnabled = self.tableInfo.isSortingEnabled()
        self.tableInfo.setSortingEnabled(False)
        item = self.tableInfo.item(0, 0)
        item.setText(_translate("MainWindow", "0行，0列"))
        item = self.tableInfo.item(0, 1)
        item.setText(_translate("MainWindow", "0行，1列"))
        item = self.tableInfo.item(0, 2)
        item.setText(_translate("MainWindow", "0行，2列"))
        item = self.tableInfo.item(0, 3)
        item.setText(_translate("MainWindow", "0行，3列"))
        item = self.tableInfo.item(1, 0)
        item.setText(_translate("MainWindow", "1行，0列"))
        item = self.tableInfo.item(1, 1)
        item.setText(_translate("MainWindow", "1行，1列"))
        item = self.tableInfo.item(2, 0)
        item.setText(_translate("MainWindow", "2行，0列"))
        item = self.tableInfo.item(3, 0)
        item.setText(_translate("MainWindow", "3行，0列"))
        item = self.tableInfo.item(4, 0)
        item.setText(_translate("MainWindow", "4行，0列"))
        item = self.tableInfo.item(4, 3)
        item.setText(_translate("MainWindow", "4行，3列"))
        self.tableInfo.setSortingEnabled(__sortingEnabled)
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
