#!/usr/bin/env python3
"""
Module to retrieve a list of schools that have a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools that have a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents that have the specified topic.
    """
    # Use the find method to query documents with the specified topic
    cursor = mongo_collection.find({"topics": topic})
    # Convert the cursor to a list of documents
    schools = list(cursor)
    return schools
