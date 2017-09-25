from datetime import datetime, timedelta

import requests

API_KEY = "0e660ad4bd38a8bd"  # I don't usually commit my API keys


def get_current_conditions(city, state):
    url_template = 'https://api.wunderground.com/api/{api_key}/geolookup/conditions/q/{state}/{city}.json'
    url = url_template.format(api_key=API_KEY,
                              state=state,
                              city=city)
    response = requests.get(url)
    parsed_json = response.json()
    current_temp_f = parsed_json['current_observation']['temp_f']
    current_condition = parsed_json['current_observation']['weather']
    # print "Current temperature in %s is: %s" % (location, temp_f)
    return (current_temp_f, current_condition)


def get_average_temperature(city, state):
    now = datetime.utcnow()
    thirty_days_ago = now - timedelta(days=30)

    date_range_string = "%s%s" % (thirty_days_ago.strftime("%m%d"), now.strftime("%m%d"))
    url_template = 'https://api.wunderground.com/api/{api_key}/planner_{date_range}/q/{state}/{city}.json'
    url = url_template.format(api_key=API_KEY,
                              date_range=date_range_string,
                              state=state,
                              city=city)

    response = requests.get(url)
    parsed_json = response.json()
    average_low = int(parsed_json['trip']['temp_low']['avg']['F'])
    average_high = int(parsed_json['trip']['temp_high']['avg']['F'])

    return (average_low + average_high)/2
