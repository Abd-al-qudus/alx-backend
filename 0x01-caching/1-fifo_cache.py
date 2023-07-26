#!/usr/bin/env python3
"""FIFOCache is a caching system that removes the
    first element in the cache to update a new one"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FifoCaching inherit from basecaching using fifo algorithm"""

    def __init__(self):
        """initialize fifocache class constructor"""
        super().__init__()

    def put(self, key, item):
        """store objects in the cache"""
        if key is not None or item is not None:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                del self.cache_data[first]
                print("DISCARD: {}".format(first))
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """get data from the cache"""
        if key is not None:
            return self.cache_data.get(key)
