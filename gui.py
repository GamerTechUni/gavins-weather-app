"""
TODO: Add Module Docstring
"""
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QWidget,
                               QMainWindow,
                               QLabel,
                               QLineEdit,
                               QPushButton,
                               QGridLayout,
                               QVBoxLayout,
                               QComboBox,
                               QTabWidget,
                               QMessageBox,
                               QAbstractItemView,
                               QTableWidgetItem)
from PySide6.QtCore import Qt, Slot, QThreadPool
from main_ui import Ui_WeatherApp
from backend import (fetch_location_options,
                     fetch_observation,
                     fetch_location_information,
                     fetch_daily_forecast,
                     fetch_hourly_forecast,
                     fetch_hourly_observations,
                     fetch_station_code,
                     read_settings,
                     write_to_settings
                     )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create attribute to that stores location to share info across class
        self.location_and_geohash = {}

        # Read settings file
        self.ws_unit = read_settings('ws_unit')
        self.previous_location_geohash = read_settings(
            'previous_location_geohash')
        self.previous_location_name = read_settings('previous_location_name')

        # Create thread to avoid freezing program while searching
        self.thread_manager = QThreadPool()

        self.ui = Ui_WeatherApp()
        self.ui.setupUi(self)
        self.setWindowTitle("Gavin's Weather App")

        # Sends call everytime the text changes in the search bar
        self.ui.location_input.textChanged.connect(
            self.display_locations_thread)
        self.ui.get_weather_button.clicked.connect(
            self.get_current_location_from_selection)
        self.ui.overview.hide()

        # Disable tabs until weather data is loaded
        self.ui.tabWidget.setTabEnabled(0, False)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)

        # Define Weather Icons
        self.sunny_icon = QPixmap('assets/bom/sunny.png')
        self.cloudy_icon = QPixmap('assets/bom/cloudy.png')
        self.hazy_icon = QPixmap('assets/bom/haze.png')
        self.light_rain_icon = QPixmap('assets/bom/light-rain.png')
        self.partly_cloudy_icon = QPixmap('assets/bom/partly-cloudy.png')
        self.shower_icon = QPixmap('assets/bom/showers.png')
        self.rain_icon = QPixmap('assets/bom/rain.png')
        self.storm_icon = QPixmap('assets/bom/storm.png')
        self.windy_icon = QPixmap('assets/bom/wind.png')
        self.fog_icon = QPixmap('assets/bom/fog.png')
        self.dusty_icon = QPixmap('assets/bom/dust.png')
        self.frost_icon = QPixmap('assets/bom/frost.png')
        self.snow_icon = QPixmap('assets/bom/snow.png')
        self.light_shower_icon = QPixmap('assets/bom/light-showers.png')
        self.heavy_shower_icon = QPixmap('assets/bom/heavy-showers.png')
        self.cyclone_icon = QPixmap('assets/bom/tropicalcyclone.png')
        self.clear_icon = QPixmap('assets/bom/clear.png')
        self.partly_cloudy_night_icon = QPixmap(
            'assets/bom/partly-cloudy-night.png')
        self.hazy_night_icon = QPixmap('assets/bom/haze-night.png')
        self.fog_night_icon = QPixmap('assets/bom/fog-night.png')
        self.shower_night_icon = QPixmap('assets/bom/showers-night.png')
        self.light_shower_night_icon = QPixmap(
            'assets/bom/light-showers-night.png')

        # Resize icons to the limit of the label size
        self.resize(self.sunny_icon.width(), self.sunny_icon.height())
        self.resize(self.cloudy_icon.width(), self.cloudy_icon.height())
        self.resize(self.hazy_icon.width(), self.hazy_icon.height())
        self.resize(self.light_rain_icon.width(),
                    self.light_rain_icon.height())
        self.resize(self.partly_cloudy_icon.width(),
                    self.partly_cloudy_icon.height())
        self.resize(self.shower_icon.width(), self.shower_icon.height())
        self.resize(self.rain_icon.width(), self.rain_icon.height())
        self.resize(self.storm_icon.width(), self.storm_icon.height())
        self.resize(self.windy_icon.width(), self.windy_icon.height())
        self.resize(self.fog_icon.width(), self.fog_icon.height())
        self.resize(self.dusty_icon.width(), self.dusty_icon.height())
        self.resize(self.frost_icon.width(), self.frost_icon.height())
        self.resize(self.snow_icon.width(), self.snow_icon.height())
        self.resize(self.light_shower_icon.width(),
                    self.light_shower_icon.height())
        self.resize(self.heavy_shower_icon.width(),
                    self.heavy_shower_icon.height())
        self.resize(self.cyclone_icon.width(), self.cyclone_icon.height())
        self.resize(self.clear_icon.width(), self.clear_icon.height())
        self.resize(self.partly_cloudy_night_icon.width(),
                    self.partly_cloudy_night_icon.height())
        self.resize(self.hazy_night_icon.width(),
                    self.hazy_night_icon.height())
        self.resize(self.fog_night_icon.width(), self.fog_night_icon.height())
        self.resize(self.shower_night_icon.width(),
                    self.shower_night_icon.height())
        self.resize(self.light_shower_night_icon.width(),
                    self.light_shower_night_icon.height())

        if self.previous_location_geohash != '':
            # If a previous location has been stored in settings, then restore previous location
            self.get_previous_location_info()

    def display_locations(self):
        """ A method that gathers location options to be stored
        Calls fetch_location_options from the backend module and stores it in
        self.location_and_geohash for use and then presents the location
        choices in the dropdown menu.
        """
        location = self.ui.location_input.text()
        self.location_and_geohash = fetch_location_options(location)
        location_options = self.location_and_geohash.keys()
        self.ui.location_choices.clear()
        self.ui.location_choices.addItems(location_options)

    @Slot()
    def display_locations_thread(self):
        """ Creates thread for display_locations method
        """
        self.thread_manager.start(self.display_locations)

    def get_previous_location_info(self):
        """ Retrieves location info from settings.ini file
        The info from the settings.ini file is used to gather
        the weather data for the location to restore it.
        Calls self.get_weather_info to actually retrieve the data.
        """
        geohash = self.previous_location_geohash
        location_name = self.previous_location_name
        self.get_weather_info(location_name, geohash)

    @Slot()
    def get_current_location_from_selection(self):
        """ Retrieves weather data from selection
        Gathers selection from dropdown menu and then calls
        self.get_weather_info to gather the weather data.
        """
        try:
            geohash = self.location_and_geohash[self.ui.location_choices.currentText(
            )]
            location_name = self.ui.location_choices.currentText()[:-4]
            write_to_settings('previous_location_geohash', geohash)
            write_to_settings('previous_location_name', location_name)
            self.get_weather_info(location_name, geohash)
        except KeyError:
            QMessageBox.information(
                self, "No Location Selected",
                "You have not selected a location\nPlease select a location")

    def get_weather_info(self, location_name, geohash):
        """ Gathers weather info and sets things up
        The method will gather the data using functions from
        the backend module and then initialises everything else
        by calling the self.set_placeholder_values method to replace
        placeholder data with actual weather data. Also enables the
        other tabs, creates tables for hourly forecasts and observations,
        as well as plotting the graph.
        Parameters
        ----------
        location_name : str
            The name of the location that has been selected or restored
        geohash : str
            Seven digit code used to identify location and gather weather data

        """
        location_info = fetch_location_information(geohash)

        timezone = location_info.get('timezone')

        ob_info = fetch_observation(geohash, timezone)
        state = location_info.get('state')
        wmo_code = fetch_station_code(
            location_info.get('station_id'), state)
        daily_forecast_info = fetch_daily_forecast(geohash, timezone)
        hourly_forecast_info = fetch_hourly_forecast(geohash, timezone)
        hourly_observation_info = fetch_hourly_observations(
            wmo_code, state, timezone)

        self.set_placeholder_values(
            ob_info, daily_forecast_info, location_name)

        self.create_forecast_table(hourly_forecast_info)
        self.create_observation_table(hourly_observation_info)

        self.ui.rain_graph_overview.plot_graph(hourly_forecast_info)

        self.ui.tabWidget.setTabEnabled(0, True)
        self.ui.tabWidget.setTabEnabled(1, True)
        self.ui.tabWidget.setTabEnabled(2, True)
        self.ui.tabWidget.setCurrentWidget(self.ui.overview)

    def set_placeholder_values(self, ob_info, daily_forecast_info, location_name):
        """ Replaces placeholder data with actual weather data
        Parameters
        ----------
        ob_info : dict
            Current observation data used to replace placeholder data in the UI
        daily_forecast_info : list
            Forecast info used to replace placeholder data in the UI
        location_name : str
            Used to replace location placeholder name with actual location

        """
        # Overview
        is_night = daily_forecast_info[0].get('is_night')

        # Overview Current Info
        self.ui.current_temp_overview.setText(
            f"{ob_info.get('current_temp')}\u00b0")
        self.ui.feels_like_temp_overview.setText(
            f"Feels like: {ob_info.get('feels_like_temp')}\u00b0")
        self.ui.current_condtions_overview.setText(
            daily_forecast_info[0].get('short_text'))

        if is_night:
            self.ui.min_temp_overview.setText(
                f"Overnight Min: {str(daily_forecast_info[0].get('temp_now'))}\u00b0")
            self.ui.max_temp_overview.setText(
                f"Tomorrow's Max: {str(daily_forecast_info[1].get('max_temp'))}\u00b0")
            self.set_overview_forecast_icons(
                daily_forecast_info[0].get('icon_descriptor'),
                self.ui.current_day_icon_overview, is_night)
        else:

            self.ui.min_temp_overview.setText(f"Min: {str(
                daily_forecast_info[0].get('min_temp'))}\u00b0")
            self.ui.max_temp_overview.setText(f"Max: {str(
                daily_forecast_info[0].get('max_temp'))}\u00b0")
            self.set_overview_forecast_icons(
                daily_forecast_info[0].get('icon_descriptor'),
                self.ui.current_day_icon_overview, is_night)

        self.ui.place_overview.setText(location_name)

        # Overview UV index
        max_uv = daily_forecast_info[0].get('max_uv_index')
        max_uv_category = daily_forecast_info[0].get('max_uv_category')
        print(max_uv_category)
        self.ui.max_uv_overview.setText(f"Max UV: {str(max_uv)}")
        if max_uv == '':
            self.ui.protection_time_overview.setText("")
            self.ui.sun_protection_recommended_overview.setText(
                "Sun Protection Not Required")
        else:
            if max_uv <= 11:
                self.ui.uv_index_bar.setValue(max_uv)
            else:
                self.ui.uv_index_bar.setValue(11)
            if max_uv > 2:
                self.ui.protection_time_overview.setText(f"From {daily_forecast_info[0].get(
                    'sun_prot_start_time')} to {daily_forecast_info[0].get('sun_prot_end_time')}")

            # Set UV Index bar colour based on category of risk
        if max_uv_category == 'low':
            self.ui.uv_index_bar.setStyleSheet(
                "QProgressBar::chunk {background-color: green}")
        elif max_uv_category == 'moderate':
            self.ui.uv_index_bar.setStyleSheet(
                "QProgressBar::chunk {background-color: yellow}")
        elif max_uv_category == 'high':
            self.ui.uv_index_bar.setStyleSheet(
                "QProgressBar::chunk {background-color: orange}")
        elif max_uv_category == 'veryhigh':
            self.ui.uv_index_bar.setStyleSheet(
                "QProgressBar::chunk {background-color: red}")
        elif max_uv_category == 'extreme':
            self.ui.uv_index_bar.setStyleSheet(
                "QProgressBar::chunk {background-color: violet}")

        # Sunrise and Sunset Time
        self.ui.sunrise_overview.setText(
            f"Sunrise: {daily_forecast_info[0].get('sunrise_time')}")
        self.ui.sunset_overview.setText(
            f"Sunset: {daily_forecast_info[0].get('sunset_time')}")

        # Set the relevant rain info in the rain widget
        if daily_forecast_info[0].get('max_rain_amount') == '':
            self.ui.forecast_amount_of_rain_overview.setText(f'{daily_forecast_info[0].get(
                'min_rain_amount')}mm')
        else:
            self.ui.forecast_amount_of_rain_overview.setText(f'{daily_forecast_info[0].get(
                'min_rain_amount')}-{daily_forecast_info[0].get('max_rain_amount')}mm')
        self.ui.chance_of_rain_overview.setText(
            f'{daily_forecast_info[0].get('chance_of_rain')}%')

        # Show chance of rain in the upcoming forecast section
        self.ui.icon_chance_of_rain1.setText(f"{daily_forecast_info[1].get(
            'chance_of_rain')}%")
        self.ui.icon_chance_of_rain2.setText(f"{daily_forecast_info[2].get(
            'chance_of_rain')}%")
        self.ui.icon_chance_of_rain3.setText(f"{daily_forecast_info[3].get(
            'chance_of_rain')}%")
        self.ui.icon_chance_of_rain4.setText(f"{daily_forecast_info[4].get(
            'chance_of_rain')}%")
        self.ui.icon_chance_of_rain5.setText(f"{daily_forecast_info[5].get(
            'chance_of_rain')}%")

        # Set compass to show direction of wind
        wind_direction = ob_info.get('wind_direction')
        wind_direction_full = ''
        if wind_direction == 'N':
            self.ui.compass_widget.setAngle(180)
            wind_direction_full = 'North'
        elif wind_direction == 'NNE':
            self.ui.compass_widget.setAngle(202.5)
            wind_direction_full = 'North Northeast'
        elif wind_direction == 'NE':
            self.ui.compass_widget.setAngle(225)
            wind_direction_full = 'Northeast'
        elif wind_direction == 'ENE':
            self.ui.compass_widget.setAngle(247.5)
            wind_direction_full = 'East Northeast'
        elif wind_direction == 'E':
            self.ui.compass_widget.setAngle(270)
            wind_direction_full = 'East'
        elif wind_direction == 'ESE':
            self.ui.compass_widget.setAngle(292.5)
            wind_direction_full = 'East Southeast'
        elif wind_direction == 'SE':
            self.ui.compass_widget.setAngle(315)
            wind_direction_full = 'Southeast'
        elif wind_direction == 'SSE':
            self.ui.compass_widget.setAngle(337.5)
            wind_direction_full = 'South Southeast'
        elif wind_direction == 'S':
            self.ui.compass_widget.setAngle(0)
            wind_direction_full = 'South'
        elif wind_direction == 'SSW':
            self.ui.compass_widget.setAngle(22.5)
            wind_direction_full = 'South Southwest'
        elif wind_direction == 'SW':
            self.ui.compass_widget.setAngle(45)
            wind_direction_full = 'Southwest'
        elif wind_direction == 'WSW':
            self.ui.compass_widget.setAngle(67.5)
            wind_direction_full = 'West Southwest'
        elif wind_direction == 'W':
            self.ui.compass_widget.setAngle(90)
            wind_direction_full = 'West'
        elif wind_direction == 'WNW':
            self.ui.compass_widget.setAngle(112.5)
            wind_direction_full = 'West Northwest'
        elif wind_direction == 'NW':
            self.ui.compass_widget.setAngle(135)
            wind_direction_full = 'Northwest'
        elif wind_direction == 'NNW':
            self.ui.compass_widget.setAngle(157.5)
            wind_direction_full = 'North Northwest'
        else:
            self.ui.compass_widget.setAngle(0)

        self.ui.wind_speed_overview.setText(
            f"{ob_info.get('wind')}{self.ws_unit} {wind_direction_full}")

        # Set Future Forecast Overview Data
        self.ui.day1_overview.setText("Tomorrow")
        self.ui.day1_temp_overview.setText(f"{daily_forecast_info[1].get(
            'min_temp')}\u00b0—{daily_forecast_info[1].get('max_temp')}\u00b0")
        self.set_overview_forecast_icons(
            daily_forecast_info[1].get('icon_descriptor'), self.ui.icon_overview1, is_night=False)

        self.ui.day2_overview.setText(daily_forecast_info[2].get('date'))
        self.ui.day2_temp_overview.setText(f"{daily_forecast_info[2].get(
            'min_temp')}\u00b0—{daily_forecast_info[2].get('max_temp')}\u00b0")
        self.set_overview_forecast_icons(
            daily_forecast_info[2].get('icon_descriptor'), self.ui.icon_overview2, is_night=False)

        self.ui.day3_overview.setText(daily_forecast_info[3].get('date'))
        self.ui.day3_temp_overview.setText(f"{daily_forecast_info[3].get(
            'min_temp')}\u00b0—{daily_forecast_info[3].get('max_temp')}\u00b0")
        self.set_overview_forecast_icons(
            daily_forecast_info[3].get('icon_descriptor'), self.ui.icon_overview3, is_night=False)

        self.ui.day4_overview.setText(daily_forecast_info[4].get('date'))
        self.ui.day4_temp_overview.setText(f"{daily_forecast_info[4].get(
            'min_temp')}\u00b0—{daily_forecast_info[4].get('max_temp')}\u00b0")
        self.set_overview_forecast_icons(
            daily_forecast_info[4].get('icon_descriptor'), self.ui.icon_overview4, is_night=False)

        self.ui.day5_overview.setText(daily_forecast_info[5].get('date'))
        self.ui.day5_temp_overview.setText(f"{daily_forecast_info[5].get(
            'min_temp')}\u00b0—{daily_forecast_info[5].get('max_temp')}\u00b0")
        self.set_overview_forecast_icons(
            daily_forecast_info[5].get('icon_descriptor'), self.ui.icon_overview5, is_night=False)

        # Set highlight information in 'Past' tab
        self.ui.highlights_max_temp.setText(f"{ob_info.get('max_temp')}\u00b0")
        self.ui.highlights_max_temp_time.setText(
            f"at {ob_info.get('max_temp_time')}")
        self.ui.highlights_min_temp.setText(f"{ob_info.get('min_temp')}\u00b0")
        self.ui.highlights_min_temp_time.setText(
            f"at {ob_info.get('min_temp_time')}")
        self.ui.highlights_gust_speed.setText(
            f"{ob_info.get('max_gust')}{self.ws_unit}")
        self.ui.highlights_gust_speed_time.setText(
            f"at {ob_info.get('max_gust_time')}")
        self.ui.highlights_rain_since_9am.setText(
            f"{ob_info.get('rain_since_9am')}mm")

    def set_overview_forecast_icons(self, weather_condition, label, is_night):
        """ Sets the weather icons of the given label, based on the condition
        Parameters
        ----------
        weather_condition : str
            Tells function what the weather condition is from the data
        label : QLabel
            Tells function what label to set the pixmap of
        is_night : bool
            Tells function whether to set the day icons or night icons
        """

        if is_night:
            if weather_condition == 'clear':
                label.setPixmap(self.clear_icon)
            elif weather_condition == 'partly_cloudy' or weather_condition == 'mostly_sunny':
                label.setPixmap(self.partly_cloudy_night_icon)
            elif weather_condition == 'hazy':
                label.setPixmap(self.hazy_night_icon)
            elif weather_condition == 'fog':
                label.setPixmap(self.fog_night_icon)
            elif weather_condition == 'shower':
                label.setPixmap(self.shower_night_icon)
            elif weather_condition == 'light_shower':
                label.setPixmap(self.light_shower_night_icon)
        else:
            if weather_condition == 'sunny':
                label.setPixmap(self.sunny_icon)
            elif weather_condition == 'mostly_sunny' or weather_condition == 'partly_cloudy':
                label.setPixmap(self.partly_cloudy_icon)
            elif weather_condition == 'shower':
                label.setPixmap(self.shower_icon)
            elif weather_condition == 'hazy':
                label.setPixmap(self.hazy_icon)
            elif weather_condition == 'fog':
                label.setPixmap(self.fog_icon)
            elif weather_condition == 'shower':
                label.setPixmap(self.shower_icon)
            elif weather_condition == 'light_shower':
                label.setPixmap(self.light_shower_icon)

        # Icons that are the same during day and night
        if weather_condition == 'cloudy':
            label.setPixmap(self.cloudy_icon)
        elif weather_condition == 'storm':
            label.setPixmap(self.storm_icon)
        elif weather_condition == 'light_rain':
            label.setPixmap(self.light_rain_icon)
        elif weather_condition == 'windy':
            label.setPixmap(self.windy_icon)
        elif weather_condition == 'rain':
            label.setPixmap(self.rain_icon)
        elif weather_condition == 'dusty':
            label.setPixmap(self.dusty_icon)
        elif weather_condition == 'frost':
            label.setPixmap(self.frost_icon)
        elif weather_condition == 'snow':
            label.setPixmap(self.snow_icon)
        elif weather_condition == 'heavy_shower':
            label.setPixmap(self.heavy_shower_icon)
        elif weather_condition == 'cyclone':
            label.setPixmap(self.cyclone_icon)

        label.setScaledContents(True)

    def create_forecast_table(self, hourly_data):
        """ Creates a tabular form of the hourly data on the forecast tab
        Parameters
        ----------
        hourly_data : list
            The weather data that is used to create a tabular form of the data
        """
        time_list = []
        category_list = ['Air temperature (\u00b0C)', 'Feels like (\u00b0C)',
                         'Dew point temperature (\u00b0C)', 'UV Index',
                         f'Wind speed ({self.ws_unit})', 'Wind direction']
        for hour in hourly_data:
            hour_time = hour.get('time')
            time_list.append(hour_time)

        self.ui.forecast_info_table.setRowCount(len(category_list))
        self.ui.forecast_info_table.setColumnCount(len(time_list))
        self.ui.forecast_info_table.setVerticalHeaderLabels(category_list)
        self.ui.forecast_info_table.setHorizontalHeaderLabels(time_list)
        self.ui.forecast_info_table.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        for i in range(len(time_list)):
            self.ui.forecast_info_table.setItem(
                0, i, QTableWidgetItem(str(f'{hourly_data[i].get('temp')}\u00b0')))
            self.ui.forecast_info_table.setItem(
                1, i, QTableWidgetItem(str(f'{hourly_data[i].get('feels_like_temp')}\u00b0')))
            self.ui.forecast_info_table.setItem(
                2, i, QTableWidgetItem(str(f'{hourly_data[i].get('dew_point')}\u00b0')))
            self.ui.forecast_info_table.setItem(
                3, i, QTableWidgetItem(str(hourly_data[i].get('uv_index'))))
            self.ui.forecast_info_table.setItem(
                4, i, QTableWidgetItem(str(hourly_data[i].get('wind'))))
            self.ui.forecast_info_table.setItem(5, i, QTableWidgetItem(
                str(hourly_data[i].get('wind_direction'))))

    def create_observation_table(self, hourly_data):
        """ Creates a tabular form of the past hourly observation data on the past tab
        Parameters
        ----------
        hourly_data : list
            The weather data that is used to create a tabular form of the data
        """
        time_list = []
        category_list = ['Air temperature (°C)', 'Feels like (°C)',
                         'Dew point temperature (°C)', 'Humidity',
                         f'Wind speed ({self.ws_unit})',
                         f'Gust Speed ({self.ws_unit})', 'Wind direction', 'Pressure (hPa)']
        for hour in hourly_data:
            hour_time = hour.get('time')
            time_list.append(hour_time)

        self.ui.observation_info_table.setRowCount(len(category_list))
        self.ui.observation_info_table.setColumnCount(len(time_list))
        self.ui.observation_info_table.setVerticalHeaderLabels(category_list)
        self.ui.observation_info_table.setHorizontalHeaderLabels(time_list)
        self.ui.observation_info_table.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        for i in range(len(time_list)):
            self.ui.observation_info_table.setItem(
                0, i, QTableWidgetItem(str(f'{hourly_data[i].get('temp')}\u00b0')))
            self.ui.observation_info_table.setItem(
                1, i, QTableWidgetItem(str(f'{hourly_data[i].get('feels_like_temp')}\u00b0')))
            self.ui.observation_info_table.setItem(
                2, i, QTableWidgetItem(str(f'{hourly_data[i].get('dew_point')}\u00b0')))
            self.ui.observation_info_table.setItem(
                3, i, QTableWidgetItem(str(f'{hourly_data[i].get('humidity')}%')))
            self.ui.observation_info_table.setItem(
                4, i, QTableWidgetItem(str(hourly_data[i].get('wind_speed'))))
            self.ui.observation_info_table.setItem(
                5, i, QTableWidgetItem(str(hourly_data[i].get('gust_speed'))))
            self.ui.observation_info_table.setItem(
                6, i, QTableWidgetItem(str(hourly_data[i].get('wind_direction'))))
            self.ui.observation_info_table.setItem(
                7, i, QTableWidgetItem(str(hourly_data[i].get('pressure'))))
