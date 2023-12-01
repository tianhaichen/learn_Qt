import sys
from PyQt5.QtWidgets import QApplication,QDialog
from myDialog import QmyDialog

app = QApplication(sys.argv)
mainform = QmyDialog()
mainform.show()
sys.exit(app.exec_())