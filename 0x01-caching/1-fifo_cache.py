#!/usr/bin/env python3
"""
This script contains a class that implement FIFO Cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This is the FIFOCache
    """

    def __init__(self):
        """ The constructor for the FIFOCache Class. """
        self.items = []
        super().__init__()

    def put(self, key, item):
        """ This method assigns key and value to the dictionary. """
        if key is None:
            return
        if item is None:
            return
        if key not in self.items:
            self.items.insert(0, key)  # insert the key at the beginning
            self.cache_data[key] = item
        if len(self.items) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.items[-1]]
            print("DISCARD: {}".format(self.items.pop()))

    def get(self, key):
        """ """
        if key:
            value = self.cache_data.get(key)
            if value:
                return value
            return None
        return None
