#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
    - Caching system using LRU algorithm
    """

    def __init__(self):
        """ Initialize LRUCache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is None or item is None:
            return

        # If key exists, update its position in usage order
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
            
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Update usage order when an item is accessed
        self.usage_order.remove(key)
        self.usage_order.append(key)
        
        return self.cache_data.get(key)