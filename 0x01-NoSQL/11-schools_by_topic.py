#!/usr/bin/env python3
"""function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic"""
    return [doc for doc in mongo_collection.find({"topics": topic})]
