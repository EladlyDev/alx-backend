#!/usr/bin/env python3
""" contains the BasicCashe class """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache implementation that extends the BaseCashing class.
    """

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.
        """
        if (key and item):
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Retrieves the item from the cache with the specified key.
        """
        return self.cache_data.get(key, None)
