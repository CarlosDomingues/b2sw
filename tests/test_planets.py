"""
Tests related to the planets module.
"""

import unittest
import unittest.mock


from b2sw import planets


class TestPlanets(unittest.TestCase):
    """
    Tests related to the Planets class
    """

    @unittest.mock.patch('b2sw.planets.Planets')
    def test_get_by_id(self, fake_table):
        """
        get_by_id should call PynamoDB API correctly.
        """
        planets.get_by_id(1)
        fake_table.get.assert_called_with(1)

    @unittest.mock.patch('b2sw.planets.Planets')
    def test_get_by_name(self, fake_table):
        """
        get_by_name should call PynamoDB API correctly.
        """
        planets.get_by_name('Pluto')
        fake_table.scan.assert_called_with(fake_table.name == 'Pluto')

    @unittest.mock.patch('b2sw.planets.Planets')
    def test_put(self, fake_table):
        """
        put should call PynamoDB API correctly.
        """
        planets.put(
            1,
            'Pluto',
            ['Cold', 'Very Cold'],
            ['Ice']
        )
        fake_table().save.assert_called_with()

    @unittest.mock.patch('b2sw.planets.Planets')
    def test_delete(self, fake_table):
        """
        delete should call PynamoDB API correctly.
        """
        planets.delete(1)
        fake_table.get.assert_called_with(1)
        fake_table.get().delete.assert_called_with()

    @unittest.mock.patch('b2sw.planets.Planets')
    def test_update(self, fake_table):
        """
        delete should call PynamoDB API correctly.
        """
        planets.update(1, name='New Pluto')
        fake_table.get.assert_called_with(1)
        fake_table.get().refresh.assert_called_with()
