#!/usr/bin/env python3
"""
This script contins a simple cache implemented as a python Class.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This is a Basic Cache Implementationin Python.
    """

    def put(self, key, item):
        """
        This method assigns key and value to the dictionary
        """
        if key is None:
            return
        if item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        This method return the value of a key in a dictionary
        """
        if key:
            value = self.cache_data.get(key)
            if value:
                return value
            return None
        return None
