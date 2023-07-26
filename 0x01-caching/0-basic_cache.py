#!/usr/bin/env python3
"""BasicCache inherits from basecache implemented with
    two methods -- put and get"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """creates a basic cache class"""

    def __init__(self):
        """initialize the class constructor"""
        super().__init__()

    def put(self, key, item):
        """save items in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """retrieve elements from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        else:
            pass
