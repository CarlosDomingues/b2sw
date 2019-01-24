"""
Configuration parameters
"""


class SwapiConfig:
    """
    Default configuration for the `swapiutils` module.
    """
    BASE_URL = 'http://swapi.co/'
    HEADERS = {'User-Agent': 'swapi-python'}
    RESOURCES = ['planets']
