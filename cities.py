import json

from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()


def get_cities():
    return cache.get('cities') or load_cities()


def load_cities():
    with open('cities.json', 'r') as cities_file:
        return json.load(cities_file)
