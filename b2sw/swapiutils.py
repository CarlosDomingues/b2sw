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
        if resource not in SwapiConfig.RESOURCES:
            raise ValueError(
                resource + ' not supported. Supported resources: ' +
                str(SwapiConfig.RESOURCES)
            )
        if isinstance(search_value, str) is not True:
            raise TypeError(
                'search_value must be a string.'
            )
        self.resource = resource
        self. search_value = search_value

    def build_url(self):
        """
        blabla
        """
        return SwapiConfig.BASE_URL + 'api/{0}/?search={1}'.format(
            self.resource,
            self.search_value
        )

    def search(self):
        """
        TODO - Handle requests.get exception
        """
        url = self.build_url()
        response = requests.get(url, headers=SwapiConfig.HEADERS)
        return response.json()
