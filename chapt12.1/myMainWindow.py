import sys,math
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtChart import QChartView,QChart,QLineSeries,QValueAxis

class QmyMainWindow(QMainWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Demo12_1, QChart基本绘图")
        self.resize(580,420)

        chart = QChart()
        chart.setTitle("简单函数曲线")

        chartView = QChartView(self)
        chartView.setChart(chart)
        self.setCentralWidget(chartView)

        series0 = QLineSeries()
        series1 = QLineSeries()
        series0.setName("Sin曲线")
        series1.setName("Cos曲线")
        chart.addSeries(series0)
        chart.addSeries(series1)

        t=0
        intv=0.1
        pointCount=100
        for i in range(pointCount):
            y1=math.cos(t)
            series0.append(t,y1)
            y2=math.sin(t+20)
            series1.append(t,y2)
            t=t+intv

        axisX=QValueAxis()
        axisX.setRange(0,10)
        axisX.setTitleText("time(secs)")

        axisY = QValueAxis()
        axisY.setRange(-2,2)
        axisY.setTitleText("value")

        chart.setAxisX(axisX,series0)
        chart.setAxisY(axisY,series0)

        chart.setAxisX(axisX,series1)
        chart.setAxisY(axisY,series1)


##  ===========窗体测试程序=================================
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())