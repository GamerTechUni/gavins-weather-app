import json
import datetime
from dateutil import tz
import xml.etree.ElementTree as ET

from ratelimit import limits, sleep_and_retry

import requests

from settings import *


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
    'WA':  'IDW'    # Western Australia
}


@sleep_and_retry
@limits(calls=1, period=0.35)
def fetch_location_options(location):

    # Handles error
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations?search={location}", timeout=90, headers=HEADERS)
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
    response1 = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash}", timeout=90, headers=HEADERS)
    location_info_raw = json.loads(json.dumps(response1.json()))
    response2 = requests.get(f"https://api.weather.bom.gov.au/v1/locations/{
                             geohash[:-1]}/observations", timeout=90, headers=HEADERS)
    observation_data = json.loads(json.dumps(response2.json())).get("data")
    location_info = {'name': check_if_none_value('data', 'name', location_info_raw),
                     'state': check_if_none_value('data', 'state', location_info_raw),
                     'geohash': check_if_none_value('data', 'geohash', location_info_raw),
                     'timezone': check_if_none_value('data', 'timezone', location_info_raw),
                     'station_name': check_if_none_value('station', 'name', observation_data),
                     'station_id': check_if_none_value('station', 'bom_id', observation_data)}

    return location_info


def fetch_observation(geohash, timezone):
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash[:-1]}/observations", timeout=90, headers=HEADERS)
    observation_data = json.loads(json.dumps(response.json())).get("data")
    wind_unit = ''
    if WS_UNIT == 'km/h':
        wind_unit = 'speed_kilometre'
    elif WS_UNIT == 'kn':
        wind_unit = 'speed_knot'
    ob_info = {'max_temp': check_if_none_value("max_temp", "value", observation_data),
               'max_temp_time': parse_time(check_if_none_value("max_temp", "time", observation_data), date_format="hour_minute", utc=True, timezone=timezone),
               'min_temp': check_if_none_value("min_temp", "value", observation_data),
               'min_temp_time': parse_time(check_if_none_value("min_temp", "time", observation_data), date_format="hour_minute", utc=True, timezone=timezone),
               'current_temp': check_if_none_value(None, "temp", observation_data),
               'feels_like_temp': check_if_none_value(None, "temp_feels_like", observation_data),
               'humidity': check_if_none_value(None, "humidity", observation_data),
               'rain_since_9am': check_if_none_value(None, "rain_since_9am", observation_data),
               'wind': check_if_none_value("wind", wind_unit, observation_data),
               'wind_direction': check_if_none_value("wind", "direction", observation_data),
               'gust': check_if_none_value("gust", wind_unit, observation_data),
               'max_gust': check_if_none_value("max_gust", wind_unit, observation_data)}

    # print(observation_data)

    return ob_info


def fetch_daily_forecast(geohash, timezone):
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash}/forecasts/daily", timeout=90, headers=HEADERS)

    forecast_data = json.loads(json.dumps(response.json())).get('data')
    daily_forecast_info = []
    for day in forecast_data:

        forecast_dict = {  # UV Information
            'max_uv_index': check_if_none_value('uv', 'max_index', day),
            'max_uv_category': check_if_none_value('uv', 'category', day),
            'sun_prot_start_time': parse_time(check_if_none_value('uv', 'start_time', day), date_format='hour_minute', utc=True, timezone=timezone),
            'sun_prot_end_time': parse_time(check_if_none_value('uv', 'end_time', day), date_format='hour_minute', utc=True, timezone=timezone),
            # General Info
            'max_temp': check_if_none_value(None, 'temp_max', day),
            'min_temp': check_if_none_value(None, 'temp_min', day),
            'short_text': check_if_none_value(None, 'short_text', day),
            'icon_descriptor': check_if_none_value(None, 'icon_descriptor', day),
            'fire_danger': check_if_none_value(None, 'fire_danger', day),
            'date': parse_time(check_if_none_value(None, 'date', day), date_format='weekday', utc=True, timezone=timezone),
            # Astronomical Info
            'sunrise_time': parse_time(check_if_none_value('astronomical', 'sunrise_time', day), date_format='hour_minute', utc=True, timezone=timezone),
            'sunset_time': parse_time(check_if_none_value('astronomical', 'sunset_time', day), date_format='hour_minute', utc=True, timezone=timezone),
            # Now Information
            'is_night': check_if_none_value('now', 'is_night', day),
            'temp_now': check_if_none_value('now', 'temp_now', day),
            'temp_later': check_if_none_value('now', 'temp_later', day)}
        rain_info = day['rain']
        forecast_dict.update(
            {'min_rain_amount': check_if_none_value('amount', 'min', rain_info),
             'max_rain_amount': check_if_none_value('amount', 'max', rain_info),
             'chance_of_rain': check_if_none_value(None, 'chance', rain_info)})
        daily_forecast_info.append(forecast_dict)
    print(daily_forecast_info[0])
    return daily_forecast_info


def check_if_none_value(key, value_name, data):
    try:
        value = data[key].get(value_name)
        if value == None:
            value = ''
    except KeyError:
        value = data.get(value_name)
        if value == None:
            value = '-'
    except AttributeError:
        value = '-'
    return value


def parse_time(iso_time, date_format, utc, timezone):

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
    response = requests.get(
        f"https://api.weather.bom.gov.au/v1/locations/{geohash[:-1]}/forecasts/hourly", timeout=90, headers=HEADERS)

    hourly_forecast_data = json.loads(
        json.dumps(response.json())).get('data')

    wind_unit = ''
    if WS_UNIT == 'km/h':
        wind_unit = 'speed_kilometre'
    elif WS_UNIT == 'kn':
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
            'time': parse_time(check_if_none_value(None, 'time', hour), date_format='hour_minute', utc=True, timezone=timezone),
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
                'precipitation_amount_10_percent_chance': check_if_none_value(None, 'precipitation_amount_10_percent_chance', rain_info),
                'precipitation_amount_25_percent_chance': check_if_none_value(None, 'precipitation_amount_25_percent_chance', rain_info),
                'precipitation_amount_50_percent_chance': check_if_none_value(None, 'precipitation_amount_50_percent_chance', rain_info)})
        hourly_forecast_info.append(forecast_dict)
    return hourly_forecast_info


def fetch_station_code(bom_code, state):
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
    state_code = STATE_CODES.get(state)
    response = requests.get(
        f"http://www.bom.gov.au/fwo/{state_code}60801/{state_code}60801.{wmo_code}.json", timeout=90, headers=HEADERS)

    hourly_observation_data = json.loads(json.dumps(response.json()))[
        'observations'].get('data')

    wind_unit = ''
    if WS_UNIT == 'km/h':
        wind_unit = 'kmh'
    elif WS_UNIT == 'kn':
        wind_unit = 'kt'

    hourly_observation_info = []
    for hour in hourly_observation_data:

        observation_dict = {'time': parse_time(check_if_none_value(None, 'aifstime_utc', hour), date_format='hour_minute', utc=False, timezone=timezone),
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


if __name__ == "__main__":
    # print(fetch_location_information('r1tuwby'))
    # print(fetch_location_options('Perth'))
    daily_forecast = fetch_daily_forecast('qsycvsc')
    # print(daily_forecast[0])
