#!/usr/bin/env python3
"""
Module to insert a new document in a MongoDB collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new school document in a MongoDB collection based on keyword arguments.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the fields and values for the new document.

    Returns:
        The new _id of the inserted document.
    """
    new_school = kwargs  # Create a dictionary from kwargs
    result = mongo_collection.insert_one(new_school)
    return result.inserted_id
