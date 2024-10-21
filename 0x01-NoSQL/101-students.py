#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """Prints all students in a collection sorted by average score"""
    students = mongo_collection.aggregate(
        [
            {"$unwind": "$topics"},  # Deconstructs the topics array
            {
                "$group": {
                    "_id": "$name",  # Group by student name
                    "averageScore": {
                        "$avg": "$topics.score"
                    },  # Calculate the average score
                    "topics": {
                        "$push": "$topics"
                    },  # Optional: collect topics back into an array
                },
            },
            {
                "$sort": {"averageScore": -1}
            },  # Sort by average score in descending order
        ]
    )
    return students
