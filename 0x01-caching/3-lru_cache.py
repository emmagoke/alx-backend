#!/usr/bin/env python3
"""
This script contains a class that implement LRU Cache
which discards the least recently used(LRU) item
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ This is the LRUCache implementation Class. """

    def __init__(self):
        """ The constructor for the LRUCache Class. """
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
                remove = self.items.pop(0)
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
