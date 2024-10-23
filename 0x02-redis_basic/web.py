#!/usr/bin/env python3
"""
A module providing tools for request caching and tracking 
using Redis as the backend.
"""
import redis
import requests

redis_store = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the content of a URL, caches the response, and tracks access.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.
    """
    # Increment access count in Redis
    redis_store.incr(f"count:{url}")

    # Check if result is cached in Redis
    result = redis_store.get(f"result:{url}")
    if result:
        # Return cached result if available
        return result.decode("utf-8")

    # Fetch fresh data if not cached
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.text
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"

    # Cache the result in Redis with a 10-second expiration
    redis_store.setex(f"result:{url}", 10, result)

    # Return the fetched result
    return result
