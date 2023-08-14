#!/usr/bin/env python3
"""
This script contains a class that implement MRU Cache
which discards the most recently used (MRU) item
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ This is the MRUCache implementation Class. """

    def __init__(self):
        """ The constructor for the MRUCache Class. """
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
            if len(self.items) > BaseCaching.MAX_ITEMS:
                remove = self.items.pop(-2)
                del self.cache_data[remove]
                print("DISCARD: {}".format(remove))

    def get(self, key):
        """ This method return the value of a key in a dictionary. """
        if key:
            if key in self.items:
                self.items.remove(key)
                self.items.append(key)  # Move to the most recently used
                return self.cache_data[key]
            return None
        return None
