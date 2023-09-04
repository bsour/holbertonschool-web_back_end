#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of all documents in the collection,
    or an empty list if no documents are found.
    """
    cursor = mongo_collection.find({})
    documents = list(cursor)
    return documents
