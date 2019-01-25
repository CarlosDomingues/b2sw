"""
This module contains functions to interact witth the datbase, as well as schema
enforcing procedures
"""

import boto3


class Planets():
    """
    Represents the 'planets' table.
    """

    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('planets')

    def get_by_name(self, planet_name):
        """
        Returns a planet with name equals 'planet_name'
        TODO - NAME MUST BE VALID
        """
        response = self.table.get_item(
            Key={
                'name': planet_name
            }
        )
        planet = response['Item']
        return planet

    def get_by_id(self, planet_id):
        """
        Returns a planet with id equals 'planet_id'
        TODO - NAME MUST BE VALID
        """
        response = self.table.get_item(
            Key={
                'id': planet_id
            }
        )
        planet = response['Item']
        return planet
