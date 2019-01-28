"""
This module contains functions to interact with the database, as well as
schema enforcing procedures.
"""
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute


class Planets(Model):
    """
    Describes the schema used on our DynamoDB table.
    """
    class Meta:
        """
        Table name on DynamoDB
        """
        table_name = 'Planets'
    climate = ListAttribute(null=False)
    terrain = ListAttribute(null=False)
    name = UnicodeAttribute(null=False)
    planet_id = NumberAttribute(hash_key=True)
    read_capacity_units = 5
    write_capacity_units = 5
    region = 'us-east-1'


def get_by_id(planet_id):
    """
    Returns the planet with the specified planet_id.
    """
    planet = Planets.get(planet_id)
    return planet


def get_by_name(name):
    """
    Returns the planet with the specified name.
    TODO - Raise exception if planet does not exist
    """
    planets = [x for x in Planets.scan(Planets.name == name)]
    return planets


def delete(planet_id):
    """
    Deletes the planet with the specified planet_id
    """
    planet = Planets.get(planet_id)
    planet.delete()


def put(planet_id, name, climate, terrain):
    """
    Creates a new planet and adds it to the database.
    TODO - Planet name must be unique.
    """
    planet = Planets(planet_id)
    planet.name = name
    planet.climate = climate
    planet.terrain = terrain
    planet.save()


def update(planet_id, name=None, climate=None, terrain=None):
    """
    Updates the attributes of an existing planet.
    """
    planet = Planets.get(planet_id)
    if name is not None:
        planet.name = name
    if name is not None:
        planet.climate = climate
    if name is not None:
        planet.terrain = terrain
    planet.refresh()
