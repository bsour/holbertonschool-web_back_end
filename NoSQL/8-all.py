#!/usr/bin/env python3
'''
Python function that lists all documents in a collection
'''
import pymongo


def list_all(mongo_collection):
    '''
    return all documents in the collection
    return empty list if no document
    '''
    cursor = mongo_collection.finc({})

    documents = []
    for document in cursor:
        documents.append(document)
    return documents
