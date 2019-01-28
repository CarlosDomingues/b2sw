"""
This module provides helper functions to get data from the Star Wars API
at swapi.co
"""

import requests

from b2sw.config import SwapiConfig


class SwapiSearch:
    """
    SwapiSearch has attributes and methods to do search-type requests to the
    Star Wars API, e.g. 'GET /api/planets/?search=Dagobah'
    """

    def __init__(self, resource, search_value):
        if resource not in SwapiConfig.resources:
            raise ValueError(
                str(resource) + ' not supported. Supported resources: ' +
                str(SwapiConfig.resources)
            )
        if isinstance(search_value, str) is not True:
            raise TypeError(
                'search_value must be a string. Got: ' +
                str(type(search_value))
            )
        self.resource = resource
        self.search_value = str(search_value)

    def build_url(self):
        """
        blabla
        """
        return SwapiConfig.base_url + 'api/{0}/?search={1}'.format(
            self.resource,
            self.search_value
        )

    def search(self):
        """
        TODO - Handle requests.get exception
        """
        url = self.build_url()
        response = requests.get(url, headers=SwapiConfig.headers)
        return response.json()
