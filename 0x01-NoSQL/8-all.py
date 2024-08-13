#!/usr/bin/env python3
"""Lists all documents in a collection"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """Returns a list of documents in a collection"""
    doc_list = []

    client = MongoClient()
    col = db["mongo_collection"]

    for doc in col.find():
        doc_list.append(doc)

    return doc_list
