#!/usr/bin/env python3
"""LIFOCache is a caching system that removes the
    last element in the cache to update a new one"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LifoCaching inherit from basecaching using fifo algorithm"""

    def __init__(self):
        """initialize fifocache class constructor"""
        super().__init__()

    def put(self, key, item):
        """store objects in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            last = list(self.cache_data.keys())[-1]
            del self.cache_data[last]
            print("DISCARD: {}".format(last))
        self.cache_data[key] = item

    def get(self, key):
        """get data from the cache"""
        return self.cache_data.get(key)
