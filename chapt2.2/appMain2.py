import sys
from PyQt5.QtWidgets import QWidget, QApplication
from FormHello import Ui_FormHello


class QmyWidget(QWidget, Ui_FormHello):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.Lab = "多重继承的QmyWidget"
        self.setupUi(self)
        self.LabHello.setText(self.Lab)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.btnClose.setText("不关闭了")
    sys.exit(app.exec_())
