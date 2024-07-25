#!/usr/bin/env python3
"""1. FIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A basic cache implementation that extends the BaseCashing class.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.cache_data.popitem()[0]
            print(f"DISCARD: {discarded}")
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item from the cache with the specified key.
        """
        return self.cache_data.get(key, None)
