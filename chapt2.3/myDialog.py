import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QDialog
from ui_Dialog import Ui_Dialog


class QmyDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.radioBlack.clicked.connect(self.do_setTextColor)
        self.ui.radioRed.clicked.connect(self.do_setTextColor)
        self.ui.radioBlue.clicked.connect(self.do_setTextColor)

    def on_btnClear_clicked(self):
        self.ui.textEdit.clear()

    # @pyqtSlot()
    def on_chkBoxBold_toggled(self,checked):
        font = self.ui.textEdit.font()
        font.setBold(checked)
        self.ui.textEdit.setFont(font)

    # @pyqtSlot()
    def on_chkBoxUnder_clicked(self):
        checked = self.ui.chkBoxUnder.isChecked()
        font = self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)

    @pyqtSlot(bool)
    def on_chkBoxItalic_clicked(self, checked):
        font = self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)

    def do_setTextColor(self):
        plet = self.ui.textEdit.palette()

        if (self.ui.radioBlack.isChecked()):
            plet.setColor(QPalette.Text, Qt.black)
        elif(self.ui.radioRed.isChecked()):
            plet.setColor(QPalette.Text, Qt.red)
        elif(self.ui.radioBlue.isChecked()):
            plet.setColor(QPalette.Text, Qt.blue)

        self.ui.textEdit.setPalette(plet)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = QmyDialog()

    form.show()

    sys.exit(app.exec_())