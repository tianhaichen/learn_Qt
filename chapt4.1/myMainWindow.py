import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel
from PyQt5.QtCore import QDir
from ui_MainWindow import Ui_MainWindow


class QmyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(QmyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__buildModelView()

    ##  ==============自定义功能函数============
    def __buildModelView(self):
        self.model = QFileSystemModel(self)
        self.model.setRootPath(QDir.currentPath())

        self.ui.treeView.setModel(self.model)
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)

        self.ui.treeView.clicked.connect(self.ui.listView.setRootIndex)
        self.ui.treeView.clicked.connect(self.ui.tableView.setRootIndex)

    # == == == == == 由connectSlotsByName() 自动连接的槽函数 == == == == == == == == ==

    def on_treeView_clicked(self, index):

        self.ui.chkBox_IsDir.setChecked(self.model.isDir(index))

        self.ui.LabPath.setText(self.model.filePath(index))
        self.ui.LabType.setText(self.model.type(index))
        self.ui.LabFileName.setText(self.model.fileName(index))

        fileSize = self.model.size(index) / 1024
        if (fileSize < 1024):
            self.ui.LabFileSize.setText("%d KB" % fileSize)
        else:
            self.ui.LabFileSize.setText("%.2f MB" % (fileSize / 1024.0))


##  ===========窗体测试程序=================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
