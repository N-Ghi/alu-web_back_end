#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - Caching system using FIFO algorithm
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            # No need to update queue for existing keys in FIFO
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)