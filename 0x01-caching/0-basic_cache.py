#!/usr/bin/env python3
"""BasicCache inherits from basecache implemented with
    two methods -- put and get"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """creates a basic cache class"""

    def put(self, key, item):
        """save items in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """retrieve elements from the cache"""
        return self.cache_data.get(key, None)
