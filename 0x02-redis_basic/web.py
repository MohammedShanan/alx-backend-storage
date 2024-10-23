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
    redis_store.incr(f"count:{url}")

    result = redis_store.get(f"result:{url}")
    if result:
        return result.decode("utf-8")

    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.text
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"

    redis_store.setex(f"result:{url}", 10, result)

    return result
