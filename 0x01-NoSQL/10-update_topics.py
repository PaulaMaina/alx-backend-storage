#!/usr/bin/env python3
"""Changes all topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Updates topics that match name"""
    query = {name: name}
    new_topics = {"$set": {topics: topics}}

    mongo_collection.update_many(query, new_topics)
