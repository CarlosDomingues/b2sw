"""
Tests related to the datamodel module.
"""

import unittest
import unittest.mock
import warnings

from b2sw.datamodel import Planets


class TestPlanets(unittest.TestCase):
    """
    Tests related to the Planets class
    """

    def setUp(self):
        """
        Ignore boto3 SSL Socket Warnings, please see:
        https://github.com/boto/boto3/issues/454
        """
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<ssl.SSLSocket.*>"
        )

    def test_constructor(self):
        """
        The table object must be create successfuly
        """
        planets = Planets()
        self.assertEqual(planets.table.name, 'planets')

    @unittest.mock.patch.object('boto3.resources.factory.dynamodb.Table', 'get_item')
    def test_get_planet(self, fake_get_item):
        """
        get() should call boto3 with the correct parameters.
        """
        # reponse {'id': Decimal('1'), 'climate': 'murky', 'name': 'Dagobah', 'terrain': ['swamp', 'jungles']}
        planets = Planets()
        fake_get_item.return_value = 'a'
        planet = planets.get('Dagobah')
        self.assertEqual(planet['name'], 'Dagobah')
