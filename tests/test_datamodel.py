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

    @unittest.mock.patch('b2sw.datamodel.boto3')
    def test_constructor(self, fake_boto3):
        """
        The table object must be create successfuly
        """
        Planets()
        fake_boto3.resource.assert_called_with('dynamodb')
        fake_boto3.resource().Table.assert_called_with('planets')

    @unittest.mock.patch('b2sw.datamodel.boto3')
    def test_get_planet(self, fake_boto3):
        """
        get() should call boto3 with the correct parameters.
        """
        planets = Planets()
        planets.get('Dagobah')
        fake_boto3.resource().Table().get_item.assert_called_with(
            Key={
                'name': 'Dagobah'
            }
        )
