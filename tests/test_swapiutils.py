"""
Tests related to the swapiutils module.
"""

import unittest
import unittest.mock

import responses

from b2sw.swapiutils import SwapiSearch
from b2sw.config import SwapiConfig


class TestSwapiSearch(unittest.TestCase):
    """
    Tests related to the SwapiSearch class.
    """

    def setUp(self):
        """
        We must override user-defined configuration to guarantee tests will
        be deterministic.
        """
        SwapiConfig.BASE_URL = 'http://swapi.co/'
        SwapiConfig.HEADERS = {'User-Agent': 'swapi-python'}
        SwapiConfig.RESOURCES = ['planets']

    def test_constructor(self):
        """
        SwapiSearch should have its attributes initialized correctly.
        """
        my_search = SwapiSearch('planets', 'Dagobah')
        self.assertEqual(my_search.resource, 'planets')
        self.assertEqual(my_search.search_value, 'Dagobah')

    def test_invalid_resource(self):
        """
        SwapiSearch should raise a ValueError exception if the passed resource
        is not valid.
        """
        with self.assertRaises(ValueError) as context:
            SwapiSearch('dogs', 'Dagobah')
        self.assertTrue(
            "dogs not supported. Supported resources: ['planets']"
            in str(context.exception)
        )

    def test_invalid_search_value(self):
        """
        SwapiSearch should raise a TypeError exception if the passed
        search_value is not a string..
        """
        with self.assertRaises(TypeError) as context:
            SwapiSearch('planets', 95)
        self.assertTrue(
            "search_value must be a string. Got: <class 'int'>"
            in str(context.exception)
        )

    def test_build_url(self):
        """
        The build_url method should construct a valid swapi.co url.
        """
        my_search = SwapiSearch('planets', 'Dagobah')
        url = my_search.build_url()
        self.assertEqual(url, 'http://swapi.co/api/planets/?search=Dagobah')

    @unittest.mock.patch('requests.get')
    def test_search_call(self, requests_get):
        """
        The search method should call requests.get with the correct parameters.
        """
        my_search = SwapiSearch('planets', 'Dagobah')
        my_search.search()
        requests_get.assert_called_with(
            'http://swapi.co/api/planets/?search=Dagobah',
            headers={'User-Agent': 'swapi-python'}
        )

    @responses.activate
    def test_search_return(self):
        """
        The search method should call return a dictionary if the request is
        successful.
        """
        responses.add(
            responses.GET,
            'http://swapi.co/api/planets/?search=Dagobah',
            json={
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "name": "Dagobah",
                        "rotation_period": "23",
                        "orbital_period": "341",
                        "diameter": "8900",
                        "climate": "murky",
                        "gravity": "N/A",
                        "terrain": "swamp, jungles",
                        "surface_water": "8",
                        "population": "unknown",
                        "residents": [],
                        "films": [
                            "https://swapi.co/api/films/2/",
                            "https://swapi.co/api/films/6/",
                            "https://swapi.co/api/films/3/"
                        ],
                        "created": "2014-12-10T11:42:22.590000Z",
                        "edited": "2014-12-20T20:58:18.425000Z",
                        "url": "https://swapi.co/api/planets/5/"
                    }
                ]
            },
            status=200
        )
        my_search = SwapiSearch('planets', 'Dagobah')
        result = my_search.search()
        self.assertEqual(
            result['results'][0]['name'],
            'Dagobah'
        )
