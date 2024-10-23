#!/usr/bin/env python3
"""
A module for interacting with Redis, a NoSQL key-value store,
providing functionality to store, retrieve, and track the usage of data.
"""
import redis
import uuid
from typing import Any, Callable, Union


class Cache:
    """
    A class for interacting with a Redis data store,
    providing methods to store and retrieve data,
    as well as track method calls and their histories.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache instance with a Redis connection.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a value in the Redis data store and returns a unique key.

        Args:
            data (Union[str, bytes, int, float]):
            The data to be stored in Redis.

        Returns:
            str: The unique key associated with the stored data.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
