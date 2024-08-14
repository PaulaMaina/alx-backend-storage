#!/usr/bin/env python3
"""Redis Basics"""
from typing import Callable, Union
import redis
import uuid


class Cache:
    """Cache Class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    
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
