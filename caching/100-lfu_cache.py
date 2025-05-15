#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
    - Caching system using LFU algorithm with LRU as tie-breaker
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequencies = {}  # key -> frequency count
        self.frequency_lists = {}  # frequency -> list of keys with that frequency
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        # Key already exists, update its value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        # Cache is full, need to evict an item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get keys with the minimum frequency
            lfu_keys = self.frequency_lists.get(self.min_frequency, [])
            
            # Apply LRU as tie-breaker by discarding the first item in the list
            # (least recently used among those with the same frequency)
            lfu_key = lfu_keys.pop(0)
            
            # Clean up if the list is now empty
            if not lfu_keys:
                del self.frequency_lists[self.min_frequency]
            
            # Remove the LFU item
            del self.cache_data[lfu_key]
            del self.frequencies[lfu_key]
            print("DISCARD: {}".format(lfu_key))

        # Add the new item to the cache
        self.cache_data[key] = item
        
        # Initialize frequency for new key
        self.frequencies[key] = 1
        
        # Add to frequency list for frequency 1
        if 1 not in self.frequency_lists:
            self.frequency_lists[1] = []
        self.frequency_lists[1].append(key)
        
        # Update minimum frequency to 1 since we just added a new item
        self.min_frequency = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Update frequency when item is accessed
        self._update_frequency(key)
        
        return self.cache_data.get(key)

    def _update_frequency(self, key):
        """ Helper method to update frequency of a key
        """
        # Get current frequency
        current_freq = self.frequencies[key]
        
        # Remove from current frequency list
        self.frequency_lists[current_freq].remove(key)
        
        # Clean up empty frequency lists
        if not self.frequency_lists[current_freq]:
            del self.frequency_lists[current_freq]
            # Update min frequency if needed
            if current_freq == self.min_frequency:
                self.min_frequency += 1
        
        # Increment frequency
        new_freq = current_freq + 1
        self.frequencies[key] = new_freq
        
        # Add to new frequency list
        if new_freq not in self.frequency_lists:
            self.frequency_lists[new_freq] = []
        self.frequency_lists[new_freq].append(key)