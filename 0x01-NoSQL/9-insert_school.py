#!/usr/bin/env python3
"""Inserts a new document"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new collection and returns the _id"""
    new_doc = mongo_collection.insert_one(kwargs)

    return new_doc.inserted_id
