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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from compasswidget import CompassWidget

class Ui_WeatherApp(object):
    def setupUi(self, WeatherApp):
        if not WeatherApp.objectName():
            WeatherApp.setObjectName(u"WeatherApp")
        WeatherApp.resize(919, 781)
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
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.location_input = QLineEdit(self.frame_3)
        self.location_input.setObjectName(u"location_input")
        self.location_input.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.location_input)

        self.location_choices = QComboBox(self.frame_3)
        self.location_choices.setObjectName(u"location_choices")

        self.horizontalLayout.addWidget(self.location_choices)

        self.get_weather_button = QPushButton(self.frame_3)
        self.get_weather_button.setObjectName(u"get_weather_button")

        self.horizontalLayout.addWidget(self.get_weather_button)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
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
        self.current_temp.setFrameShape(QFrame.Shape.Box)
        self.current_temp.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.current_temp)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.place_overview = QLabel(self.current_temp)
        self.place_overview.setObjectName(u"place_overview")
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.place_overview.setFont(font1)
        self.place_overview.setTextFormat(Qt.TextFormat.PlainText)
        self.place_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.place_overview)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.current_temp_overview = QLabel(self.current_temp)
        self.current_temp_overview.setObjectName(u"current_temp_overview")
        self.current_temp_overview.setMaximumSize(QSize(200, 50))
        font2 = QFont()
        font2.setFamilies([u"Liberation Sans"])
        font2.setPointSize(30)
        self.current_temp_overview.setFont(font2)
        self.current_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.current_temp_overview)

        self.current_day_icon_overview = QLabel(self.current_temp)
        self.current_day_icon_overview.setObjectName(u"current_day_icon_overview")
        self.current_day_icon_overview.setMaximumSize(QSize(100, 100))
        font3 = QFont()
        font3.setFamilies([u"Liberation Sans"])
        font3.setPointSize(35)
        self.current_day_icon_overview.setFont(font3)

        self.horizontalLayout_11.addWidget(self.current_day_icon_overview)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.current_condtions_overview = QLabel(self.current_temp)
        self.current_condtions_overview.setObjectName(u"current_condtions_overview")
        font4 = QFont()
        font4.setFamilies([u"Liberation Sans"])
        font4.setPointSize(15)
        self.current_condtions_overview.setFont(font4)
        self.current_condtions_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.current_condtions_overview)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.min_temp_overview = QLabel(self.current_temp)
        self.min_temp_overview.setObjectName(u"min_temp_overview")
        self.min_temp_overview.setFont(font)
        self.min_temp_overview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.min_temp_overview)

        self.max_temp_overview = QLabel(self.current_temp)
        self.max_temp_overview.setObjectName(u"max_temp_overview")
        self.max_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.max_temp_overview)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.feels_like_temp_overview = QLabel(self.current_temp)
        self.feels_like_temp_overview.setObjectName(u"feels_like_temp_overview")
        self.feels_like_temp_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.feels_like_temp_overview)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)


        self.left_side.addWidget(self.current_temp)

        self.forecast_overview = QFrame(self.overview)
        self.forecast_overview.setObjectName(u"forecast_overview")
        self.forecast_overview.setFrameShape(QFrame.Shape.Box)
        self.forecast_overview.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.forecast_overview)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.day1_overview = QLabel(self.forecast_overview)
        self.day1_overview.setObjectName(u"day1_overview")

        self.verticalLayout_2.addWidget(self.day1_overview)

        self.day2_overview = QLabel(self.forecast_overview)
        self.day2_overview.setObjectName(u"day2_overview")

        self.verticalLayout_2.addWidget(self.day2_overview)

        self.day3_overview = QLabel(self.forecast_overview)
        self.day3_overview.setObjectName(u"day3_overview")

        self.verticalLayout_2.addWidget(self.day3_overview)

        self.day4_overview = QLabel(self.forecast_overview)
        self.day4_overview.setObjectName(u"day4_overview")

        self.verticalLayout_2.addWidget(self.day4_overview)

        self.day5_overview = QLabel(self.forecast_overview)
        self.day5_overview.setObjectName(u"day5_overview")

        self.verticalLayout_2.addWidget(self.day5_overview)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.icon_overview1 = QLabel(self.forecast_overview)
        self.icon_overview1.setObjectName(u"icon_overview1")
        self.icon_overview1.setMaximumSize(QSize(75, 75))
        font5 = QFont()
        font5.setFamilies([u"Liberation Sans"])
        font5.setPointSize(10)
        self.icon_overview1.setFont(font5)
        self.icon_overview1.setPixmap(QPixmap(u"../8a3a0566/sunny.png"))
        self.icon_overview1.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.icon_overview1)

        self.icon_overview2 = QLabel(self.forecast_overview)
        self.icon_overview2.setObjectName(u"icon_overview2")
        self.icon_overview2.setMaximumSize(QSize(75, 75))
        self.icon_overview2.setFont(font5)

        self.verticalLayout_3.addWidget(self.icon_overview2)

        self.icon_overview3 = QLabel(self.forecast_overview)
        self.icon_overview3.setObjectName(u"icon_overview3")
        self.icon_overview3.setMaximumSize(QSize(75, 75))
        self.icon_overview3.setFont(font5)

        self.verticalLayout_3.addWidget(self.icon_overview3)

        self.icon_overview4 = QLabel(self.forecast_overview)
        self.icon_overview4.setObjectName(u"icon_overview4")
        self.icon_overview4.setMaximumSize(QSize(75, 75))
        self.icon_overview4.setFont(font5)

        self.verticalLayout_3.addWidget(self.icon_overview4)

        self.icon_overview5 = QLabel(self.forecast_overview)
        self.icon_overview5.setObjectName(u"icon_overview5")
        self.icon_overview5.setMaximumSize(QSize(75, 75))
        self.icon_overview5.setFont(font5)

        self.verticalLayout_3.addWidget(self.icon_overview5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.day1_temp_overview = QLabel(self.forecast_overview)
        self.day1_temp_overview.setObjectName(u"day1_temp_overview")

        self.verticalLayout_4.addWidget(self.day1_temp_overview)

        self.day2_temp_overview = QLabel(self.forecast_overview)
        self.day2_temp_overview.setObjectName(u"day2_temp_overview")

        self.verticalLayout_4.addWidget(self.day2_temp_overview)

        self.day3_temp_overview = QLabel(self.forecast_overview)
        self.day3_temp_overview.setObjectName(u"day3_temp_overview")

        self.verticalLayout_4.addWidget(self.day3_temp_overview)

        self.day4_temp_overview = QLabel(self.forecast_overview)
        self.day4_temp_overview.setObjectName(u"day4_temp_overview")

        self.verticalLayout_4.addWidget(self.day4_temp_overview)

        self.day5_temp_overview = QLabel(self.forecast_overview)
        self.day5_temp_overview.setObjectName(u"day5_temp_overview")

        self.verticalLayout_4.addWidget(self.day5_temp_overview)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)


        self.left_side.addWidget(self.forecast_overview)


        self.horizontalLayout_12.addLayout(self.left_side)

        self.right_side = QVBoxLayout()
        self.right_side.setObjectName(u"right_side")
        self.uv_index = QFrame(self.overview)
        self.uv_index.setObjectName(u"uv_index")
        self.uv_index.setFrameShape(QFrame.Shape.Box)
        self.uv_index.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.uv_index)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.uv_index)
        self.label_17.setObjectName(u"label_17")
        font6 = QFont()
        font6.setFamilies([u"Liberation Sans"])
        font6.setPointSize(20)
        self.label_17.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_17)

        self.uv_index_bar = QProgressBar(self.uv_index)
        self.uv_index_bar.setObjectName(u"uv_index_bar")
        self.uv_index_bar.setMinimum(0)
        self.uv_index_bar.setMaximum(11)
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

        self.horizontalLayout_5.addWidget(self.max_uv_overview)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sun_protection_recommended_overview = QLabel(self.uv_index)
        self.sun_protection_recommended_overview.setObjectName(u"sun_protection_recommended_overview")

        self.verticalLayout_7.addWidget(self.sun_protection_recommended_overview)

        self.protection_time_overview = QLabel(self.uv_index)
        self.protection_time_overview.setObjectName(u"protection_time_overview")

        self.verticalLayout_7.addWidget(self.protection_time_overview)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.right_side.addWidget(self.uv_index)

        self.sunrise_and_set = QFrame(self.overview)
        self.sunrise_and_set.setObjectName(u"sunrise_and_set")
        self.sunrise_and_set.setFrameShape(QFrame.Shape.Box)
        self.sunrise_and_set.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.sunrise_and_set)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sunrise_overview = QLabel(self.sunrise_and_set)
        self.sunrise_overview.setObjectName(u"sunrise_overview")

        self.horizontalLayout_4.addWidget(self.sunrise_overview)

        self.sunset_overview = QLabel(self.sunrise_and_set)
        self.sunset_overview.setObjectName(u"sunset_overview")

        self.horizontalLayout_4.addWidget(self.sunset_overview)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.right_side.addWidget(self.sunrise_and_set)

        self.amount_of_rain = QFrame(self.overview)
        self.amount_of_rain.setObjectName(u"amount_of_rain")
        self.amount_of_rain.setFrameShape(QFrame.Shape.Box)
        self.amount_of_rain.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.amount_of_rain)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.graphicsView = QGraphicsView(self.amount_of_rain)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_11.addWidget(self.graphicsView)


        self.right_side.addWidget(self.amount_of_rain)

        self.wind_speed = QFrame(self.overview)
        self.wind_speed.setObjectName(u"wind_speed")
        self.wind_speed.setFrameShape(QFrame.Shape.Box)
        self.wind_speed.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.wind_speed)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.wind_speed)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setFamilies([u"Liberation Sans"])
        font7.setBold(True)
        self.label.setFont(font7)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.compass_widget = CompassWidget(self.wind_speed)
        self.compass_widget.setObjectName(u"compass_widget")
        self.compass_widget.setMinimumSize(QSize(100, 100))

        self.verticalLayout_9.addWidget(self.compass_widget)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_25 = QLabel(self.wind_speed)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_25)

        self.wind_speed_overview = QLabel(self.wind_speed)
        self.wind_speed_overview.setObjectName(u"wind_speed_overview")
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
        self.Highlights.setFrameShape(QFrame.Shape.NoFrame)
        self.Highlights.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.Highlights)
        self.gridLayout.setObjectName(u"gridLayout")
        self.highest_gust_speed = QFrame(self.Highlights)
        self.highest_gust_speed.setObjectName(u"highest_gust_speed")
        self.highest_gust_speed.setFrameShape(QFrame.Shape.Box)
        self.highest_gust_speed.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.highest_gust_speed)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.highlights_gust_speed = QLabel(self.highest_gust_speed)
        self.highlights_gust_speed.setObjectName(u"highlights_gust_speed")
        self.highlights_gust_speed.setFont(font4)

        self.horizontalLayout_8.addWidget(self.highlights_gust_speed)

        self.highlights_gust_speed_time = QLabel(self.highest_gust_speed)
        self.highlights_gust_speed_time.setObjectName(u"highlights_gust_speed_time")

        self.horizontalLayout_8.addWidget(self.highlights_gust_speed_time)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 20)

        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.label_35 = QLabel(self.highest_gust_speed)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_15.addWidget(self.label_35)


        self.verticalLayout_19.addLayout(self.verticalLayout_15)


        self.gridLayout.addWidget(self.highest_gust_speed, 2, 0, 1, 1)

        self.highest_temperature = QFrame(self.Highlights)
        self.highest_temperature.setObjectName(u"highest_temperature")
        self.highest_temperature.setFrameShape(QFrame.Shape.Box)
        self.highest_temperature.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_18 = QVBoxLayout(self.highest_temperature)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.highlights_max_temp = QLabel(self.highest_temperature)
        self.highlights_max_temp.setObjectName(u"highlights_max_temp")
        self.highlights_max_temp.setFont(font4)

        self.horizontalLayout_2.addWidget(self.highlights_max_temp)

        self.highlights_max_temp_time = QLabel(self.highest_temperature)
        self.highlights_max_temp_time.setObjectName(u"highlights_max_temp_time")

        self.horizontalLayout_2.addWidget(self.highlights_max_temp_time)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 20)

        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.label_29 = QLabel(self.highest_temperature)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_13.addWidget(self.label_29)


        self.verticalLayout_18.addLayout(self.verticalLayout_13)


        self.gridLayout.addWidget(self.highest_temperature, 1, 0, 1, 1)

        self.amount_of_rain_9am = QFrame(self.Highlights)
        self.amount_of_rain_9am.setObjectName(u"amount_of_rain_9am")
        self.amount_of_rain_9am.setFrameShape(QFrame.Shape.Box)
        self.amount_of_rain_9am.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.amount_of_rain_9am)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.highlights_rain_since_9am = QLabel(self.amount_of_rain_9am)
        self.highlights_rain_since_9am.setObjectName(u"highlights_rain_since_9am")
        self.highlights_rain_since_9am.setFont(font4)

        self.horizontalLayout_13.addWidget(self.highlights_rain_since_9am)

        self.label_37 = QLabel(self.amount_of_rain_9am)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_13.addWidget(self.label_37)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 20)

        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.label_38 = QLabel(self.amount_of_rain_9am)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_16.addWidget(self.label_38)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.gridLayout.addWidget(self.amount_of_rain_9am, 2, 1, 1, 1)

        self.lowest_temperature = QFrame(self.Highlights)
        self.lowest_temperature.setObjectName(u"lowest_temperature")
        self.lowest_temperature.setFrameShape(QFrame.Shape.Box)
        self.lowest_temperature.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.lowest_temperature)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.highlights_min_temp = QLabel(self.lowest_temperature)
        self.highlights_min_temp.setObjectName(u"highlights_min_temp")
        self.highlights_min_temp.setFont(font4)

        self.horizontalLayout_3.addWidget(self.highlights_min_temp)

        self.highlights_min_temp_time = QLabel(self.lowest_temperature)
        self.highlights_min_temp_time.setObjectName(u"highlights_min_temp_time")

        self.horizontalLayout_3.addWidget(self.highlights_min_temp_time)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)

        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.label_32 = QLabel(self.lowest_temperature)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_14.addWidget(self.label_32)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)


        self.gridLayout.addWidget(self.lowest_temperature, 1, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.Highlights)

        self.Details = QFrame(self.past_weather)
        self.Details.setObjectName(u"Details")
        self.Details.setFrameShape(QFrame.Shape.StyledPanel)
        self.Details.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Details)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.observation_info_table = QTableWidget(self.Details)
        self.observation_info_table.setObjectName(u"observation_info_table")

        self.horizontalLayout_16.addWidget(self.observation_info_table)


        self.verticalLayout_12.addWidget(self.Details)

        self.tabWidget.addTab(self.past_weather, "")
        self.forecast_weather = QWidget()
        self.forecast_weather.setObjectName(u"forecast_weather")
        self.verticalLayout_20 = QVBoxLayout(self.forecast_weather)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.forecast_info_table = QTableWidget(self.forecast_weather)
        self.forecast_info_table.setObjectName(u"forecast_info_table")

        self.verticalLayout_20.addWidget(self.forecast_info_table)

        self.tabWidget.addTab(self.forecast_weather, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 271, 61))
        font8 = QFont()
        font8.setFamilies([u"Liberation Sans"])
        font8.setPointSize(25)
        font8.setBold(True)
        self.label_3.setFont(font8)
        self.tabWidget.addTab(self.settings, "")

        self.verticalLayout.addWidget(self.tabWidget)

        WeatherApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(WeatherApp)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(WeatherApp)
    # setupUi

    def retranslateUi(self, WeatherApp):
        WeatherApp.setWindowTitle(QCoreApplication.translate("WeatherApp", u"MainWindow", None))
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
        self.icon_overview2.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_overview3.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_overview4.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_overview5.setText(QCoreApplication.translate("WeatherApp", u"O", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.forecast_weather), QCoreApplication.translate("WeatherApp", u"Forecast", None))
        self.label_3.setText(QCoreApplication.translate("WeatherApp", u"Gavin's Weather", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("WeatherApp", u"Settings", None))
    # retranslateUi

