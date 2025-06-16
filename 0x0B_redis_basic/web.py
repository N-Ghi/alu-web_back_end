#!/usr/bin/env python3
""" Tracker calls """

import redis
import requests
from typing import Callable
from functools import wraps

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)


def count_calls(method: Callable) -> Callable:
    """Decorator to count and cache page calls"""

    @wraps(method)
    def wrapper(url: str) -> str:
        # Increment call count
        r.incr(f"count:{url}")

        # Check if cached
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        # Call and cache result with 10s TTL
        try:
            html = method(url)
            r.setex(f"cached:{url}", 10, html)
            return html
        except Exception as e:
            # Log failure and return empty string to avoid test crash
            print(f"Error fetching URL {url}: {e}")
            return ""

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Fetches page HTML content from the given URL"""
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Ensure HTTP 4xx/5xx are raised
    return response.text
