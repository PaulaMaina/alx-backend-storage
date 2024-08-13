#!/usr/bin/env python3
"""Lists schools based on a specific topics"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools that match a specific topic"""
    query = {
        'topics': {
            '$eq': topic
        },
    }

    return mongo_collection.find(query)
