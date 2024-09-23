import sys
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QVBoxLayout
import pyqtgraph as pg

WS_UNIT = 'km/h'


class GraphPlot(QGraphicsView):

    def __init__(self, *args, **kwargs):
        super(GraphPlot, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.graph_widget = pg.PlotWidget()

        color = self.palette().color(QPalette.Window)
        self.graph_widget.setBackground(color)

        layout.addWidget(self.graph_widget)
        self.setLayout(layout)

    def plot_graph(self, hourly_info):
        self.graph_widget.clear()
        self.graph_widget.enableAutoRange(axis='y')
        self.graph_widget.setAutoVisible(y=True)
        # self.graph_widget.setRange(xRange=[0, 73], yRange=[0, 30])
        hours = []
        rain_amount = []
        for hour, data in enumerate(hourly_info):
            min_rain_amount = data.get(
                'min_rain_amount')
            max_rain_amount = data.get(
                'max_rain_amount')

            if max_rain_amount == '':
                max_rain_amount = 0

            average_rain_amount = (min_rain_amount+max_rain_amount)/2
            hours.append(hour)
            rain_amount.append(average_rain_amount)

        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.graph_widget.showGrid(x=True, y=True)
        self.graph_widget.setLabel('left', 'Average Amount of Rain (mL)')
        self.graph_widget.setLabel('bottom', 'Forecast Hours (H)')
        self.graph_widget.plot(hours, rain_amount, pen=pen)
