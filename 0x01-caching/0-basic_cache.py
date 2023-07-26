#!/usr/bin/env python3
"""BasicCache inherits from basecache implemented with
    two methods -- put and get"""
from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """creates a basic cache class"""

    def __init__(self) -> None:
        """initialize the class constructor"""
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """save items in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key: Any) -> Any:
        """retrieve elements from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        else:
            pass
