# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from compasswidget import CompassWidget
from graphplot import GraphPlot

class Ui_WeatherApp(object):
    def setupUi(self, WeatherApp):
        if not WeatherApp.objectName():
            WeatherApp.setObjectName(u"WeatherApp")
        WeatherApp.resize(1158, 881)
        WeatherApp.setStyleSheet(u"")
        self.centralwidget = QWidget(WeatherApp)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setBold(False)
        font1.setItalic(False)
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.location_input = QLineEdit(self.frame_3)
        self.location_input.setObjectName(u"location_input")
        self.location_input.setFont(font1)
        self.location_input.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.location_input)

        self.location_choices = QComboBox(self.frame_3)
        self.location_choices.setObjectName(u"location_choices")
        self.location_choices.setFont(font1)

        self.horizontalLayout.addWidget(self.location_choices)

        self.get_weather_button = QPushButton(self.frame_3)
        self.get_weather_button.setObjectName(u"get_weather_button")
        self.get_weather_button.setFont(font1)

        self.horizontalLayout.addWidget(self.get_weather_button)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.overview = QWidget()
        self.overview.setObjectName(u"overview")
        self.horizontalLayout_12 = QHBoxLayout(self.overview)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.left_side = QVBoxLayout()
        self.left_side.setObjectName(u"left_side")
        self.current_temp = QFrame(self.overview)
        self.current_temp.setObjectName(u"current_temp")
        self.current_temp.setFont(font1)
        self.current_temp.setFrameShape(QFrame.Shape.Box)
        self.current_temp.setFrameShadow(QFrame.Shadow.Plain)
        self.current_temp.setLineWidth(2)
        self.horizontalLayout_15 = QHBoxLayout(self.current_temp)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.place_overview = QLabel(self.current_temp)
        self.place_overview.setObjectName(u"place_overview")
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setItalic(False)
        self.place_overview.setFont(font2)
        self.place_overview.setTextFormat(Qt.TextFormat.PlainText)
        self.place_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.place_overview.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.place_overview)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.current_temp_overview = QLabel(self.current_temp)
        self.current_temp_overview.setObjectName(u"current_temp_overview")
        self.current_temp_overview.setMaximumSize(QSize(200, 50))
        font3 = QFont()
        font3.setFamilies([u"Sans Serif"])
        font3.setPointSize(30)
        font3.setBold(False)
        font3.setItalic(False)
        self.current_temp_overview.setFont(font3)
        self.current_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.current_temp_overview)

        self.current_day_icon_overview = QLabel(self.current_temp)
        self.current_day_icon_overview.setObjectName(u"current_day_icon_overview")
        self.current_day_icon_overview.setMaximumSize(QSize(100, 100))
        font4 = QFont()
        font4.setFamilies([u"Sans Serif"])
        font4.setPointSize(35)
        font4.setBold(False)
        font4.setItalic(False)
        self.current_day_icon_overview.setFont(font4)

        self.horizontalLayout_11.addWidget(self.current_day_icon_overview)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.current_condtions_overview = QLabel(self.current_temp)
        self.current_condtions_overview.setObjectName(u"current_condtions_overview")
        font5 = QFont()
        font5.setFamilies([u"Sans Serif"])
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        self.current_condtions_overview.setFont(font5)
        self.current_condtions_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.current_condtions_overview)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.min_temp_overview = QLabel(self.current_temp)
        self.min_temp_overview.setObjectName(u"min_temp_overview")
        self.min_temp_overview.setFont(font1)
        self.min_temp_overview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.min_temp_overview)

        self.max_temp_overview = QLabel(self.current_temp)
        self.max_temp_overview.setObjectName(u"max_temp_overview")
        self.max_temp_overview.setFont(font1)
        self.max_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.max_temp_overview)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.feels_like_temp_overview = QLabel(self.current_temp)
        self.feels_like_temp_overview.setObjectName(u"feels_like_temp_overview")
        self.feels_like_temp_overview.setFont(font1)
        self.feels_like_temp_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.feels_like_temp_overview)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)


        self.left_side.addWidget(self.current_temp)

        self.forecast_overview = QFrame(self.overview)
        self.forecast_overview.setObjectName(u"forecast_overview")
        self.forecast_overview.setFont(font1)
        self.forecast_overview.setFrameShape(QFrame.Shape.Box)
        self.forecast_overview.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_overview.setLineWidth(2)
        self.horizontalLayout_9 = QHBoxLayout(self.forecast_overview)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.day1_overview = QLabel(self.forecast_overview)
        self.day1_overview.setObjectName(u"day1_overview")
        self.day1_overview.setFont(font1)

        self.verticalLayout_2.addWidget(self.day1_overview)

        self.day2_overview = QLabel(self.forecast_overview)
        self.day2_overview.setObjectName(u"day2_overview")
        self.day2_overview.setFont(font1)

        self.verticalLayout_2.addWidget(self.day2_overview)

        self.day3_overview = QLabel(self.forecast_overview)
        self.day3_overview.setObjectName(u"day3_overview")
        self.day3_overview.setFont(font1)

        self.verticalLayout_2.addWidget(self.day3_overview)

        self.day4_overview = QLabel(self.forecast_overview)
        self.day4_overview.setObjectName(u"day4_overview")
        self.day4_overview.setFont(font1)

        self.verticalLayout_2.addWidget(self.day4_overview)

        self.day5_overview = QLabel(self.forecast_overview)
        self.day5_overview.setObjectName(u"day5_overview")
        self.day5_overview.setFont(font1)

        self.verticalLayout_2.addWidget(self.day5_overview)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.icon_overview1 = QLabel(self.forecast_overview)
        self.icon_overview1.setObjectName(u"icon_overview1")
        self.icon_overview1.setMaximumSize(QSize(75, 75))
        font6 = QFont()
        font6.setFamilies([u"Sans Serif"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.icon_overview1.setFont(font6)
        self.icon_overview1.setPixmap(QPixmap(u"../8a3a0566/sunny.png"))
        self.icon_overview1.setScaledContents(True)
        self.icon_overview1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview1)

        self.icon_chance_of_rain1 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain1.setObjectName(u"icon_chance_of_rain1")
        self.icon_chance_of_rain1.setMaximumSize(QSize(75, 75))
        font7 = QFont()
        font7.setFamilies([u"Sans Serif"])
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setItalic(False)
        self.icon_chance_of_rain1.setFont(font7)
        self.icon_chance_of_rain1.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain1)

        self.icon_overview2 = QLabel(self.forecast_overview)
        self.icon_overview2.setObjectName(u"icon_overview2")
        self.icon_overview2.setMaximumSize(QSize(75, 75))
        self.icon_overview2.setFont(font6)
        self.icon_overview2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview2)

        self.icon_chance_of_rain2 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain2.setObjectName(u"icon_chance_of_rain2")
        self.icon_chance_of_rain2.setMaximumSize(QSize(75, 75))
        font8 = QFont()
        font8.setFamilies([u"Sans Serif"])
        font8.setBold(True)
        font8.setItalic(False)
        self.icon_chance_of_rain2.setFont(font8)
        self.icon_chance_of_rain2.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain2)

        self.icon_overview3 = QLabel(self.forecast_overview)
        self.icon_overview3.setObjectName(u"icon_overview3")
        self.icon_overview3.setMaximumSize(QSize(75, 75))
        self.icon_overview3.setFont(font6)
        self.icon_overview3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview3)

        self.icon_chance_of_rain3 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain3.setObjectName(u"icon_chance_of_rain3")
        self.icon_chance_of_rain3.setMaximumSize(QSize(75, 75))
        self.icon_chance_of_rain3.setFont(font8)
        self.icon_chance_of_rain3.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain3)

        self.icon_overview4 = QLabel(self.forecast_overview)
        self.icon_overview4.setObjectName(u"icon_overview4")
        self.icon_overview4.setMaximumSize(QSize(75, 75))
        self.icon_overview4.setFont(font6)
        self.icon_overview4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview4)

        self.icon_chance_of_rain4 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain4.setObjectName(u"icon_chance_of_rain4")
        self.icon_chance_of_rain4.setMaximumSize(QSize(75, 75))
        self.icon_chance_of_rain4.setFont(font8)
        self.icon_chance_of_rain4.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain4)

        self.icon_overview5 = QLabel(self.forecast_overview)
        self.icon_overview5.setObjectName(u"icon_overview5")
        self.icon_overview5.setMaximumSize(QSize(75, 75))
        self.icon_overview5.setFont(font6)
        self.icon_overview5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview5)

        self.icon_chance_of_rain5 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain5.setObjectName(u"icon_chance_of_rain5")
        self.icon_chance_of_rain5.setMaximumSize(QSize(75, 75))
        self.icon_chance_of_rain5.setFont(font8)
        self.icon_chance_of_rain5.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.day1_temp_overview = QLabel(self.forecast_overview)
        self.day1_temp_overview.setObjectName(u"day1_temp_overview")
        self.day1_temp_overview.setFont(font1)
        self.day1_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day1_temp_overview)

        self.day2_temp_overview = QLabel(self.forecast_overview)
        self.day2_temp_overview.setObjectName(u"day2_temp_overview")
        self.day2_temp_overview.setFont(font1)
        self.day2_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day2_temp_overview)

        self.day3_temp_overview = QLabel(self.forecast_overview)
        self.day3_temp_overview.setObjectName(u"day3_temp_overview")
        self.day3_temp_overview.setFont(font1)
        self.day3_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day3_temp_overview)

        self.day4_temp_overview = QLabel(self.forecast_overview)
        self.day4_temp_overview.setObjectName(u"day4_temp_overview")
        self.day4_temp_overview.setFont(font1)
        self.day4_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day4_temp_overview)

        self.day5_temp_overview = QLabel(self.forecast_overview)
        self.day5_temp_overview.setObjectName(u"day5_temp_overview")
        self.day5_temp_overview.setFont(font1)
        self.day5_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day5_temp_overview)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)


        self.left_side.addWidget(self.forecast_overview)


        self.horizontalLayout_12.addLayout(self.left_side)

        self.right_side = QVBoxLayout()
        self.right_side.setObjectName(u"right_side")
        self.uv_index = QFrame(self.overview)
        self.uv_index.setObjectName(u"uv_index")
        self.uv_index.setFont(font1)
        self.uv_index.setFrameShape(QFrame.Shape.Box)
        self.uv_index.setFrameShadow(QFrame.Shadow.Plain)
        self.uv_index.setLineWidth(2)
        self.horizontalLayout_6 = QHBoxLayout(self.uv_index)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.uv_index)
        self.label_17.setObjectName(u"label_17")
        font9 = QFont()
        font9.setFamilies([u"Sans Serif"])
        font9.setPointSize(20)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_17.setFont(font9)

        self.verticalLayout_5.addWidget(self.label_17)

        self.uv_index_bar = QProgressBar(self.uv_index)
        self.uv_index_bar.setObjectName(u"uv_index_bar")
        self.uv_index_bar.setFont(font1)
        self.uv_index_bar.setStyleSheet(u"")
        self.uv_index_bar.setMinimum(0)
        self.uv_index_bar.setMaximum(14)
        self.uv_index_bar.setValue(0)
        self.uv_index_bar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.uv_index_bar.setTextVisible(False)
        self.uv_index_bar.setOrientation(Qt.Orientation.Horizontal)
        self.uv_index_bar.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.uv_index_bar)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.max_uv_overview = QLabel(self.uv_index)
        self.max_uv_overview.setObjectName(u"max_uv_overview")
        self.max_uv_overview.setFont(font1)

        self.horizontalLayout_5.addWidget(self.max_uv_overview)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sun_protection_recommended_overview = QLabel(self.uv_index)
        self.sun_protection_recommended_overview.setObjectName(u"sun_protection_recommended_overview")
        self.sun_protection_recommended_overview.setFont(font1)

        self.verticalLayout_7.addWidget(self.sun_protection_recommended_overview)

        self.protection_time_overview = QLabel(self.uv_index)
        self.protection_time_overview.setObjectName(u"protection_time_overview")
        self.protection_time_overview.setFont(font1)

        self.verticalLayout_7.addWidget(self.protection_time_overview)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.right_side.addWidget(self.uv_index)

        self.sunrise_and_set = QFrame(self.overview)
        self.sunrise_and_set.setObjectName(u"sunrise_and_set")
        self.sunrise_and_set.setFont(font1)
        self.sunrise_and_set.setFrameShape(QFrame.Shape.Box)
        self.sunrise_and_set.setFrameShadow(QFrame.Shadow.Plain)
        self.sunrise_and_set.setLineWidth(2)
        self.horizontalLayout_7 = QHBoxLayout(self.sunrise_and_set)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sunrise_overview = QLabel(self.sunrise_and_set)
        self.sunrise_overview.setObjectName(u"sunrise_overview")
        self.sunrise_overview.setFont(font1)

        self.horizontalLayout_4.addWidget(self.sunrise_overview)

        self.sunset_overview = QLabel(self.sunrise_and_set)
        self.sunset_overview.setObjectName(u"sunset_overview")
        self.sunset_overview.setFont(font1)

        self.horizontalLayout_4.addWidget(self.sunset_overview)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.right_side.addWidget(self.sunrise_and_set)

        self.amount_of_rain = QFrame(self.overview)
        self.amount_of_rain.setObjectName(u"amount_of_rain")
        self.amount_of_rain.setFont(font1)
        self.amount_of_rain.setFrameShape(QFrame.Shape.Box)
        self.amount_of_rain.setFrameShadow(QFrame.Shadow.Plain)
        self.amount_of_rain.setLineWidth(2)
        self.verticalLayout_11 = QVBoxLayout(self.amount_of_rain)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.rain_graph_overview = GraphPlot(self.amount_of_rain)
        self.rain_graph_overview.setObjectName(u"rain_graph_overview")
        self.rain_graph_overview.setFont(font1)
        self.rain_graph_overview.setFrameShape(QFrame.Shape.NoFrame)
        self.rain_graph_overview.setFrameShadow(QFrame.Shadow.Plain)
        self.rain_graph_overview.setLineWidth(0)

        self.verticalLayout_11.addWidget(self.rain_graph_overview)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.amount_of_rain)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_6)

        self.forecast_amount_of_rain_overview = QLabel(self.amount_of_rain)
        self.forecast_amount_of_rain_overview.setObjectName(u"forecast_amount_of_rain_overview")
        self.forecast_amount_of_rain_overview.setFont(font1)

        self.horizontalLayout_17.addWidget(self.forecast_amount_of_rain_overview)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 20)

        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_4 = QLabel(self.amount_of_rain)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_4)

        self.chance_of_rain_overview = QLabel(self.amount_of_rain)
        self.chance_of_rain_overview.setObjectName(u"chance_of_rain_overview")
        self.chance_of_rain_overview.setFont(font1)

        self.horizontalLayout_18.addWidget(self.chance_of_rain_overview)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 20)

        self.verticalLayout_11.addLayout(self.horizontalLayout_18)


        self.right_side.addWidget(self.amount_of_rain)

        self.wind_speed = QFrame(self.overview)
        self.wind_speed.setObjectName(u"wind_speed")
        self.wind_speed.setFont(font1)
        self.wind_speed.setFrameShape(QFrame.Shape.Box)
        self.wind_speed.setFrameShadow(QFrame.Shadow.Plain)
        self.wind_speed.setLineWidth(2)
        self.verticalLayout_9 = QVBoxLayout(self.wind_speed)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.wind_speed)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.compass_widget = CompassWidget(self.wind_speed)
        self.compass_widget.setObjectName(u"compass_widget")
        self.compass_widget.setMinimumSize(QSize(100, 100))
        self.compass_widget.setFont(font1)

        self.verticalLayout_9.addWidget(self.compass_widget)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_25 = QLabel(self.wind_speed)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_25)

        self.wind_speed_overview = QLabel(self.wind_speed)
        self.wind_speed_overview.setObjectName(u"wind_speed_overview")
        self.wind_speed_overview.setFont(font1)
        self.wind_speed_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.wind_speed_overview)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.right_side.addWidget(self.wind_speed)


        self.horizontalLayout_12.addLayout(self.right_side)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.tabWidget.addTab(self.overview, "")
        self.past_weather = QWidget()
        self.past_weather.setObjectName(u"past_weather")
        self.verticalLayout_12 = QVBoxLayout(self.past_weather)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.Highlights = QFrame(self.past_weather)
        self.Highlights.setObjectName(u"Highlights")
        self.Highlights.setFont(font1)
        self.Highlights.setFrameShape(QFrame.Shape.NoFrame)
        self.Highlights.setFrameShadow(QFrame.Shadow.Plain)
        self.Highlights.setLineWidth(2)
        self.gridLayout = QGridLayout(self.Highlights)
        self.gridLayout.setObjectName(u"gridLayout")
        self.highest_gust_speed = QFrame(self.Highlights)
        self.highest_gust_speed.setObjectName(u"highest_gust_speed")
        self.highest_gust_speed.setFont(font1)
        self.highest_gust_speed.setFrameShape(QFrame.Shape.Box)
        self.highest_gust_speed.setFrameShadow(QFrame.Shadow.Plain)
        self.highest_gust_speed.setLineWidth(2)
        self.verticalLayout_19 = QVBoxLayout(self.highest_gust_speed)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.highlights_gust_speed = QLabel(self.highest_gust_speed)
        self.highlights_gust_speed.setObjectName(u"highlights_gust_speed")
        self.highlights_gust_speed.setFont(font5)

        self.horizontalLayout_8.addWidget(self.highlights_gust_speed)

        self.highlights_gust_speed_time = QLabel(self.highest_gust_speed)
        self.highlights_gust_speed_time.setObjectName(u"highlights_gust_speed_time")
        self.highlights_gust_speed_time.setFont(font1)

        self.horizontalLayout_8.addWidget(self.highlights_gust_speed_time)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 20)

        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.label_35 = QLabel(self.highest_gust_speed)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_35)


        self.verticalLayout_19.addLayout(self.verticalLayout_15)


        self.gridLayout.addWidget(self.highest_gust_speed, 2, 0, 1, 1)

        self.highest_temperature = QFrame(self.Highlights)
        self.highest_temperature.setObjectName(u"highest_temperature")
        self.highest_temperature.setFont(font1)
        self.highest_temperature.setFrameShape(QFrame.Shape.Box)
        self.highest_temperature.setFrameShadow(QFrame.Shadow.Plain)
        self.highest_temperature.setLineWidth(2)
        self.verticalLayout_18 = QVBoxLayout(self.highest_temperature)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.highlights_max_temp = QLabel(self.highest_temperature)
        self.highlights_max_temp.setObjectName(u"highlights_max_temp")
        self.highlights_max_temp.setFont(font5)

        self.horizontalLayout_2.addWidget(self.highlights_max_temp)

        self.highlights_max_temp_time = QLabel(self.highest_temperature)
        self.highlights_max_temp_time.setObjectName(u"highlights_max_temp_time")
        self.highlights_max_temp_time.setFont(font1)

        self.horizontalLayout_2.addWidget(self.highlights_max_temp_time)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 20)

        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.label_29 = QLabel(self.highest_temperature)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_29)


        self.verticalLayout_18.addLayout(self.verticalLayout_13)


        self.gridLayout.addWidget(self.highest_temperature, 1, 0, 1, 1)

        self.amount_of_rain_9am = QFrame(self.Highlights)
        self.amount_of_rain_9am.setObjectName(u"amount_of_rain_9am")
        self.amount_of_rain_9am.setFont(font1)
        self.amount_of_rain_9am.setFrameShape(QFrame.Shape.Box)
        self.amount_of_rain_9am.setFrameShadow(QFrame.Shadow.Plain)
        self.amount_of_rain_9am.setLineWidth(2)
        self.verticalLayout_17 = QVBoxLayout(self.amount_of_rain_9am)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.highlights_rain_since_9am = QLabel(self.amount_of_rain_9am)
        self.highlights_rain_since_9am.setObjectName(u"highlights_rain_since_9am")
        self.highlights_rain_since_9am.setFont(font5)

        self.horizontalLayout_13.addWidget(self.highlights_rain_since_9am)

        self.label_37 = QLabel(self.amount_of_rain_9am)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_37)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 20)

        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.label_38 = QLabel(self.amount_of_rain_9am)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_38)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.gridLayout.addWidget(self.amount_of_rain_9am, 2, 1, 1, 1)

        self.lowest_temperature = QFrame(self.Highlights)
        self.lowest_temperature.setObjectName(u"lowest_temperature")
        self.lowest_temperature.setFont(font1)
        self.lowest_temperature.setFrameShape(QFrame.Shape.Box)
        self.lowest_temperature.setFrameShadow(QFrame.Shadow.Plain)
        self.lowest_temperature.setLineWidth(2)
        self.horizontalLayout_14 = QHBoxLayout(self.lowest_temperature)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.highlights_min_temp = QLabel(self.lowest_temperature)
        self.highlights_min_temp.setObjectName(u"highlights_min_temp")
        self.highlights_min_temp.setFont(font5)

        self.horizontalLayout_3.addWidget(self.highlights_min_temp)

        self.highlights_min_temp_time = QLabel(self.lowest_temperature)
        self.highlights_min_temp_time.setObjectName(u"highlights_min_temp_time")
        self.highlights_min_temp_time.setFont(font1)

        self.horizontalLayout_3.addWidget(self.highlights_min_temp_time)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)

        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.label_32 = QLabel(self.lowest_temperature)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_32)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)


        self.gridLayout.addWidget(self.lowest_temperature, 1, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.Highlights)

        self.observation_info_table = QTableWidget(self.past_weather)
        self.observation_info_table.setObjectName(u"observation_info_table")
        self.observation_info_table.setFont(font1)
        self.observation_info_table.setFrameShape(QFrame.Shape.Box)
        self.observation_info_table.setFrameShadow(QFrame.Shadow.Plain)
        self.observation_info_table.setLineWidth(2)

        self.verticalLayout_12.addWidget(self.observation_info_table)

        self.tabWidget.addTab(self.past_weather, "")
        self.forecast_weather = QWidget()
        self.forecast_weather.setObjectName(u"forecast_weather")
        self.verticalLayout_20 = QVBoxLayout(self.forecast_weather)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea = QScrollArea(self.forecast_weather)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFont(font1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 3642, 358))
        self.horizontalLayout_16 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.forecast_day1 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day1.setObjectName(u"forecast_day1")
        self.forecast_day1.setMinimumSize(QSize(600, 100))
        self.forecast_day1.setFont(font1)
        self.forecast_day1.setFrameShape(QFrame.Shape.Box)
        self.forecast_day1.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day1.setLineWidth(2)
        self.horizontalLayout_28 = QHBoxLayout(self.forecast_day1)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.forecast_day1_icon = QLabel(self.forecast_day1)
        self.forecast_day1_icon.setObjectName(u"forecast_day1_icon")
        self.forecast_day1_icon.setMaximumSize(QSize(75, 75))
        self.forecast_day1_icon.setFont(font1)

        self.horizontalLayout_19.addWidget(self.forecast_day1_icon)

        self.forecast_day1_date = QLabel(self.forecast_day1)
        self.forecast_day1_date.setObjectName(u"forecast_day1_date")
        self.forecast_day1_date.setFont(font1)

        self.horizontalLayout_19.addWidget(self.forecast_day1_date)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.forecast_day1_min_temp = QLabel(self.forecast_day1)
        self.forecast_day1_min_temp.setObjectName(u"forecast_day1_min_temp")
        self.forecast_day1_min_temp.setFont(font1)

        self.horizontalLayout_24.addWidget(self.forecast_day1_min_temp)

        self.forecast_day1_max_temp = QLabel(self.forecast_day1)
        self.forecast_day1_max_temp.setObjectName(u"forecast_day1_max_temp")
        self.forecast_day1_max_temp.setFont(font1)

        self.horizontalLayout_24.addWidget(self.forecast_day1_max_temp)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 20)

        self.verticalLayout_21.addLayout(self.horizontalLayout_24)

        self.border_1 = QFrame(self.forecast_day1)
        self.border_1.setObjectName(u"border_1")
        self.border_1.setMinimumSize(QSize(0, 1))
        self.border_1.setMaximumSize(QSize(16777215, 1))
        self.border_1.setFont(font1)
        self.border_1.setFrameShape(QFrame.Shape.Box)
        self.border_1.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_21.addWidget(self.border_1)

        self.label_9 = QLabel(self.forecast_day1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_9)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.forecast_day1_chance_of_rain_1 = QLabel(self.forecast_day1)
        self.forecast_day1_chance_of_rain_1.setObjectName(u"forecast_day1_chance_of_rain_1")
        self.forecast_day1_chance_of_rain_1.setFont(font1)

        self.horizontalLayout_25.addWidget(self.forecast_day1_chance_of_rain_1)

        self.forecast_day1_amount_of_rain_1 = QLabel(self.forecast_day1)
        self.forecast_day1_amount_of_rain_1.setObjectName(u"forecast_day1_amount_of_rain_1")
        self.forecast_day1_amount_of_rain_1.setFont(font8)

        self.horizontalLayout_25.addWidget(self.forecast_day1_amount_of_rain_1)

        self.horizontalLayout_25.setStretch(0, 1)
        self.horizontalLayout_25.setStretch(1, 20)

        self.verticalLayout_21.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.forecast_day1_chance_of_rain_2 = QLabel(self.forecast_day1)
        self.forecast_day1_chance_of_rain_2.setObjectName(u"forecast_day1_chance_of_rain_2")
        self.forecast_day1_chance_of_rain_2.setFont(font1)

        self.horizontalLayout_26.addWidget(self.forecast_day1_chance_of_rain_2)

        self.forecast_day1_amount_of_rain_2 = QLabel(self.forecast_day1)
        self.forecast_day1_amount_of_rain_2.setObjectName(u"forecast_day1_amount_of_rain_2")
        self.forecast_day1_amount_of_rain_2.setFont(font8)

        self.horizontalLayout_26.addWidget(self.forecast_day1_amount_of_rain_2)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(1, 20)

        self.verticalLayout_21.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.forecast_day1_chance_of_rain_3 = QLabel(self.forecast_day1)
        self.forecast_day1_chance_of_rain_3.setObjectName(u"forecast_day1_chance_of_rain_3")

        self.horizontalLayout_20.addWidget(self.forecast_day1_chance_of_rain_3)

        self.forecast_day1_amount_of_rain_3 = QLabel(self.forecast_day1)
        self.forecast_day1_amount_of_rain_3.setObjectName(u"forecast_day1_amount_of_rain_3")
        self.forecast_day1_amount_of_rain_3.setFont(font8)

        self.horizontalLayout_20.addWidget(self.forecast_day1_amount_of_rain_3)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 20)

        self.verticalLayout_21.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_28.addLayout(self.verticalLayout_21)

        self.border_3 = QFrame(self.forecast_day1)
        self.border_3.setObjectName(u"border_3")
        self.border_3.setMinimumSize(QSize(1, 0))
        self.border_3.setMaximumSize(QSize(1, 16777215))
        self.border_3.setFont(font1)
        self.border_3.setFrameShape(QFrame.Shape.Box)
        self.border_3.setFrameShadow(QFrame.Shadow.Plain)
        self.border_3.setLineWidth(10)

        self.horizontalLayout_28.addWidget(self.border_3)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_14 = QLabel(self.forecast_day1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_14)

        self.forecast_day1_info = QLabel(self.forecast_day1)
        self.forecast_day1_info.setObjectName(u"forecast_day1_info")
        self.forecast_day1_info.setFont(font1)
        self.forecast_day1_info.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.forecast_day1_info)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.forecast_day1_fire_danger = QLabel(self.forecast_day1)
        self.forecast_day1_fire_danger.setObjectName(u"forecast_day1_fire_danger")
        self.forecast_day1_fire_danger.setFont(font8)

        self.horizontalLayout_27.addWidget(self.forecast_day1_fire_danger)

        self.label_16 = QLabel(self.forecast_day1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_27.addWidget(self.label_16)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 20)

        self.verticalLayout_26.addLayout(self.horizontalLayout_27)

        self.border_2 = QFrame(self.forecast_day1)
        self.border_2.setObjectName(u"border_2")
        self.border_2.setMinimumSize(QSize(0, 1))
        self.border_2.setMaximumSize(QSize(16777215, 1))
        self.border_2.setFont(font1)
        self.border_2.setFrameShape(QFrame.Shape.Box)
        self.border_2.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_26.addWidget(self.border_2)

        self.label_19 = QLabel(self.forecast_day1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_19)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.forecast_day1_sunrise_time = QLabel(self.forecast_day1)
        self.forecast_day1_sunrise_time.setObjectName(u"forecast_day1_sunrise_time")
        self.forecast_day1_sunrise_time.setFont(font1)

        self.horizontalLayout_29.addWidget(self.forecast_day1_sunrise_time)

        self.forecast_day1_sunset_time = QLabel(self.forecast_day1)
        self.forecast_day1_sunset_time.setObjectName(u"forecast_day1_sunset_time")
        self.forecast_day1_sunset_time.setFont(font1)

        self.horizontalLayout_29.addWidget(self.forecast_day1_sunset_time)

        self.horizontalLayout_29.setStretch(0, 1)
        self.horizontalLayout_29.setStretch(1, 20)

        self.verticalLayout_26.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.forecast_day1_uv = QLabel(self.forecast_day1)
        self.forecast_day1_uv.setObjectName(u"forecast_day1_uv")
        self.forecast_day1_uv.setFont(font8)

        self.horizontalLayout_31.addWidget(self.forecast_day1_uv)

        self.forecast_day1_uv_label = QLabel(self.forecast_day1)
        self.forecast_day1_uv_label.setObjectName(u"forecast_day1_uv_label")
        self.forecast_day1_uv_label.setFont(font1)

        self.horizontalLayout_31.addWidget(self.forecast_day1_uv_label)

        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 20)

        self.verticalLayout_26.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.forecast_day1_prot_time = QLabel(self.forecast_day1)
        self.forecast_day1_prot_time.setObjectName(u"forecast_day1_prot_time")
        self.forecast_day1_prot_time.setFont(font8)

        self.horizontalLayout_32.addWidget(self.forecast_day1_prot_time)

        self.forecast_day1_prot_rec = QLabel(self.forecast_day1)
        self.forecast_day1_prot_rec.setObjectName(u"forecast_day1_prot_rec")
        self.forecast_day1_prot_rec.setFont(font1)

        self.horizontalLayout_32.addWidget(self.forecast_day1_prot_rec)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 20)

        self.verticalLayout_26.addLayout(self.horizontalLayout_32)


        self.horizontalLayout_28.addLayout(self.verticalLayout_26)


        self.horizontalLayout_16.addWidget(self.forecast_day1)

        self.forecast_day2 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day2.setObjectName(u"forecast_day2")
        self.forecast_day2.setMinimumSize(QSize(600, 100))
        self.forecast_day2.setFont(font1)
        self.forecast_day2.setFrameShape(QFrame.Shape.Box)
        self.forecast_day2.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day2.setLineWidth(2)
        self.horizontalLayout_129 = QHBoxLayout(self.forecast_day2)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.forecast_day2_icon = QLabel(self.forecast_day2)
        self.forecast_day2_icon.setObjectName(u"forecast_day2_icon")
        self.forecast_day2_icon.setMaximumSize(QSize(75, 75))
        self.forecast_day2_icon.setFont(font1)

        self.horizontalLayout_130.addWidget(self.forecast_day2_icon)

        self.forecast_day2_date = QLabel(self.forecast_day2)
        self.forecast_day2_date.setObjectName(u"forecast_day2_date")
        self.forecast_day2_date.setFont(font1)

        self.horizontalLayout_130.addWidget(self.forecast_day2_date)


        self.verticalLayout_43.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.forecast_day2_min_temp = QLabel(self.forecast_day2)
        self.forecast_day2_min_temp.setObjectName(u"forecast_day2_min_temp")
        self.forecast_day2_min_temp.setFont(font1)

        self.horizontalLayout_131.addWidget(self.forecast_day2_min_temp)

        self.forecast_day2_max_temp = QLabel(self.forecast_day2)
        self.forecast_day2_max_temp.setObjectName(u"forecast_day2_max_temp")
        self.forecast_day2_max_temp.setFont(font1)

        self.horizontalLayout_131.addWidget(self.forecast_day2_max_temp)

        self.horizontalLayout_131.setStretch(0, 1)
        self.horizontalLayout_131.setStretch(1, 20)

        self.verticalLayout_43.addLayout(self.horizontalLayout_131)

        self.border_19 = QFrame(self.forecast_day2)
        self.border_19.setObjectName(u"border_19")
        self.border_19.setMinimumSize(QSize(0, 1))
        self.border_19.setMaximumSize(QSize(16777215, 1))
        self.border_19.setFont(font1)
        self.border_19.setFrameShape(QFrame.Shape.Box)
        self.border_19.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_43.addWidget(self.border_19)

        self.label_170 = QLabel(self.forecast_day2)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setFont(font1)

        self.verticalLayout_43.addWidget(self.label_170)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.forecast_day2_chance_of_rain_1 = QLabel(self.forecast_day2)
        self.forecast_day2_chance_of_rain_1.setObjectName(u"forecast_day2_chance_of_rain_1")
        self.forecast_day2_chance_of_rain_1.setFont(font1)

        self.horizontalLayout_132.addWidget(self.forecast_day2_chance_of_rain_1)

        self.forecast_day2_amount_of_rain_1 = QLabel(self.forecast_day2)
        self.forecast_day2_amount_of_rain_1.setObjectName(u"forecast_day2_amount_of_rain_1")
        self.forecast_day2_amount_of_rain_1.setFont(font8)

        self.horizontalLayout_132.addWidget(self.forecast_day2_amount_of_rain_1)

        self.horizontalLayout_132.setStretch(0, 1)
        self.horizontalLayout_132.setStretch(1, 20)

        self.verticalLayout_43.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.forecast_day2_chance_of_rain_2 = QLabel(self.forecast_day2)
        self.forecast_day2_chance_of_rain_2.setObjectName(u"forecast_day2_chance_of_rain_2")
        self.forecast_day2_chance_of_rain_2.setFont(font1)

        self.horizontalLayout_133.addWidget(self.forecast_day2_chance_of_rain_2)

        self.forecast_day2_amount_of_rain_2 = QLabel(self.forecast_day2)
        self.forecast_day2_amount_of_rain_2.setObjectName(u"forecast_day2_amount_of_rain_2")
        self.forecast_day2_amount_of_rain_2.setFont(font8)

        self.horizontalLayout_133.addWidget(self.forecast_day2_amount_of_rain_2)

        self.horizontalLayout_133.setStretch(0, 1)
        self.horizontalLayout_133.setStretch(1, 20)

        self.verticalLayout_43.addLayout(self.horizontalLayout_133)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.forecast_day2_chance_of_rain_3 = QLabel(self.forecast_day2)
        self.forecast_day2_chance_of_rain_3.setObjectName(u"forecast_day2_chance_of_rain_3")

        self.horizontalLayout_22.addWidget(self.forecast_day2_chance_of_rain_3)

        self.forecast_day2_amount_of_rain_3 = QLabel(self.forecast_day2)
        self.forecast_day2_amount_of_rain_3.setObjectName(u"forecast_day2_amount_of_rain_3")
        self.forecast_day2_amount_of_rain_3.setFont(font8)

        self.horizontalLayout_22.addWidget(self.forecast_day2_amount_of_rain_3)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 20)

        self.verticalLayout_43.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_129.addLayout(self.verticalLayout_43)

        self.border_20 = QFrame(self.forecast_day2)
        self.border_20.setObjectName(u"border_20")
        self.border_20.setMinimumSize(QSize(1, 0))
        self.border_20.setMaximumSize(QSize(1, 16777215))
        self.border_20.setFont(font1)
        self.border_20.setFrameShape(QFrame.Shape.Box)
        self.border_20.setFrameShadow(QFrame.Shadow.Plain)
        self.border_20.setLineWidth(10)

        self.horizontalLayout_129.addWidget(self.border_20)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_171 = QLabel(self.forecast_day2)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setFont(font1)

        self.verticalLayout_44.addWidget(self.label_171)

        self.forecast_day2_info = QLabel(self.forecast_day2)
        self.forecast_day2_info.setObjectName(u"forecast_day2_info")
        self.forecast_day2_info.setFont(font1)
        self.forecast_day2_info.setWordWrap(True)

        self.verticalLayout_44.addWidget(self.forecast_day2_info)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.forecast_day2_fire_danger = QLabel(self.forecast_day2)
        self.forecast_day2_fire_danger.setObjectName(u"forecast_day2_fire_danger")
        self.forecast_day2_fire_danger.setFont(font8)

        self.horizontalLayout_134.addWidget(self.forecast_day2_fire_danger)

        self.label_174 = QLabel(self.forecast_day2)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setFont(font1)

        self.horizontalLayout_134.addWidget(self.label_174)

        self.horizontalLayout_134.setStretch(0, 1)
        self.horizontalLayout_134.setStretch(1, 20)

        self.verticalLayout_44.addLayout(self.horizontalLayout_134)

        self.border_21 = QFrame(self.forecast_day2)
        self.border_21.setObjectName(u"border_21")
        self.border_21.setMinimumSize(QSize(0, 1))
        self.border_21.setMaximumSize(QSize(16777215, 1))
        self.border_21.setFont(font1)
        self.border_21.setFrameShape(QFrame.Shape.Box)
        self.border_21.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_44.addWidget(self.border_21)

        self.label_175 = QLabel(self.forecast_day2)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font1)

        self.verticalLayout_44.addWidget(self.label_175)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.forecast_day2_sunrise_time = QLabel(self.forecast_day2)
        self.forecast_day2_sunrise_time.setObjectName(u"forecast_day2_sunrise_time")
        self.forecast_day2_sunrise_time.setFont(font1)

        self.horizontalLayout_135.addWidget(self.forecast_day2_sunrise_time)

        self.forecast_day2_sunset_time = QLabel(self.forecast_day2)
        self.forecast_day2_sunset_time.setObjectName(u"forecast_day2_sunset_time")
        self.forecast_day2_sunset_time.setFont(font1)

        self.horizontalLayout_135.addWidget(self.forecast_day2_sunset_time)

        self.horizontalLayout_135.setStretch(0, 1)
        self.horizontalLayout_135.setStretch(1, 20)

        self.verticalLayout_44.addLayout(self.horizontalLayout_135)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.forecast_day2_uv = QLabel(self.forecast_day2)
        self.forecast_day2_uv.setObjectName(u"forecast_day2_uv")
        self.forecast_day2_uv.setFont(font8)

        self.horizontalLayout_137.addWidget(self.forecast_day2_uv)

        self.forecast_day2_uv_label = QLabel(self.forecast_day2)
        self.forecast_day2_uv_label.setObjectName(u"forecast_day2_uv_label")
        self.forecast_day2_uv_label.setFont(font1)

        self.horizontalLayout_137.addWidget(self.forecast_day2_uv_label)

        self.horizontalLayout_137.setStretch(0, 1)
        self.horizontalLayout_137.setStretch(1, 20)

        self.verticalLayout_44.addLayout(self.horizontalLayout_137)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.forecast_day2_prot_time = QLabel(self.forecast_day2)
        self.forecast_day2_prot_time.setObjectName(u"forecast_day2_prot_time")
        self.forecast_day2_prot_time.setFont(font8)

        self.horizontalLayout_138.addWidget(self.forecast_day2_prot_time)

        self.forecast_day2_prot_rec = QLabel(self.forecast_day2)
        self.forecast_day2_prot_rec.setObjectName(u"forecast_day2_prot_rec")
        self.forecast_day2_prot_rec.setFont(font1)

        self.horizontalLayout_138.addWidget(self.forecast_day2_prot_rec)

        self.horizontalLayout_138.setStretch(0, 1)
        self.horizontalLayout_138.setStretch(1, 20)

        self.verticalLayout_44.addLayout(self.horizontalLayout_138)


        self.horizontalLayout_129.addLayout(self.verticalLayout_44)


        self.horizontalLayout_16.addWidget(self.forecast_day2)

        self.forecast_day3 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day3.setObjectName(u"forecast_day3")
        self.forecast_day3.setMinimumSize(QSize(600, 100))
        self.forecast_day3.setFont(font1)
        self.forecast_day3.setFrameShape(QFrame.Shape.Box)
        self.forecast_day3.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day3.setLineWidth(2)
        self.horizontalLayout_119 = QHBoxLayout(self.forecast_day3)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.forecast_day3_icon = QLabel(self.forecast_day3)
        self.forecast_day3_icon.setObjectName(u"forecast_day3_icon")
        self.forecast_day3_icon.setMaximumSize(QSize(75, 75))
        self.forecast_day3_icon.setFont(font1)

        self.horizontalLayout_120.addWidget(self.forecast_day3_icon)

        self.forecast_day3_date = QLabel(self.forecast_day3)
        self.forecast_day3_date.setObjectName(u"forecast_day3_date")
        self.forecast_day3_date.setFont(font1)

        self.horizontalLayout_120.addWidget(self.forecast_day3_date)


        self.verticalLayout_41.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.forecast_day3_min_temp = QLabel(self.forecast_day3)
        self.forecast_day3_min_temp.setObjectName(u"forecast_day3_min_temp")
        self.forecast_day3_min_temp.setFont(font1)

        self.horizontalLayout_121.addWidget(self.forecast_day3_min_temp)

        self.forecast_day3_max_temp = QLabel(self.forecast_day3)
        self.forecast_day3_max_temp.setObjectName(u"forecast_day3_max_temp")
        self.forecast_day3_max_temp.setFont(font1)

        self.horizontalLayout_121.addWidget(self.forecast_day3_max_temp)

        self.horizontalLayout_121.setStretch(0, 1)
        self.horizontalLayout_121.setStretch(1, 20)

        self.verticalLayout_41.addLayout(self.horizontalLayout_121)

        self.border_16 = QFrame(self.forecast_day3)
        self.border_16.setObjectName(u"border_16")
        self.border_16.setMinimumSize(QSize(0, 1))
        self.border_16.setMaximumSize(QSize(16777215, 1))
        self.border_16.setFont(font1)
        self.border_16.setFrameShape(QFrame.Shape.Box)
        self.border_16.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_41.addWidget(self.border_16)

        self.label_156 = QLabel(self.forecast_day3)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font1)

        self.verticalLayout_41.addWidget(self.label_156)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.forecast_day3_chance_of_rain_1 = QLabel(self.forecast_day3)
        self.forecast_day3_chance_of_rain_1.setObjectName(u"forecast_day3_chance_of_rain_1")
        self.forecast_day3_chance_of_rain_1.setFont(font1)

        self.horizontalLayout_122.addWidget(self.forecast_day3_chance_of_rain_1)

        self.forecast_day3_amount_of_rain_1 = QLabel(self.forecast_day3)
        self.forecast_day3_amount_of_rain_1.setObjectName(u"forecast_day3_amount_of_rain_1")
        self.forecast_day3_amount_of_rain_1.setFont(font8)

        self.horizontalLayout_122.addWidget(self.forecast_day3_amount_of_rain_1)

        self.horizontalLayout_122.setStretch(0, 1)
        self.horizontalLayout_122.setStretch(1, 20)

        self.verticalLayout_41.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.forecast_day3_chance_of_rain_2 = QLabel(self.forecast_day3)
        self.forecast_day3_chance_of_rain_2.setObjectName(u"forecast_day3_chance_of_rain_2")
        self.forecast_day3_chance_of_rain_2.setFont(font1)

        self.horizontalLayout_123.addWidget(self.forecast_day3_chance_of_rain_2)

        self.forecast_day3_amount_of_rain_2 = QLabel(self.forecast_day3)
        self.forecast_day3_amount_of_rain_2.setObjectName(u"forecast_day3_amount_of_rain_2")
        self.forecast_day3_amount_of_rain_2.setFont(font8)

        self.horizontalLayout_123.addWidget(self.forecast_day3_amount_of_rain_2)

        self.horizontalLayout_123.setStretch(0, 1)
        self.horizontalLayout_123.setStretch(1, 20)

        self.verticalLayout_41.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.forecast_day3_chance_of_rain_3 = QLabel(self.forecast_day3)
        self.forecast_day3_chance_of_rain_3.setObjectName(u"forecast_day3_chance_of_rain_3")

        self.horizontalLayout_21.addWidget(self.forecast_day3_chance_of_rain_3)

        self.forecast_day3_amount_of_rain_3 = QLabel(self.forecast_day3)
        self.forecast_day3_amount_of_rain_3.setObjectName(u"forecast_day3_amount_of_rain_3")
        self.forecast_day3_amount_of_rain_3.setFont(font8)

        self.horizontalLayout_21.addWidget(self.forecast_day3_amount_of_rain_3)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 20)

        self.verticalLayout_41.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_119.addLayout(self.verticalLayout_41)

        self.border_17 = QFrame(self.forecast_day3)
        self.border_17.setObjectName(u"border_17")
        self.border_17.setMinimumSize(QSize(1, 0))
        self.border_17.setMaximumSize(QSize(1, 16777215))
        self.border_17.setFont(font1)
        self.border_17.setFrameShape(QFrame.Shape.Box)
        self.border_17.setFrameShadow(QFrame.Shadow.Plain)
        self.border_17.setLineWidth(10)

        self.horizontalLayout_119.addWidget(self.border_17)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_157 = QLabel(self.forecast_day3)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setFont(font1)

        self.verticalLayout_42.addWidget(self.label_157)

        self.forecast_day3_info = QLabel(self.forecast_day3)
        self.forecast_day3_info.setObjectName(u"forecast_day3_info")
        self.forecast_day3_info.setFont(font1)
        self.forecast_day3_info.setWordWrap(True)

        self.verticalLayout_42.addWidget(self.forecast_day3_info)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.forecast_day3_fire_danger = QLabel(self.forecast_day3)
        self.forecast_day3_fire_danger.setObjectName(u"forecast_day3_fire_danger")
        self.forecast_day3_fire_danger.setFont(font8)

        self.horizontalLayout_124.addWidget(self.forecast_day3_fire_danger)

        self.label_160 = QLabel(self.forecast_day3)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font1)

        self.horizontalLayout_124.addWidget(self.label_160)

        self.horizontalLayout_124.setStretch(0, 1)
        self.horizontalLayout_124.setStretch(1, 20)

        self.verticalLayout_42.addLayout(self.horizontalLayout_124)

        self.border_18 = QFrame(self.forecast_day3)
        self.border_18.setObjectName(u"border_18")
        self.border_18.setMinimumSize(QSize(0, 1))
        self.border_18.setMaximumSize(QSize(16777215, 1))
        self.border_18.setFont(font1)
        self.border_18.setFrameShape(QFrame.Shape.Box)
        self.border_18.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_42.addWidget(self.border_18)

        self.label_161 = QLabel(self.forecast_day3)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font1)

        self.verticalLayout_42.addWidget(self.label_161)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.forecast_day3_sunrise_time = QLabel(self.forecast_day3)
        self.forecast_day3_sunrise_time.setObjectName(u"forecast_day3_sunrise_time")
        self.forecast_day3_sunrise_time.setFont(font1)

        self.horizontalLayout_125.addWidget(self.forecast_day3_sunrise_time)

        self.forecast_day3_sunset_time = QLabel(self.forecast_day3)
        self.forecast_day3_sunset_time.setObjectName(u"forecast_day3_sunset_time")
        self.forecast_day3_sunset_time.setFont(font1)

        self.horizontalLayout_125.addWidget(self.forecast_day3_sunset_time)

        self.horizontalLayout_125.setStretch(0, 1)
        self.horizontalLayout_125.setStretch(1, 20)

        self.verticalLayout_42.addLayout(self.horizontalLayout_125)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.forecast_day3_uv = QLabel(self.forecast_day3)
        self.forecast_day3_uv.setObjectName(u"forecast_day3_uv")
        self.forecast_day3_uv.setFont(font8)

        self.horizontalLayout_127.addWidget(self.forecast_day3_uv)

        self.forecast_day3_uv_label = QLabel(self.forecast_day3)
        self.forecast_day3_uv_label.setObjectName(u"forecast_day3_uv_label")
        self.forecast_day3_uv_label.setFont(font1)

        self.horizontalLayout_127.addWidget(self.forecast_day3_uv_label)

        self.horizontalLayout_127.setStretch(0, 1)
        self.horizontalLayout_127.setStretch(1, 20)

        self.verticalLayout_42.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.forecast_day3_prot_time = QLabel(self.forecast_day3)
        self.forecast_day3_prot_time.setObjectName(u"forecast_day3_prot_time")
        self.forecast_day3_prot_time.setFont(font8)

        self.horizontalLayout_128.addWidget(self.forecast_day3_prot_time)

        self.forecast_day3_prot_rec = QLabel(self.forecast_day3)
        self.forecast_day3_prot_rec.setObjectName(u"forecast_day3_prot_rec")
        self.forecast_day3_prot_rec.setFont(font1)

        self.horizontalLayout_128.addWidget(self.forecast_day3_prot_rec)

        self.horizontalLayout_128.setStretch(0, 1)
        self.horizontalLayout_128.setStretch(1, 20)

        self.verticalLayout_42.addLayout(self.horizontalLayout_128)


        self.horizontalLayout_119.addLayout(self.verticalLayout_42)


        self.horizontalLayout_16.addWidget(self.forecast_day3)

        self.forecast_day4 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day4.setObjectName(u"forecast_day4")
        self.forecast_day4.setMinimumSize(QSize(600, 100))
        self.forecast_day4.setFont(font1)
        self.forecast_day4.setFrameShape(QFrame.Shape.Box)
        self.forecast_day4.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day4.setLineWidth(2)
        self.horizontalLayout_109 = QHBoxLayout(self.forecast_day4)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.forecast_day4_icon = QLabel(self.forecast_day4)
        self.forecast_day4_icon.setObjectName(u"forecast_day4_icon")
        self.forecast_day4_icon.setMaximumSize(QSize(75, 75))
        self.forecast_day4_icon.setFont(font1)

        self.horizontalLayout_110.addWidget(self.forecast_day4_icon)

        self.forecast_day4_date = QLabel(self.forecast_day4)
        self.forecast_day4_date.setObjectName(u"forecast_day4_date")
        self.forecast_day4_date.setFont(font1)

        self.horizontalLayout_110.addWidget(self.forecast_day4_date)


        self.verticalLayout_39.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.forecast_day4_min_temp = QLabel(self.forecast_day4)
        self.forecast_day4_min_temp.setObjectName(u"forecast_day4_min_temp")
        self.forecast_day4_min_temp.setFont(font1)

        self.horizontalLayout_111.addWidget(self.forecast_day4_min_temp)

        self.forecast_day4_max_temp = QLabel(self.forecast_day4)
        self.forecast_day4_max_temp.setObjectName(u"forecast_day4_max_temp")
        self.forecast_day4_max_temp.setFont(font1)

        self.horizontalLayout_111.addWidget(self.forecast_day4_max_temp)

        self.horizontalLayout_111.setStretch(0, 1)
        self.horizontalLayout_111.setStretch(1, 20)

        self.verticalLayout_39.addLayout(self.horizontalLayout_111)

        self.border_13 = QFrame(self.forecast_day4)
        self.border_13.setObjectName(u"border_13")
        self.border_13.setMinimumSize(QSize(0, 1))
        self.border_13.setMaximumSize(QSize(16777215, 1))
        self.border_13.setFont(font1)
        self.border_13.setFrameShape(QFrame.Shape.Box)
        self.border_13.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_39.addWidget(self.border_13)

        self.label_142 = QLabel(self.forecast_day4)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setFont(font1)

        self.verticalLayout_39.addWidget(self.label_142)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.forecast_day4_chance_of_rain_1 = QLabel(self.forecast_day4)
        self.forecast_day4_chance_of_rain_1.setObjectName(u"forecast_day4_chance_of_rain_1")
        self.forecast_day4_chance_of_rain_1.setFont(font1)

        self.horizontalLayout_112.addWidget(self.forecast_day4_chance_of_rain_1)

        self.forecast_day4_amount_of_rain_1 = QLabel(self.forecast_day4)
        self.forecast_day4_amount_of_rain_1.setObjectName(u"forecast_day4_amount_of_rain_1")
        self.forecast_day4_amount_of_rain_1.setFont(font8)

        self.horizontalLayout_112.addWidget(self.forecast_day4_amount_of_rain_1)

        self.horizontalLayout_112.setStretch(0, 1)
        self.horizontalLayout_112.setStretch(1, 20)

        self.verticalLayout_39.addLayout(self.horizontalLayout_112)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.forecast_day4_chance_of_rain_2 = QLabel(self.forecast_day4)
        self.forecast_day4_chance_of_rain_2.setObjectName(u"forecast_day4_chance_of_rain_2")
        self.forecast_day4_chance_of_rain_2.setFont(font1)

        self.horizontalLayout_113.addWidget(self.forecast_day4_chance_of_rain_2)

        self.forecast_day4_amount_of_rain_2 = QLabel(self.forecast_day4)
        self.forecast_day4_amount_of_rain_2.setObjectName(u"forecast_day4_amount_of_rain_2")
        self.forecast_day4_amount_of_rain_2.setFont(font8)

        self.horizontalLayout_113.addWidget(self.forecast_day4_amount_of_rain_2)

        self.horizontalLayout_113.setStretch(0, 1)
        self.horizontalLayout_113.setStretch(1, 20)

        self.verticalLayout_39.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.forecast_day4_chance_of_rain_3 = QLabel(self.forecast_day4)
        self.forecast_day4_chance_of_rain_3.setObjectName(u"forecast_day4_chance_of_rain_3")

        self.horizontalLayout_23.addWidget(self.forecast_day4_chance_of_rain_3)

        self.forecast_day4_amount_of_rain_3 = QLabel(self.forecast_day4)
        self.forecast_day4_amount_of_rain_3.setObjectName(u"forecast_day4_amount_of_rain_3")
        self.forecast_day4_amount_of_rain_3.setFont(font8)

        self.horizontalLayout_23.addWidget(self.forecast_day4_amount_of_rain_3)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 20)

        self.verticalLayout_39.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_109.addLayout(self.verticalLayout_39)

        self.border_14 = QFrame(self.forecast_day4)
        self.border_14.setObjectName(u"border_14")
        self.border_14.setMinimumSize(QSize(1, 0))
        self.border_14.setMaximumSize(QSize(1, 16777215))
        self.border_14.setFont(font1)
        self.border_14.setFrameShape(QFrame.Shape.Box)
        self.border_14.setFrameShadow(QFrame.Shadow.Plain)
        self.border_14.setLineWidth(10)

        self.horizontalLayout_109.addWidget(self.border_14)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_143 = QLabel(self.forecast_day4)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font1)

        self.verticalLayout_40.addWidget(self.label_143)

        self.forecast_day4_info = QLabel(self.forecast_day4)
        self.forecast_day4_info.setObjectName(u"forecast_day4_info")
        self.forecast_day4_info.setFont(font1)
        self.forecast_day4_info.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.forecast_day4_info)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.forecast_day4_fire_danger = QLabel(self.forecast_day4)
        self.forecast_day4_fire_danger.setObjectName(u"forecast_day4_fire_danger")
        self.forecast_day4_fire_danger.setFont(font8)

        self.horizontalLayout_114.addWidget(self.forecast_day4_fire_danger)

        self.label_146 = QLabel(self.forecast_day4)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font1)

        self.horizontalLayout_114.addWidget(self.label_146)

        self.horizontalLayout_114.setStretch(0, 1)
        self.horizontalLayout_114.setStretch(1, 20)

        self.verticalLayout_40.addLayout(self.horizontalLayout_114)

        self.border_15 = QFrame(self.forecast_day4)
        self.border_15.setObjectName(u"border_15")
        self.border_15.setMinimumSize(QSize(0, 1))
        self.border_15.setMaximumSize(QSize(16777215, 1))
        self.border_15.setFont(font1)
        self.border_15.setFrameShape(QFrame.Shape.Box)
        self.border_15.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_40.addWidget(self.border_15)

        self.label_147 = QLabel(self.forecast_day4)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font1)

        self.verticalLayout_40.addWidget(self.label_147)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.forecast_day4_sunrise_time = QLabel(self.forecast_day4)
        self.forecast_day4_sunrise_time.setObjectName(u"forecast_day4_sunrise_time")
        self.forecast_day4_sunrise_time.setFont(font1)

        self.horizontalLayout_115.addWidget(self.forecast_day4_sunrise_time)

        self.forecast_day4_sunset_time = QLabel(self.forecast_day4)
        self.forecast_day4_sunset_time.setObjectName(u"forecast_day4_sunset_time")
        self.forecast_day4_sunset_time.setFont(font1)

        self.horizontalLayout_115.addWidget(self.forecast_day4_sunset_time)

        self.horizontalLayout_115.setStretch(0, 1)
        self.horizontalLayout_115.setStretch(1, 20)

        self.verticalLayout_40.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.forecast_day4_uv = QLabel(self.forecast_day4)
        self.forecast_day4_uv.setObjectName(u"forecast_day4_uv")
        self.forecast_day4_uv.setFont(font8)

        self.horizontalLayout_117.addWidget(self.forecast_day4_uv)

        self.forecast_day4_uv_label = QLabel(self.forecast_day4)
        self.forecast_day4_uv_label.setObjectName(u"forecast_day4_uv_label")
        self.forecast_day4_uv_label.setFont(font1)

        self.horizontalLayout_117.addWidget(self.forecast_day4_uv_label)

        self.horizontalLayout_117.setStretch(0, 1)
        self.horizontalLayout_117.setStretch(1, 20)

        self.verticalLayout_40.addLayout(self.horizontalLayout_117)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.forecast_day4_prot_time = QLabel(self.forecast_day4)
        self.forecast_day4_prot_time.setObjectName(u"forecast_day4_prot_time")
        self.forecast_day4_prot_time.setFont(font8)

        self.horizontalLayout_118.addWidget(self.forecast_day4_prot_time)

        self.forecast_day4_prot_rec = QLabel(self.forecast_day4)
        self.forecast_day4_prot_rec.setObjectName(u"forecast_day4_prot_rec")
        self.forecast_day4_prot_rec.setFont(font1)

        self.horizontalLayout_118.addWidget(self.forecast_day4_prot_rec)

        self.horizontalLayout_118.setStretch(0, 1)
        self.horizontalLayout_118.setStretch(1, 20)

        self.verticalLayout_40.addLayout(self.horizontalLayout_118)


        self.horizontalLayout_109.addLayout(self.verticalLayout_40)


        self.horizontalLayout_16.addWidget(self.forecast_day4)

        self.forecast_day5 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day5.setObjectName(u"forecast_day5")
        self.forecast_day5.setMinimumSize(QSize(600, 100))
        self.forecast_day5.setFont(font1)
        self.forecast_day5.setFrameShape(QFrame.Shape.Box)
        self.forecast_day5.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day5.setLineWidth(2)
        self.horizontalLayout_99 = QHBoxLayout(self.forecast_day5)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.forecast_day5_icon = QLabel(self.forecast_day5)
        self.forecast_day5_icon.setObjectName(u"forecast_day5_icon")
        self.forecast_day5_icon.setMaximumSize(QSize(75, 75))
        self.forecast_day5_icon.setFont(font1)

        self.horizontalLayout_100.addWidget(self.forecast_day5_icon)

        self.forecast_day5_date = QLabel(self.forecast_day5)
        self.forecast_day5_date.setObjectName(u"forecast_day5_date")
        self.forecast_day5_date.setFont(font1)

        self.horizontalLayout_100.addWidget(self.forecast_day5_date)


        self.verticalLayout_37.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.forecast_day5_min_temp = QLabel(self.forecast_day5)
        self.forecast_day5_min_temp.setObjectName(u"forecast_day5_min_temp")
        self.forecast_day5_min_temp.setFont(font1)

        self.horizontalLayout_101.addWidget(self.forecast_day5_min_temp)

        self.forecast_day5_max_temp = QLabel(self.forecast_day5)
        self.forecast_day5_max_temp.setObjectName(u"forecast_day5_max_temp")
        self.forecast_day5_max_temp.setFont(font1)

        self.horizontalLayout_101.addWidget(self.forecast_day5_max_temp)

        self.horizontalLayout_101.setStretch(0, 1)
        self.horizontalLayout_101.setStretch(1, 20)

        self.verticalLayout_37.addLayout(self.horizontalLayout_101)

        self.border_10 = QFrame(self.forecast_day5)
        self.border_10.setObjectName(u"border_10")
        self.border_10.setMinimumSize(QSize(0, 1))
        self.border_10.setMaximumSize(QSize(16777215, 1))
        self.border_10.setFont(font1)
        self.border_10.setFrameShape(QFrame.Shape.Box)
        self.border_10.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_37.addWidget(self.border_10)

        self.label_128 = QLabel(self.forecast_day5)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font1)

        self.verticalLayout_37.addWidget(self.label_128)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.forecast_day5_chance_of_rain_1 = QLabel(self.forecast_day5)
        self.forecast_day5_chance_of_rain_1.setObjectName(u"forecast_day5_chance_of_rain_1")
        self.forecast_day5_chance_of_rain_1.setFont(font1)

        self.horizontalLayout_102.addWidget(self.forecast_day5_chance_of_rain_1)

        self.forecast_day5_amount_of_rain_1 = QLabel(self.forecast_day5)
        self.forecast_day5_amount_of_rain_1.setObjectName(u"forecast_day5_amount_of_rain_1")
        self.forecast_day5_amount_of_rain_1.setFont(font8)

        self.horizontalLayout_102.addWidget(self.forecast_day5_amount_of_rain_1)

        self.horizontalLayout_102.setStretch(0, 1)
        self.horizontalLayout_102.setStretch(1, 20)

        self.verticalLayout_37.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.forecast_day5_chance_of_rain_2 = QLabel(self.forecast_day5)
        self.forecast_day5_chance_of_rain_2.setObjectName(u"forecast_day5_chance_of_rain_2")
        self.forecast_day5_chance_of_rain_2.setFont(font1)

        self.horizontalLayout_103.addWidget(self.forecast_day5_chance_of_rain_2)

        self.forecast_day5_amount_of_rain_2 = QLabel(self.forecast_day5)
        self.forecast_day5_amount_of_rain_2.setObjectName(u"forecast_day5_amount_of_rain_2")
        self.forecast_day5_amount_of_rain_2.setFont(font8)

        self.horizontalLayout_103.addWidget(self.forecast_day5_amount_of_rain_2)

        self.horizontalLayout_103.setStretch(0, 1)
        self.horizontalLayout_103.setStretch(1, 20)

        self.verticalLayout_37.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.forecast_day5_chance_of_rain_3 = QLabel(self.forecast_day5)
        self.forecast_day5_chance_of_rain_3.setObjectName(u"forecast_day5_chance_of_rain_3")

        self.horizontalLayout_33.addWidget(self.forecast_day5_chance_of_rain_3)

        self.forecast_day5_amount_of_rain_3 = QLabel(self.forecast_day5)
        self.forecast_day5_amount_of_rain_3.setObjectName(u"forecast_day5_amount_of_rain_3")
        self.forecast_day5_amount_of_rain_3.setFont(font8)

        self.horizontalLayout_33.addWidget(self.forecast_day5_amount_of_rain_3)

        self.horizontalLayout_33.setStretch(0, 1)
        self.horizontalLayout_33.setStretch(1, 20)

        self.verticalLayout_37.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_99.addLayout(self.verticalLayout_37)

        self.border_11 = QFrame(self.forecast_day5)
        self.border_11.setObjectName(u"border_11")
        self.border_11.setMinimumSize(QSize(1, 0))
        self.border_11.setMaximumSize(QSize(1, 16777215))
        self.border_11.setFont(font1)
        self.border_11.setFrameShape(QFrame.Shape.Box)
        self.border_11.setFrameShadow(QFrame.Shadow.Plain)
        self.border_11.setLineWidth(10)

        self.horizontalLayout_99.addWidget(self.border_11)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_129 = QLabel(self.forecast_day5)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font1)

        self.verticalLayout_38.addWidget(self.label_129)

        self.forecast_day5_info = QLabel(self.forecast_day5)
        self.forecast_day5_info.setObjectName(u"forecast_day5_info")
        self.forecast_day5_info.setFont(font1)
        self.forecast_day5_info.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.forecast_day5_info)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.forecast_day5_fire_danger = QLabel(self.forecast_day5)
        self.forecast_day5_fire_danger.setObjectName(u"forecast_day5_fire_danger")
        self.forecast_day5_fire_danger.setFont(font8)

        self.horizontalLayout_104.addWidget(self.forecast_day5_fire_danger)

        self.label_132 = QLabel(self.forecast_day5)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font1)

        self.horizontalLayout_104.addWidget(self.label_132)

        self.horizontalLayout_104.setStretch(0, 1)
        self.horizontalLayout_104.setStretch(1, 20)

        self.verticalLayout_38.addLayout(self.horizontalLayout_104)

        self.border_12 = QFrame(self.forecast_day5)
        self.border_12.setObjectName(u"border_12")
        self.border_12.setMinimumSize(QSize(0, 1))
        self.border_12.setMaximumSize(QSize(16777215, 1))
        self.border_12.setFont(font1)
        self.border_12.setFrameShape(QFrame.Shape.Box)
        self.border_12.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_38.addWidget(self.border_12)

        self.label_133 = QLabel(self.forecast_day5)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font1)

        self.verticalLayout_38.addWidget(self.label_133)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.forecast_day5_sunrise_time = QLabel(self.forecast_day5)
        self.forecast_day5_sunrise_time.setObjectName(u"forecast_day5_sunrise_time")
        self.forecast_day5_sunrise_time.setFont(font1)

        self.horizontalLayout_105.addWidget(self.forecast_day5_sunrise_time)

        self.forecast_day5_sunset_time = QLabel(self.forecast_day5)
        self.forecast_day5_sunset_time.setObjectName(u"forecast_day5_sunset_time")
        self.forecast_day5_sunset_time.setFont(font1)

        self.horizontalLayout_105.addWidget(self.forecast_day5_sunset_time)

        self.horizontalLayout_105.setStretch(0, 1)
        self.horizontalLayout_105.setStretch(1, 20)

        self.verticalLayout_38.addLayout(self.horizontalLayout_105)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.forecast_day5_uv = QLabel(self.forecast_day5)
        self.forecast_day5_uv.setObjectName(u"forecast_day5_uv")
        self.forecast_day5_uv.setFont(font8)

        self.horizontalLayout_107.addWidget(self.forecast_day5_uv)

        self.forecast_day5_uv_label = QLabel(self.forecast_day5)
        self.forecast_day5_uv_label.setObjectName(u"forecast_day5_uv_label")
        self.forecast_day5_uv_label.setFont(font1)

        self.horizontalLayout_107.addWidget(self.forecast_day5_uv_label)

        self.horizontalLayout_107.setStretch(0, 1)
        self.horizontalLayout_107.setStretch(1, 20)

        self.verticalLayout_38.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.forecast_day5_prot_time = QLabel(self.forecast_day5)
        self.forecast_day5_prot_time.setObjectName(u"forecast_day5_prot_time")
        self.forecast_day5_prot_time.setFont(font8)

        self.horizontalLayout_108.addWidget(self.forecast_day5_prot_time)

        self.forecast_day5_prot_rec = QLabel(self.forecast_day5)
        self.forecast_day5_prot_rec.setObjectName(u"forecast_day5_prot_rec")
        self.forecast_day5_prot_rec.setFont(font1)

        self.horizontalLayout_108.addWidget(self.forecast_day5_prot_rec)

        self.horizontalLayout_108.setStretch(0, 1)
        self.horizontalLayout_108.setStretch(1, 20)

        self.verticalLayout_38.addLayout(self.horizontalLayout_108)


        self.horizontalLayout_99.addLayout(self.verticalLayout_38)


        self.horizontalLayout_16.addWidget(self.forecast_day5)

        self.forecast_day6 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day6.setObjectName(u"forecast_day6")
        self.forecast_day6.setMinimumSize(QSize(600, 100))
        self.forecast_day6.setFont(font1)
        self.forecast_day6.setFrameShape(QFrame.Shape.Box)
        self.forecast_day6.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day6.setLineWidth(2)
        self.horizontalLayout_89 = QHBoxLayout(self.forecast_day6)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.forecast_day6_icon = QLabel(self.forecast_day6)
        self.forecast_day6_icon.setObjectName(u"forecast_day6_icon")
        self.forecast_day6_icon.setMaximumSize(QSize(75, 75))
        self.forecast_day6_icon.setFont(font1)

        self.horizontalLayout_90.addWidget(self.forecast_day6_icon)

        self.forecast_day6_date = QLabel(self.forecast_day6)
        self.forecast_day6_date.setObjectName(u"forecast_day6_date")
        self.forecast_day6_date.setFont(font1)

        self.horizontalLayout_90.addWidget(self.forecast_day6_date)


        self.verticalLayout_35.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.forecast_day6_min_temp = QLabel(self.forecast_day6)
        self.forecast_day6_min_temp.setObjectName(u"forecast_day6_min_temp")
        self.forecast_day6_min_temp.setFont(font1)

        self.horizontalLayout_91.addWidget(self.forecast_day6_min_temp)

        self.forecast_day6_max_temp = QLabel(self.forecast_day6)
        self.forecast_day6_max_temp.setObjectName(u"forecast_day6_max_temp")
        self.forecast_day6_max_temp.setFont(font1)

        self.horizontalLayout_91.addWidget(self.forecast_day6_max_temp)

        self.horizontalLayout_91.setStretch(0, 1)
        self.horizontalLayout_91.setStretch(1, 20)

        self.verticalLayout_35.addLayout(self.horizontalLayout_91)

        self.border_7 = QFrame(self.forecast_day6)
        self.border_7.setObjectName(u"border_7")
        self.border_7.setMinimumSize(QSize(0, 1))
        self.border_7.setMaximumSize(QSize(16777215, 1))
        self.border_7.setFont(font1)
        self.border_7.setFrameShape(QFrame.Shape.Box)
        self.border_7.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_35.addWidget(self.border_7)

        self.label_114 = QLabel(self.forecast_day6)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font1)

        self.verticalLayout_35.addWidget(self.label_114)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.forecast_day6_chance_of_rain_1 = QLabel(self.forecast_day6)
        self.forecast_day6_chance_of_rain_1.setObjectName(u"forecast_day6_chance_of_rain_1")
        self.forecast_day6_chance_of_rain_1.setFont(font1)

        self.horizontalLayout_92.addWidget(self.forecast_day6_chance_of_rain_1)

        self.forecast_day6_amount_of_rain_1 = QLabel(self.forecast_day6)
        self.forecast_day6_amount_of_rain_1.setObjectName(u"forecast_day6_amount_of_rain_1")
        self.forecast_day6_amount_of_rain_1.setFont(font8)

        self.horizontalLayout_92.addWidget(self.forecast_day6_amount_of_rain_1)

        self.horizontalLayout_92.setStretch(0, 1)
        self.horizontalLayout_92.setStretch(1, 20)

        self.verticalLayout_35.addLayout(self.horizontalLayout_92)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.forecast_day6_chance_of_rain_2 = QLabel(self.forecast_day6)
        self.forecast_day6_chance_of_rain_2.setObjectName(u"forecast_day6_chance_of_rain_2")
        self.forecast_day6_chance_of_rain_2.setFont(font1)

        self.horizontalLayout_93.addWidget(self.forecast_day6_chance_of_rain_2)

        self.forecast_day6_amount_of_rain_2 = QLabel(self.forecast_day6)
        self.forecast_day6_amount_of_rain_2.setObjectName(u"forecast_day6_amount_of_rain_2")
        self.forecast_day6_amount_of_rain_2.setFont(font8)

        self.horizontalLayout_93.addWidget(self.forecast_day6_amount_of_rain_2)

        self.horizontalLayout_93.setStretch(0, 1)
        self.horizontalLayout_93.setStretch(1, 20)

        self.verticalLayout_35.addLayout(self.horizontalLayout_93)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.forecast_day6_chance_of_rain_3 = QLabel(self.forecast_day6)
        self.forecast_day6_chance_of_rain_3.setObjectName(u"forecast_day6_chance_of_rain_3")

        self.horizontalLayout_34.addWidget(self.forecast_day6_chance_of_rain_3)

        self.forecast_day6_amount_of_rain_3 = QLabel(self.forecast_day6)
        self.forecast_day6_amount_of_rain_3.setObjectName(u"forecast_day6_amount_of_rain_3")
        self.forecast_day6_amount_of_rain_3.setFont(font8)

        self.horizontalLayout_34.addWidget(self.forecast_day6_amount_of_rain_3)

        self.horizontalLayout_34.setStretch(0, 1)
        self.horizontalLayout_34.setStretch(1, 20)

        self.verticalLayout_35.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_89.addLayout(self.verticalLayout_35)

        self.border_8 = QFrame(self.forecast_day6)
        self.border_8.setObjectName(u"border_8")
        self.border_8.setMinimumSize(QSize(1, 0))
        self.border_8.setMaximumSize(QSize(1, 16777215))
        self.border_8.setFont(font1)
        self.border_8.setFrameShape(QFrame.Shape.Box)
        self.border_8.setFrameShadow(QFrame.Shadow.Plain)
        self.border_8.setLineWidth(10)

        self.horizontalLayout_89.addWidget(self.border_8)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_115 = QLabel(self.forecast_day6)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font1)

        self.verticalLayout_36.addWidget(self.label_115)

        self.forecast_day6_info = QLabel(self.forecast_day6)
        self.forecast_day6_info.setObjectName(u"forecast_day6_info")
        self.forecast_day6_info.setFont(font1)
        self.forecast_day6_info.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.forecast_day6_info)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.forecast_day6_fire_danger = QLabel(self.forecast_day6)
        self.forecast_day6_fire_danger.setObjectName(u"forecast_day6_fire_danger")
        self.forecast_day6_fire_danger.setFont(font8)

        self.horizontalLayout_94.addWidget(self.forecast_day6_fire_danger)

        self.label_118 = QLabel(self.forecast_day6)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font1)

        self.horizontalLayout_94.addWidget(self.label_118)

        self.horizontalLayout_94.setStretch(0, 1)
        self.horizontalLayout_94.setStretch(1, 20)

        self.verticalLayout_36.addLayout(self.horizontalLayout_94)

        self.border_9 = QFrame(self.forecast_day6)
        self.border_9.setObjectName(u"border_9")
        self.border_9.setMinimumSize(QSize(0, 1))
        self.border_9.setMaximumSize(QSize(16777215, 1))
        self.border_9.setFont(font1)
        self.border_9.setFrameShape(QFrame.Shape.Box)
        self.border_9.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_36.addWidget(self.border_9)

        self.label_119 = QLabel(self.forecast_day6)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font1)

        self.verticalLayout_36.addWidget(self.label_119)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.forecast_day6_sunrise_time = QLabel(self.forecast_day6)
        self.forecast_day6_sunrise_time.setObjectName(u"forecast_day6_sunrise_time")
        self.forecast_day6_sunrise_time.setFont(font1)

        self.horizontalLayout_95.addWidget(self.forecast_day6_sunrise_time)

        self.forecast_day6_sunset_time = QLabel(self.forecast_day6)
        self.forecast_day6_sunset_time.setObjectName(u"forecast_day6_sunset_time")
        self.forecast_day6_sunset_time.setFont(font1)

        self.horizontalLayout_95.addWidget(self.forecast_day6_sunset_time)

        self.horizontalLayout_95.setStretch(0, 1)
        self.horizontalLayout_95.setStretch(1, 20)

        self.verticalLayout_36.addLayout(self.horizontalLayout_95)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.forecast_day6_uv = QLabel(self.forecast_day6)
        self.forecast_day6_uv.setObjectName(u"forecast_day6_uv")
        self.forecast_day6_uv.setFont(font8)

        self.horizontalLayout_97.addWidget(self.forecast_day6_uv)

        self.forecast_day6_uv_label = QLabel(self.forecast_day6)
        self.forecast_day6_uv_label.setObjectName(u"forecast_day6_uv_label")
        self.forecast_day6_uv_label.setFont(font1)

        self.horizontalLayout_97.addWidget(self.forecast_day6_uv_label)

        self.horizontalLayout_97.setStretch(0, 1)
        self.horizontalLayout_97.setStretch(1, 20)

        self.verticalLayout_36.addLayout(self.horizontalLayout_97)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.forecast_day6_prot_time = QLabel(self.forecast_day6)
        self.forecast_day6_prot_time.setObjectName(u"forecast_day6_prot_time")
        self.forecast_day6_prot_time.setFont(font8)

        self.horizontalLayout_98.addWidget(self.forecast_day6_prot_time)

        self.forecast_day6_prot_rec = QLabel(self.forecast_day6)
        self.forecast_day6_prot_rec.setObjectName(u"forecast_day6_prot_rec")
        self.forecast_day6_prot_rec.setFont(font1)

        self.horizontalLayout_98.addWidget(self.forecast_day6_prot_rec)

        self.horizontalLayout_98.setStretch(0, 1)
        self.horizontalLayout_98.setStretch(1, 20)

        self.verticalLayout_36.addLayout(self.horizontalLayout_98)


        self.horizontalLayout_89.addLayout(self.verticalLayout_36)


        self.horizontalLayout_16.addWidget(self.forecast_day6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)

        self.forecast_info_table = QTableWidget(self.forecast_weather)
        self.forecast_info_table.setObjectName(u"forecast_info_table")
        self.forecast_info_table.setFont(font1)

        self.verticalLayout_20.addWidget(self.forecast_info_table)

        self.tabWidget.addTab(self.forecast_weather, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_22 = QVBoxLayout(self.settings)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        font10 = QFont()
        font10.setFamilies([u"Sans Serif"])
        font10.setPointSize(25)
        font10.setBold(True)
        font10.setItalic(False)
        self.label_3.setFont(font10)

        self.verticalLayout_22.addWidget(self.label_3)

        self.label_2 = QLabel(self.settings)
        self.label_2.setObjectName(u"label_2")
        font11 = QFont()
        font11.setFamilies([u"Sans Serif"])
        font11.setPointSize(15)
        font11.setBold(True)
        font11.setItalic(False)
        self.label_2.setFont(font11)

        self.verticalLayout_22.addWidget(self.label_2)

        self.label_5 = QLabel(self.settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font8)

        self.verticalLayout_22.addWidget(self.label_5)

        self.ws_unit_button_kmh = QRadioButton(self.settings)
        self.ws_unit_button_kmh.setObjectName(u"ws_unit_button_kmh")

        self.verticalLayout_22.addWidget(self.ws_unit_button_kmh)

        self.ws_unit_button_knots = QRadioButton(self.settings)
        self.ws_unit_button_knots.setObjectName(u"ws_unit_button_knots")

        self.verticalLayout_22.addWidget(self.ws_unit_button_knots)

        self.widget = QWidget(self.settings)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_22.addWidget(self.widget)

        self.verticalLayout_22.setStretch(5, 100)
        self.tabWidget.addTab(self.settings, "")

        self.verticalLayout.addWidget(self.tabWidget)

        WeatherApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(WeatherApp)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WeatherApp)
    # setupUi

    def retranslateUi(self, WeatherApp):
        WeatherApp.setWindowTitle(QCoreApplication.translate("WeatherApp", u"MainWindow", None))
        self.location_input.setPlaceholderText(QCoreApplication.translate("WeatherApp", u"Enter Your Location Here", None))
        self.get_weather_button.setText(QCoreApplication.translate("WeatherApp", u"Get Weather", None))
        self.place_overview.setText(QCoreApplication.translate("WeatherApp", u"Place", None))
        self.current_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"X\u00b0", None))
        self.current_day_icon_overview.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.current_condtions_overview.setText(QCoreApplication.translate("WeatherApp", u"Sunny", None))
        self.min_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"Min: x\u00b0", None))
        self.max_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"Max: y\u00b0", None))
        self.feels_like_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"Feels like: x\u00b0", None))
        self.day1_overview.setText(QCoreApplication.translate("WeatherApp", u"Day1", None))
        self.day2_overview.setText(QCoreApplication.translate("WeatherApp", u"Day2", None))
        self.day3_overview.setText(QCoreApplication.translate("WeatherApp", u"Day3", None))
        self.day4_overview.setText(QCoreApplication.translate("WeatherApp", u"Day 4", None))
        self.day5_overview.setText(QCoreApplication.translate("WeatherApp", u"Day5", None))
        self.icon_overview1.setText("")
        self.icon_chance_of_rain1.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview2.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain2.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview3.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain3.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview4.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain4.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview5.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain5.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.day1_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day2_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day3_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day4_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day5_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("WeatherApp", u"UV Index", None))
        self.max_uv_overview.setText(QCoreApplication.translate("WeatherApp", u"Max UV:", None))
        self.sun_protection_recommended_overview.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection recommended:", None))
        self.protection_time_overview.setText(QCoreApplication.translate("WeatherApp", u"xx:xxam to xx:xxpm", None))
        self.sunrise_overview.setText(QCoreApplication.translate("WeatherApp", u"Sunrise: xx:xx", None))
        self.sunset_overview.setText(QCoreApplication.translate("WeatherApp", u"Sunset: xx:xx", None))
        self.label_6.setText(QCoreApplication.translate("WeatherApp", u"Forecasted Amount of Rain Today: ", None))
        self.forecast_amount_of_rain_overview.setText(QCoreApplication.translate("WeatherApp", u"x-xmm", None))
        self.label_4.setText(QCoreApplication.translate("WeatherApp", u"Chance of Rain Today: ", None))
        self.chance_of_rain_overview.setText(QCoreApplication.translate("WeatherApp", u"x%", None))
        self.label.setText(QCoreApplication.translate("WeatherApp", u"N", None))
        self.label_25.setText(QCoreApplication.translate("WeatherApp", u"Current Wind Speed", None))
        self.wind_speed_overview.setText(QCoreApplication.translate("WeatherApp", u"xxkm/h direction", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overview), QCoreApplication.translate("WeatherApp", u"Overview", None))
        self.highlights_gust_speed.setText(QCoreApplication.translate("WeatherApp", u"XXkm/h", None))
        self.highlights_gust_speed_time.setText(QCoreApplication.translate("WeatherApp", u"at xx:xx", None))
        self.label_35.setText(QCoreApplication.translate("WeatherApp", u"Highest Wind Gust", None))
        self.highlights_max_temp.setText(QCoreApplication.translate("WeatherApp", u"XX\u00b0", None))
        self.highlights_max_temp_time.setText(QCoreApplication.translate("WeatherApp", u"at xx:xx", None))
        self.label_29.setText(QCoreApplication.translate("WeatherApp", u"Highest Temperature", None))
        self.highlights_rain_since_9am.setText(QCoreApplication.translate("WeatherApp", u"Xmm", None))
        self.label_37.setText(QCoreApplication.translate("WeatherApp", u"since 9am", None))
        self.label_38.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.highlights_min_temp.setText(QCoreApplication.translate("WeatherApp", u"XX\u00b0", None))
        self.highlights_min_temp_time.setText(QCoreApplication.translate("WeatherApp", u"at xx:xx", None))
        self.label_32.setText(QCoreApplication.translate("WeatherApp", u"Lowest Temperature", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.past_weather), QCoreApplication.translate("WeatherApp", u"Past", None))
        self.forecast_day1_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day1_date.setText(QCoreApplication.translate("WeatherApp", u"Today 26 September", None))
        self.forecast_day1_min_temp.setText(QCoreApplication.translate("WeatherApp", u"x\u00b0 Min", None))
        self.forecast_day1_max_temp.setText(QCoreApplication.translate("WeatherApp", u"y\u00b0 Max", None))
        self.label_9.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.forecast_day1_chance_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"25% chance of ", None))
        self.forecast_day1_amount_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"at least 5mm of rain", None))
        self.forecast_day1_chance_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"50% chance of", None))
        self.forecast_day1_amount_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"at least 2mm of rain", None))
        self.forecast_day1_chance_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"75% chance of ", None))
        self.forecast_day1_amount_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"at least 1mm of rain", None))
        self.label_14.setText(QCoreApplication.translate("WeatherApp", u"General Info", None))
        self.forecast_day1_info.setText(QCoreApplication.translate("WeatherApp", u"Cloudy today with light shows in the morning. Will clear up in the afternoon", None))
        self.forecast_day1_fire_danger.setText(QCoreApplication.translate("WeatherApp", u"No", None))
        self.label_16.setText(QCoreApplication.translate("WeatherApp", u"Fire danger rating", None))
        self.label_19.setText(QCoreApplication.translate("WeatherApp", u"Sun and UV", None))
        self.forecast_day1_sunrise_time.setText(QCoreApplication.translate("WeatherApp", u"6:00am Sunrise", None))
        self.forecast_day1_sunset_time.setText(QCoreApplication.translate("WeatherApp", u"6:30pm Sunset", None))
        self.forecast_day1_uv.setText(QCoreApplication.translate("WeatherApp", u"5 (Moderate)", None))
        self.forecast_day1_uv_label.setText(QCoreApplication.translate("WeatherApp", u"Max UV index", None))
        self.forecast_day1_prot_time.setText(QCoreApplication.translate("WeatherApp", u"9:30am-3:00pm", None))
        self.forecast_day1_prot_rec.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection Recommended", None))
        self.forecast_day2_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day2_date.setText(QCoreApplication.translate("WeatherApp", u"Today 26 September", None))
        self.forecast_day2_min_temp.setText(QCoreApplication.translate("WeatherApp", u"x\u00b0 Min", None))
        self.forecast_day2_max_temp.setText(QCoreApplication.translate("WeatherApp", u"y\u00b0 Max", None))
        self.label_170.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.forecast_day2_chance_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"25% chance of ", None))
        self.forecast_day2_amount_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"at least 5mm of rain", None))
        self.forecast_day2_chance_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"50% chance of", None))
        self.forecast_day2_amount_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"at least 2mm of rain", None))
        self.forecast_day2_chance_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"75% chance of", None))
        self.forecast_day2_amount_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"at least 1mm of rain", None))
        self.label_171.setText(QCoreApplication.translate("WeatherApp", u"General Info", None))
        self.forecast_day2_info.setText(QCoreApplication.translate("WeatherApp", u"Cloudy today with light shows in the morning. Will clear up in the afternoon", None))
        self.forecast_day2_fire_danger.setText(QCoreApplication.translate("WeatherApp", u"No", None))
        self.label_174.setText(QCoreApplication.translate("WeatherApp", u"Fire danger rating", None))
        self.label_175.setText(QCoreApplication.translate("WeatherApp", u"Sun and UV", None))
        self.forecast_day2_sunrise_time.setText(QCoreApplication.translate("WeatherApp", u"6:00am Sunrise", None))
        self.forecast_day2_sunset_time.setText(QCoreApplication.translate("WeatherApp", u"6:30pm Sunset", None))
        self.forecast_day2_uv.setText(QCoreApplication.translate("WeatherApp", u"5 (Moderate)", None))
        self.forecast_day2_uv_label.setText(QCoreApplication.translate("WeatherApp", u"Max UV index", None))
        self.forecast_day2_prot_time.setText(QCoreApplication.translate("WeatherApp", u"9:30am-3:00pm", None))
        self.forecast_day2_prot_rec.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection Recommended", None))
        self.forecast_day3_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day3_date.setText(QCoreApplication.translate("WeatherApp", u"Today 26 September", None))
        self.forecast_day3_min_temp.setText(QCoreApplication.translate("WeatherApp", u"x\u00b0 Min", None))
        self.forecast_day3_max_temp.setText(QCoreApplication.translate("WeatherApp", u"y\u00b0 Max", None))
        self.label_156.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.forecast_day3_chance_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"25% chance of ", None))
        self.forecast_day3_amount_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"at least 5mm of rain", None))
        self.forecast_day3_chance_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"50% chance of", None))
        self.forecast_day3_amount_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"at least 2mm of rain", None))
        self.forecast_day3_chance_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"75% chance of", None))
        self.forecast_day3_amount_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"at least 1mm of rain", None))
        self.label_157.setText(QCoreApplication.translate("WeatherApp", u"General Info", None))
        self.forecast_day3_info.setText(QCoreApplication.translate("WeatherApp", u"Cloudy today with light shows in the morning. Will clear up in the afternoon", None))
        self.forecast_day3_fire_danger.setText(QCoreApplication.translate("WeatherApp", u"No", None))
        self.label_160.setText(QCoreApplication.translate("WeatherApp", u"Fire danger rating", None))
        self.label_161.setText(QCoreApplication.translate("WeatherApp", u"Sun and UV", None))
        self.forecast_day3_sunrise_time.setText(QCoreApplication.translate("WeatherApp", u"6:00am Sunrise", None))
        self.forecast_day3_sunset_time.setText(QCoreApplication.translate("WeatherApp", u"6:30pm Sunset", None))
        self.forecast_day3_uv.setText(QCoreApplication.translate("WeatherApp", u"5 (Moderate)", None))
        self.forecast_day3_uv_label.setText(QCoreApplication.translate("WeatherApp", u"Max UV index", None))
        self.forecast_day3_prot_time.setText(QCoreApplication.translate("WeatherApp", u"9:30am-3:00pm", None))
        self.forecast_day3_prot_rec.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection Recommended", None))
        self.forecast_day4_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day4_date.setText(QCoreApplication.translate("WeatherApp", u"Today 26 September", None))
        self.forecast_day4_min_temp.setText(QCoreApplication.translate("WeatherApp", u"x\u00b0 Min", None))
        self.forecast_day4_max_temp.setText(QCoreApplication.translate("WeatherApp", u"y\u00b0 Max", None))
        self.label_142.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.forecast_day4_chance_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"25% chance of ", None))
        self.forecast_day4_amount_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"at least 5mm of rain", None))
        self.forecast_day4_chance_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"50% chance of", None))
        self.forecast_day4_amount_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"at least 2mm of rain", None))
        self.forecast_day4_chance_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"75% chance of", None))
        self.forecast_day4_amount_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"at least 1mm of rain", None))
        self.label_143.setText(QCoreApplication.translate("WeatherApp", u"General Info", None))
        self.forecast_day4_info.setText(QCoreApplication.translate("WeatherApp", u"Cloudy today with light shows in the morning. Will clear up in the afternoon", None))
        self.forecast_day4_fire_danger.setText(QCoreApplication.translate("WeatherApp", u"No", None))
        self.label_146.setText(QCoreApplication.translate("WeatherApp", u"Fire danger rating", None))
        self.label_147.setText(QCoreApplication.translate("WeatherApp", u"Sun and UV", None))
        self.forecast_day4_sunrise_time.setText(QCoreApplication.translate("WeatherApp", u"6:00am Sunrise", None))
        self.forecast_day4_sunset_time.setText(QCoreApplication.translate("WeatherApp", u"6:30pm Sunset", None))
        self.forecast_day4_uv.setText(QCoreApplication.translate("WeatherApp", u"5 (Moderate)", None))
        self.forecast_day4_uv_label.setText(QCoreApplication.translate("WeatherApp", u"Max UV index", None))
        self.forecast_day4_prot_time.setText(QCoreApplication.translate("WeatherApp", u"9:30am-3:00pm", None))
        self.forecast_day4_prot_rec.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection Recommended", None))
        self.forecast_day5_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day5_date.setText(QCoreApplication.translate("WeatherApp", u"Today 26 September", None))
        self.forecast_day5_min_temp.setText(QCoreApplication.translate("WeatherApp", u"x\u00b0 Min", None))
        self.forecast_day5_max_temp.setText(QCoreApplication.translate("WeatherApp", u"y\u00b0 Max", None))
        self.label_128.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.forecast_day5_chance_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"25% chance of ", None))
        self.forecast_day5_amount_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"at least 5mm of rain", None))
        self.forecast_day5_chance_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"50% chance of", None))
        self.forecast_day5_amount_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"at least 2mm of rain", None))
        self.forecast_day5_chance_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"75% chance of", None))
        self.forecast_day5_amount_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"at least 1mm of rain", None))
        self.label_129.setText(QCoreApplication.translate("WeatherApp", u"General Info", None))
        self.forecast_day5_info.setText(QCoreApplication.translate("WeatherApp", u"Cloudy today with light shows in the morning. Will clear up in the afternoon", None))
        self.forecast_day5_fire_danger.setText(QCoreApplication.translate("WeatherApp", u"No", None))
        self.label_132.setText(QCoreApplication.translate("WeatherApp", u"Fire danger rating", None))
        self.label_133.setText(QCoreApplication.translate("WeatherApp", u"Sun and UV", None))
        self.forecast_day5_sunrise_time.setText(QCoreApplication.translate("WeatherApp", u"6:00am Sunrise", None))
        self.forecast_day5_sunset_time.setText(QCoreApplication.translate("WeatherApp", u"6:30pm Sunset", None))
        self.forecast_day5_uv.setText(QCoreApplication.translate("WeatherApp", u"5 (Moderate)", None))
        self.forecast_day5_uv_label.setText(QCoreApplication.translate("WeatherApp", u"Max UV index", None))
        self.forecast_day5_prot_time.setText(QCoreApplication.translate("WeatherApp", u"9:30am-3:00pm", None))
        self.forecast_day5_prot_rec.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection Recommended", None))
        self.forecast_day6_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day6_date.setText(QCoreApplication.translate("WeatherApp", u"Today 26 September", None))
        self.forecast_day6_min_temp.setText(QCoreApplication.translate("WeatherApp", u"x\u00b0 Min", None))
        self.forecast_day6_max_temp.setText(QCoreApplication.translate("WeatherApp", u"y\u00b0 Max", None))
        self.label_114.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.forecast_day6_chance_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"25% chance of ", None))
        self.forecast_day6_amount_of_rain_1.setText(QCoreApplication.translate("WeatherApp", u"at least 5mm of rain", None))
        self.forecast_day6_chance_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"50% chance of", None))
        self.forecast_day6_amount_of_rain_2.setText(QCoreApplication.translate("WeatherApp", u"at least 2mm of rain", None))
        self.forecast_day6_chance_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"75% chance of", None))
        self.forecast_day6_amount_of_rain_3.setText(QCoreApplication.translate("WeatherApp", u"at least 1mm of rain", None))
        self.label_115.setText(QCoreApplication.translate("WeatherApp", u"General Info", None))
        self.forecast_day6_info.setText(QCoreApplication.translate("WeatherApp", u"Cloudy today with light shows in the morning. Will clear up in the afternoon", None))
        self.forecast_day6_fire_danger.setText(QCoreApplication.translate("WeatherApp", u"No", None))
        self.label_118.setText(QCoreApplication.translate("WeatherApp", u"Fire danger rating", None))
        self.label_119.setText(QCoreApplication.translate("WeatherApp", u"Sun and UV", None))
        self.forecast_day6_sunrise_time.setText(QCoreApplication.translate("WeatherApp", u"6:00am Sunrise", None))
        self.forecast_day6_sunset_time.setText(QCoreApplication.translate("WeatherApp", u"6:30pm Sunset", None))
        self.forecast_day6_uv.setText(QCoreApplication.translate("WeatherApp", u"5 (Moderate)", None))
        self.forecast_day6_uv_label.setText(QCoreApplication.translate("WeatherApp", u"Max UV index", None))
        self.forecast_day6_prot_time.setText(QCoreApplication.translate("WeatherApp", u"9:30am-3:00pm", None))
        self.forecast_day6_prot_rec.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection Recommended", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.forecast_weather), QCoreApplication.translate("WeatherApp", u"Forecast", None))
        self.label_3.setText(QCoreApplication.translate("WeatherApp", u"Gavin's Weather", None))
        self.label_2.setText(QCoreApplication.translate("WeatherApp", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("WeatherApp", u"Wind Speed Unit", None))
        self.ws_unit_button_kmh.setText(QCoreApplication.translate("WeatherApp", u"&km/h", None))
        self.ws_unit_button_knots.setText(QCoreApplication.translate("WeatherApp", u"&knots", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("WeatherApp", u"Settings", None))
    # retranslateUi

