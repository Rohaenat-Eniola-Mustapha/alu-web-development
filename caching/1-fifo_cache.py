#!/usr/bin/python3
""" FIFO caching module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache System """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Get an item by key from the cache.
        """
        return self.cache_data.get(key, None)
