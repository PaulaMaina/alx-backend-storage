#!/usr/bin/env python3
"""Web cache and tracker"""
from functools import wraps
from typing import Callable
import redis
import requests


redis_store = redis.Redis()


def data_cache(methos: Callable) -> Callable:
    """Caches output of fetched data"""
    @wraps
    def history(url) -> str:
        """Wrapper function"""
        redis_store.incr(f'count:{url}')
        result = redis_Store.get(f'result:{url}')
        if result:
            return result.decode("utf-8")
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:}', 10, result)
        return result
    return history


@data_cache
def get_page(url: str) -> str:
    """Returns the content of the URL after caching and tracking the request"""
    return requests.get(url).text
