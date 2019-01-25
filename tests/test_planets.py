"""
Tests related to the planets module.
"""

import unittest
import unittest.mock
import warnings

from b2sw.planets import Planets


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

    @unittest.mock.patch('b2sw.planets.boto3')
    def test_constructor(self, fake_boto3):
        """
        The table object must be create successfuly
        """
        Planets()
        fake_boto3.resource.assert_called_with('dynamodb')
        fake_boto3.resource().Table.assert_called_with('planets')

    @unittest.mock.patch('b2sw.planets.boto3')
    def test_get_by_name(self, fake_boto3):
        """
        get_by_name() should call boto3 with the correct parameters.
        """
        planets = Planets()
        planets.get('Dagobah', key='name')
        fake_boto3.resource().Table().get_item.assert_called_with(
            Key={
                'name': 'Dagobah'
            }
        )

    @unittest.mock.patch('b2sw.planets.boto3')
    def test_get_by_id(self, fake_boto3):
        """
        get_by_id() should call boto3 with the correct parameters.
        """
        planets = Planets()
        planets.get(1, key='id')
        fake_boto3.resource().Table().get_item.assert_called_with(
            Key={
                'id': 1
            }
        )

    @unittest.mock.patch('b2sw.planets.boto3')
    def test_get_invalid_key(self, fake_boto3):
        """
        get_by_id() should raise a ValueError exception if the key is invalid.
        """
        with self.assertRaises(ValueError) as context:
            planets = Planets()
            planets.get(complex(0, 1), key='imaginary_id')
        self.assertTrue(
            'imaginary_id is not a valid search key. Please use one of the following: [id, name]' in str(
                context.exception)
        )

    @unittest.mock.patch('b2sw.planets.boto3')
    def test_get_invalid_value_type(self, fake_boto3):
        """
        get_by_id() should raise a TypeError exception if the given value type
        does not conform with the one expected by the table schema.
        """
        with self.assertRaises(TypeError) as context:
            planets = Planets()
            planets.get('Joe', key='id')
        self.assertTrue(
            "Joe is not a valid id. Expected type: <class 'int'>. Actual type: <class 'str'>"
            in str(
                context.exception)
        )
