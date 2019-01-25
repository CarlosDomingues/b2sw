"""
Tests related to the app module.
"""

import unittest
import unittest.mock

import flask_api

from b2sw.app import create_app


class TestApp(unittest.TestCase):
    """
    Tests related to the app object.
    """

    def test_create_app(self):
        """
        Create app should correctly return a Flask-API appself.
        """
        self.assertTrue(
            isinstance(
                create_app(),
                flask_api.app.FlaskAPI
            )
        )
