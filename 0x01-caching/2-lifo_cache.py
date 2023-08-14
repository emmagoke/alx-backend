#!/usr/bin/env python3
"""
This script contains a class that implement LIFO Cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ This is the FIFOCache implementation Class. """

    def __init__(self):
        """ The constructor for the FIFOCache Class. """
        self.items = []
        super().__init__()

    def put(self, key, item):
        """ This method assigns key and value to the dictionary. """
        if key and item:
            if key not in self.items:
                self.items.append(key)
                self.cache_data[key] = item
            elif key in self.items:
                self.items.remove(key)
                self.items.append(key)
                self.cache_data[key] = item
            # print(self.items)
            if len(self.items) > BaseCaching.MAX_ITEMS:
                remove = self.items.pop(-2)  # last added item before the new
                del self.cache_data[remove]
                print("DISCARD: {}".format(remove))

    def get(self, key):
        """ This method return the value of a key in a dictionary. """
        if key:
            value = self.cache_data.get(key)
            if value:
                return value
            return None
        return None
