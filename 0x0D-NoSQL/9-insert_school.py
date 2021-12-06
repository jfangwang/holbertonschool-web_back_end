#!/usr/bin/env python3
"""  inserts a new document in a collection based on kwargs  """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert new doc """
    return mongo_collection.insert_one(kwargs).inserted_id
