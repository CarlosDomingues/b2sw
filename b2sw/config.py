"""
Configuration parameters
"""


class SwapiConfig:
    """
    Default configuration for the `swapiutils` module.
    """
    base_url = 'http://swapi.co/'
    headers = {'User-Agent': 'swapi-python'}
    resources = ['planets']


class PlanetsConfig:
    """
    Default configuration for the `planets` module.
    """
    table_name = 'Planets'
    region = 'us-east-1'
