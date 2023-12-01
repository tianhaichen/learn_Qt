import sys
from PyQt5 import QtWidgets
import FormHello

app = QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QWidget()
ui = FormHello.Ui_FormHello()
ui.setupUi(baseWidget)

baseWidget.show()
ui.LabHello.setText("Hello, 被程序修改")
sys.exit(app.exec_())
