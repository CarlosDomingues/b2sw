"""
This module contains functions to interact with the database, as well as
schema enforcing procedures.
"""

import boto3


class Planets():
    """
    Represents the 'planets' table.
    TODO - ALLOW SCHEMA TO BE CONFIGURABLE
    """

    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('planets')
        self.schema = {
            'primary_keys': {
                'id':   int,
                'name': str
            },
            'other_keys': {
                'climate': str,
                'terrain': str
            }
        }

    def get(self, key_value, key):
        """
        Queries a planet using one of the allowed keys defined on
        self.schema['primary_keys']
        """
        if key not in self.schema['primary_keys']:
            raise ValueError(
                key + ' is not a valid search key. Please use one of the following: ' +
                str(list(self.schema['primary_keys'].keys())).replace('\'', '')
            )
        if isinstance(key_value, self.schema['primary_keys'][key]) is False:
            raise TypeError(
                key_value + ' is not a valid ' + key + '. Expected type: ' +
                str(self.schema['primary_keys'][key]) + '. Actual type: ' +
                str(type(key_value))
            )
        response = self.table.get_item(
            Key={
                # Since we only test with isinstance, the type of key_value
                # might not be what boto3 expects and we need to cast it to
                # the correct one.
                # Example: isinstance(True, int) -> True int(True) -> 1
                key: self.schema['primary_keys'][key](key_value)
            }
        )
        planet = response['Item']
        return planet

    def put(self, planet_id, name, climate, terrain):
        """
        Creates a new planet on the database
        """
        self.table.put_item(
            Item={
                'id': planet_id,
                'name': name,
                'climate': climate,
                'terrain': terrain,
            }
        )
