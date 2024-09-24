""" Backend for Weather App
The backend program provides functions that can retrieve weather data from the
Bureau of Meteorology, using the appropriate API endpoints and third party modules
to retrieve the data. 

Most functions in this program require a geohash and a timezone parameter to be passed in,
but they can be acquired easily.

The program requires that the 'python-dateutil', 'ratelimit' and 'requests' libraries be installed
within the Python environment you are running the program in.

The functions within this file are intended to be imported into other programs for use within them,
where the following functions are included:

    * read_settings - returns entry value from settings.ini file
    * write_to_settings - writes entry value to settings.ini file
    * fetch_location_options - returns dictionary pair with location and corresponding geohash
    * fetch_location_information - returns data about geohash location
    * fetch_observation - returns observations from weather station
    * fetch_daily_forecast - returns forecast info for each day
    * check_if_none_value - returns '-' if value == None, else return normal value
    * parse_time - return local time of timestamp based on timezone param passed in
    * fetch_hourly_forecast - returns hourly forecast data for a location
    * fetch_station_code - returns wmo code for weather station based on bom code
    * fetch_hourly_observations - returns past hourly observations for a weather station

"""

import json
import datetime
import configparser
import xml.etree.ElementTree as ET
from dateutil import tz
from ratelimit import limits, sleep_and_retry
import requests


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
}

STATE_CODES = {
    'ACT': 'IDN',   # Australian Capital Territory
    'NSW': 'IDN',   # New South Wales
    'NT':  'IDD',   # Northern Territory
    'QLD': 'IDQ',   # Queensland
    'SA':  'IDS',   # South Australia
    'TAS': 'IDT',   # Tasmania
    'VIC': 'IDV',   # Victoria
    'WA':  'IDW',   # Western Australia
    'OT': 'IDQ'     # Torres Strait Islands
}


def read_settings(entry):
    """ Reads value from settings.ini value and returns it

    Parameters
    ----------
    entry : str
        The name of the entry to get value of 

    Returns
    -------
    value : str
        Value of the settings entry 
    """
    config = configparser.ConfigParser()
    config.read('settings.ini')
    value = config['Default'][entry]
    return value


def write_to_settings(entry, value):
    """ Overvwrites settings.ini entry value with given value

    Parameters
    ----------
    entry : str
        The name of the entry to edit
    value : str
        The value that will replace the current value of the netry 

    """
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config['Default'][entry] = value
    with open('settings.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


@sleep_and_retry
@limits(calls=1, period=0.35)
def fetch_location_options(location):
    """ Takes location input and returns a dictionary of locations and geohashes

    Parameters
    ----------
    location : str
        The name of the location (must be in Australia) 

    Returns
    -------
    location_and_geohash : dict
        A key value pair, with the key being locations and the value being the corresponding geohash
    """
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations?search={location}",
        timeout=90, headers=HEADERS)
    location_options = json.loads(json.dumps(response.json()))
    locations_data = location_options.get("data")
    locations = []
    geohashs = []
    for place in locations_data:
        location = f"{place.get("name")}, {place.get("state")} {
            place.get("postcode")}"
        geohash = place.get("geohash")
        locations.append(location)
        geohashs.append(geohash)

    location_and_geohash = dict(zip(locations, geohashs))

    return location_and_geohash


def fetch_location_information(geohash):
    """ Retrieves information about location

    Parameters
    ----------
    geohash : str
        A seven character string identification for a location used by the BOM (e.g. r1nwvj5)

    Returns
    -------
    location_info : dict
        Pairs containing location data extracted from BOM API request 
    """
    response1 = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash}",
        timeout=90, headers=HEADERS)
    location_info_raw = json.loads(json.dumps(response1.json()))
    response2 = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash[:-1]}/observations",
        timeout=90, headers=HEADERS)
    observation_data = json.loads(json.dumps(response2.json())).get("data")
    location_info = {'name': check_if_none_value('data', 'name', location_info_raw),
                     'state': check_if_none_value('data', 'state', location_info_raw),
                     'geohash': check_if_none_value('data', 'geohash', location_info_raw),
                     'timezone': check_if_none_value('data', 'timezone', location_info_raw),
                     'station_name': check_if_none_value('station', 'name', observation_data),
                     'station_id': check_if_none_value('station', 'bom_id', observation_data)}

    return location_info


def fetch_observation(geohash, timezone):
    """ Retrieves current observations from a location

    Parameters
    ----------
    geohash : str
        A seven character string identification for a location used by the BOM (e.g. 'r1nwvj5')
    timezone : str
        Provides the function with appropriate timezone (e.g. 'Australia/Melbourne')

    Returns
    -------
    ob_info : dict
        Pairs containing observation data for location extracted from BOM API request 
    """
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash[:-1]}/observations",
        timeout=90, headers=HEADERS)
    observation_data = json.loads(json.dumps(response.json())).get("data")
    ws_unit = read_settings('ws_unit')
    wind_unit = ''
    if ws_unit == 'km/h':
        wind_unit = 'speed_kilometre'
    elif ws_unit == 'kn':
        wind_unit = 'speed_knot'
    ob_info = {'max_temp': check_if_none_value("max_temp", "value", observation_data),
               'max_temp_time': parse_time(
                    check_if_none_value("max_temp", "time", observation_data),
                    date_format="hour_minute", utc=True, timezone=timezone),
               'min_temp': check_if_none_value("min_temp", "value", observation_data),
               'min_temp_time': parse_time(
                    check_if_none_value("min_temp", "time", observation_data),
                    date_format="hour_minute", utc=True, timezone=timezone),
               'current_temp': check_if_none_value(None, "temp", observation_data),
               'feels_like_temp': check_if_none_value(None, "temp_feels_like", observation_data),
               'humidity': check_if_none_value(None, "humidity", observation_data),
               'rain_since_9am': check_if_none_value(None, "rain_since_9am", observation_data),
               'wind': check_if_none_value("wind", wind_unit, observation_data),
               'wind_direction': check_if_none_value("wind", "direction", observation_data),
               'gust': check_if_none_value("gust", wind_unit, observation_data),
               'max_gust': check_if_none_value("max_gust", wind_unit, observation_data),
               'max_gust_time': parse_time(
                    check_if_none_value("max_gust", 'time', observation_data),
                    date_format="hour_minute", utc=True, timezone=timezone)}

    return ob_info


def fetch_daily_forecast(geohash, timezone):
    """ Retrieves forecast data for each day
    Parameters
    ----------
    geohash : str
        A seven character string identification for a location used by the BOM (e.g. 'r1nwvj5')
    timezone : str
        Provides the function with appropriate timezone (e.g. 'Australia/Melbourne')

    Returns
    -------
    ob_info : dict
        Pairs containing daily forecast data for the location extracted from BOM API request 
    """
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash}/forecasts/daily",
        timeout=90, headers=HEADERS)

    forecast_data = json.loads(json.dumps(response.json())).get('data')
    daily_forecast_info = []
    for day in forecast_data:

        forecast_dict = {  # UV Information
            'max_uv_index': check_if_none_value('uv', 'max_index', day),
            'max_uv_category': check_if_none_value('uv', 'category', day),
            'sun_prot_start_time': parse_time(
                check_if_none_value('uv', 'start_time', day),
                date_format='hour_minute', utc=True, timezone=timezone),
            'sun_prot_end_time': parse_time(
                check_if_none_value('uv', 'end_time', day),
                date_format='hour_minute', utc=True, timezone=timezone),
            # General Info
            'max_temp': check_if_none_value(None, 'temp_max', day),
            'min_temp': check_if_none_value(None, 'temp_min', day),
            'short_text': check_if_none_value(None, 'short_text', day),
            'icon_descriptor': check_if_none_value(None, 'icon_descriptor', day),
            'fire_danger': check_if_none_value(None, 'fire_danger', day),
            'date': parse_time(
                check_if_none_value(None, 'date', day),
                date_format='weekday', utc=True, timezone=timezone),
            # Astronomical Info
            'sunrise_time': parse_time(
                check_if_none_value('astronomical', 'sunrise_time', day),
                date_format='hour_minute', utc=True, timezone=timezone),
            'sunset_time': parse_time(
                check_if_none_value('astronomical', 'sunset_time', day),
                date_format='hour_minute', utc=True, timezone=timezone),
            # Now Information
            'is_night': check_if_none_value('now', 'is_night', day),
            'temp_now': check_if_none_value('now', 'temp_now', day),
            'temp_later': check_if_none_value('now', 'temp_later', day)}
        rain_info = day['rain']

        # Rain Information
        forecast_dict.update(
            {'min_rain_amount': check_if_none_value('amount', 'min', rain_info),
             'max_rain_amount': check_if_none_value('amount', 'max', rain_info),
             'chance_of_rain': check_if_none_value(None, 'chance', rain_info)})
        daily_forecast_info.append(forecast_dict)
    return daily_forecast_info


def check_if_none_value(key, value_name, data):
    """ Validates if a value contains data, otherwise a placeholder value is set
    Parameters
    ----------
    key
        The top level key for the data, can be a None value if the top level key doesn't exist

    value_name : str
        A key value that is nested inside the 'key' param, which the value is extracted from
    data : dict
        The dictionary weather data set that the 'key' and 'value_name' params are tested against

    Returns
    -------
    ob_info : str
        If the value is not a None value, it will return the regular value extracted from the data
    """
    try:
        value = data[key].get(value_name)
        if value is None:
            value = ''
    except KeyError:
        value = data.get(value_name)
        if value is None:
            value = '-'
    except AttributeError:
        value = '-'
    return value


def parse_time(iso_time, date_format, utc, timezone):
    """ Converts timestamps into readable time formats
    Parameters
    ----------
    iso_time : str
        The timestamp which the function will convert into local time
    date_format : str
        Tells how the output of the function should look like (e.g 'hour_minute' means 10:30am)
    utc : bool
        Tells whether the timestamp needs to be converted to a iso timestamp first 
    timezone: str
        Tells what timezone the timestamp should be converted to (i.e 'Australia/Melbourne)

    Returns
    -------
    local_time : str
        Returns a readable time format based on the params passed
    """
    if utc:
        try:
            tz_data = tz.gettz(timezone)
            dt = datetime.datetime.fromisoformat(iso_time)
            if date_format == 'hour_minute':
                local_time = datetime.datetime.strftime(
                    dt.astimezone(tz_data), "%I:%M%p")
            elif date_format == 'weekday':
                local_time = datetime.datetime.strftime(
                    dt.astimezone(tz_data), "%A")
            else:
                local_time = datetime.datetime.strftime(
                    dt.astimezone(tz_data), "%d/%m/%Y %I:%M%p")
        except ValueError:
            local_time = ''

    else:
        try:
            tz_data = tz.gettz(timezone)
            format_string = '%Y%m%d%H%M%S'
            split_time = datetime.datetime.strptime(iso_time, format_string)
            converted_time = f"{split_time.isoformat()}Z"
            dt = datetime.datetime.fromisoformat(converted_time)
            if date_format == 'hour_minute':
                local_time = datetime.datetime.strftime(
                    dt.astimezone(tz_data), "%I:%M%p")
            elif date_format == 'weekday':
                local_time = datetime.datetime.strftime(
                    dt.astimezone(tz_data), "%A")
            else:
                local_time = datetime.datetime.strftime(
                    dt.astimezone(tz_data), "%d/%m/%Y %I:%M%p")
        except ValueError:
            local_time = ''

    return local_time


def fetch_hourly_forecast(geohash, timezone):
    """ Retrieves forecast data for each hour
    Parameters
    ----------
    geohash : str
        A seven character string identification for a location used by the BOM (e.g. 'r1nwvj5')
    timezone : str
        Provides the function with appropriate timezone (e.g. 'Australia/Melbourne')

    Returns
    -------
    hourly_forecast_info : list
        A list of hours containing dictionaries of forecasted weather data for each hour
    """
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash[:-1]}/forecasts/hourly", timeout=90, headers=HEADERS)

    hourly_forecast_data = json.loads(
        json.dumps(response.json())).get('data')

    ws_unit = read_settings('ws_unit')
    wind_unit = ''
    if ws_unit == 'km/h':
        wind_unit = 'speed_kilometre'
    elif ws_unit == 'kn':
        wind_unit = 'speed_knot'

    hourly_forecast_info = []
    for hour in hourly_forecast_data:

        forecast_dict = {  # UV Information
            'uv_index': check_if_none_value(None, 'uv', hour),
            # General Info
            'temp': check_if_none_value(None, 'temp', hour),
            'feels_like_temp': check_if_none_value(None, 'temp_feels_like', hour),
            'dew_point': check_if_none_value(None, 'dew_point', hour),
            'icon_descriptor': check_if_none_value(None, 'icon_descriptor', hour),
            'time': parse_time(check_if_none_value(
                None, 'time', hour), date_format='hour_minute', utc=True, timezone=timezone),
            # Now Information
            'is_night': check_if_none_value('now', 'is_night', hour),
            'relative_humidity': check_if_none_value(None, 'relative_humidity', hour),
            'wind': check_if_none_value('wind', wind_unit, hour),
            'wind_direction': check_if_none_value('wind', 'direction', hour)}
        rain_info = hour['rain']
        forecast_dict.update(
            {'min_rain_amount': check_if_none_value('amount', 'min', rain_info),
                'max_rain_amount': check_if_none_value('amount', 'max', rain_info),
                'chance_of_rain': check_if_none_value(None, 'chance', rain_info),
                'precipitation_amount_10_percent_chance': check_if_none_value(
                    None, 'precipitation_amount_10_percent_chance', rain_info),
                'precipitation_amount_25_percent_chance': check_if_none_value(
                    None, 'precipitation_amount_25_percent_chance', rain_info),
                'precipitation_amount_50_percent_chance': check_if_none_value(
                    None, 'precipitation_amount_50_percent_chance', rain_info)})
        hourly_forecast_info.append(forecast_dict)
    return hourly_forecast_info


def fetch_station_code(bom_code, state):
    """ Converts a 'bom code' into a 'wmo code'
    Parameters
    ----------
    bom_code : str
        A six digit code to identify weather stations, gathered from location info
    state : str
        A state code used to identify which xml file to look through to find wmo code for station

    Returns
    -------
    wmo_code : str
        A five digit code to request hourly observation data from weather station
    """
    state_code = STATE_CODES.get(state)
    tree = ET.parse(f'xml_data/{state_code}60920.xml')
    root = tree.getroot()
    station_code_pair = {}
    for x in root[1]:
        station_values = x.attrib
        station_code_pair.update(
            {station_values.get('bom-id'): station_values.get('wmo-id')})

    wmo_code = station_code_pair.get(bom_code)
    return wmo_code


def fetch_hourly_observations(wmo_code, state, timezone):
    """ Retrieves past observations for a weather station using 'wmo code'
    Parameters
    ----------
    wmo_code : str
        A five digit code to request hourly observation data from weather station
    state : str
        A state code used to identify the state for the appropriate JSON request
    timezone : str
        Provides the function with appropriate timezone (e.g. 'Australia/Melbourne')

    Returns
    -------
    hourly_observation_info : dict
        A list of hours containing dictionaries of past weather data for each hour
    """
    state_code = STATE_CODES.get(state)
    response = requests.get(
        f"http://www.bom.gov.au/fwo/{state_code}60801/{state_code}60801.{wmo_code}.json",
        timeout=90, headers=HEADERS)

    hourly_observation_data = json.loads(json.dumps(response.json()))[
        'observations'].get('data')

    ws_unit = read_settings('ws_unit')
    wind_unit = ''
    if ws_unit == 'km/h':
        wind_unit = 'kmh'
    elif ws_unit == 'kn':
        wind_unit = 'kt'

    hourly_observation_info = []
    for hour in hourly_observation_data:

        observation_dict = {'time': parse_time(
                                check_if_none_value(None, 'aifstime_utc', hour),
                                date_format='hour_minute', utc=False, timezone=timezone),
                            'name': check_if_none_value(None, 'name', hour),
                            'temp': check_if_none_value(None, 'air_temp', hour),
                            'feels_like_temp': check_if_none_value(None, 'apparent_t', hour),
                            'humidity': check_if_none_value(None, 'rel_hum', hour),
                            'wind_speed': check_if_none_value(None, f'wind_spd_{wind_unit}', hour),
                            'gust_speed': check_if_none_value(None, f'gust_{wind_unit}', hour),
                            'wind_direction': check_if_none_value(None, 'wind_dir', hour),
                            'rain_since_9am': check_if_none_value(None, 'rain_trace', hour),
                            'pressure': check_if_none_value(None, 'press', hour),
                            'dew_point': check_if_none_value(None, 'dewpt', hour)}
        hourly_observation_info.append(observation_dict)
    return hourly_observation_info
