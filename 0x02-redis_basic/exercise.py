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

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """
        Retrieves a value from Redis by its key and applies
        an optional transformation.

        Args:
            key (str): The key associated with the value to retrieve.
            fn (Callable, optional): A function to apply to
            the retrieved value
            If not provided, the raw value is returned.

        Returns:
            Union[str, bytes, int, float]: The retrieved value,
            optionally transformed by the provided function.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string value from Redis by its key.

        Args:
            key (str): The key associated with the value to retrieve.

        Returns:
            str: The retrieved string value.
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer value from Redis by its key.

        Args:
            key (str): The key associated with the value to retrieve.

        Returns:
            int: The retrieved integer value.
        """
        return self.get(key, lambda x: int(x))
