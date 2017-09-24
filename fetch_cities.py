import json

import requests


SOURCE_URL = "https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"
MAX_CITIES = 100


def fetch_and_parse(url=SOURCE_URL):
    response = requests.get(url)
    if response.ok:
        parsed_cities = []
        for idx, city_dict in enumerate(response.json()):
            if idx >= 100:
                break

            parsed_cities.append(city_dict)

        with open('cities.json', 'w+') as cities_file:
            json.dump(parsed_cities, cities_file)


if __name__ == '__main__':
    fetch_and_parse()
