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
