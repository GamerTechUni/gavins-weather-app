""" The Graphing Widget for the program
Using PyQtGraph, this file wraps around it to assist
in plotting graphs for the rain card on the Overview in the frontend
of the program.

The file requires that the 'pyqtgraph' and 'PySide6' modules be installed.
"""
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QVBoxLayout
import pyqtgraph as pg

WS_UNIT = 'km/h'


class GraphPlot(QGraphicsView):
    """
    Widget that takes in weather data and outputs a graphical representation

    ...

    Attributes
    ----------
    graph_widget
        Defines pyqtgraph widget across class
    plot_graph
        Method to draw graph with the data given
    """

    def __init__(self, *args, **kwargs):
        """ Init method to set up the graph
        """
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.graph_widget = pg.PlotWidget()

        # Sets the background of graph to the same as the program
        self.graph_widget.setBackground('#19232D')

        layout.addWidget(self.graph_widget)
        self.setLayout(layout)

    def plot_graph(self, hourly_info):
        """
        Parameters
        ----------
        hourly_info : list
            The weather data that is to be presented graphically

        """
        self.graph_widget.clear()
        # Sets up autorange to resize the area based on the graph presented
        self.graph_widget.enableAutoRange(axis='y')
        self.graph_widget.setAutoVisible(y=True)
        self.graph_widget.setMouseEnabled(x=False, y=False)
        hours = []
        rain_amount = []
        for hour, data in enumerate(hourly_info):
            # Make sure to get a list of total hours and also the data too
            min_rain_amount = data.get(
                'min_rain_amount')
            max_rain_amount = data.get(
                'max_rain_amount')

            if max_rain_amount == '':
                max_rain_amount = 0

            # Get the average amount of rain
            average_rain_amount = (min_rain_amount+max_rain_amount)/2
            hours.append(hour)
            rain_amount.append(average_rain_amount)

        # Sets colour to red and makes line thicker
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        # self.graph_widget.showGrid(x=True, y=True)
        self.graph_widget.setLabel('left', 'Average Amount of Rain (mm)')
        self.graph_widget.setLabel('bottom', 'Forecast Hours (H)')
        # self.graph_widget.plot(hours, rain_amount, pen=pen)
        self.graph_widget.plot()
        bargraph = pg.BarGraphItem(
            x=hours, height=rain_amount, width=0.6, brush='#005392')
        self.graph_widget.addItem(bargraph)
