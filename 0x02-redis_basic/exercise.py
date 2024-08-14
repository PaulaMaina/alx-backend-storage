#!/usr/bin/env python3
"""Redis Basics"""
from typing import Union
import redis
import uuid


Class Cache:
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
