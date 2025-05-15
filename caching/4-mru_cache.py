#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
    - Caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
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
                mru_key = self.usage_order.pop()  # Most Recently Used (last item)
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            
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