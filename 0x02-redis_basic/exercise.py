#!/usr/bin/env python3
"""Redis Basics"""
from functools import wraps
from typing import Any, Callable, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Keeps track of how many times Cache methods are called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Returns the methos after incrementing the counter"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs of a particular function"""
    @wraps(method)
    def history(self, *args, **kwargs) -> Any:
        """Returns the output of a method"""
        key_in = '{}:inputs'.format(method.__qualname__)
        key_out = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self.redis.rpush(key_in, str(args))
        out = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_out, out)
        return out
    return history


class Cache:
    """Cache Class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis database and returns the key"""
        key_data = str(uuid.uuid4())
        self._redis.set(key_data, data)

        return key_data

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Gets a value from a Redis database"""
        val = self._redis.get(key)
        return fn(val) if fn is not None else val

    def get_str(self, key: str) -> str:
        """Retrieves a string value related to the key"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves an integer related to the key"""
        return self.get(key, lambda i: int(i))
