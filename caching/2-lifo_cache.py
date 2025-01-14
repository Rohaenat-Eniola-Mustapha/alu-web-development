#!/usr/bin/python3
""" LIFO Caching Module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache System """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item in the cache using LIFO policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """
        Get an item by key from the cache.
        """
        return self.cache_data.get(key, None)
