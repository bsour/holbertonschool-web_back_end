#!/usr/bin/env python3
"""
Module to update topics of school documents based on the school name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of school documents in a
    MongoDB collection based on the school name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics to set for the school.

    Returns:
        int: The number of documents modified by the update operation.
    """
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
    return result
