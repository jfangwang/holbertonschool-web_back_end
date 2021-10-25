#!/usr/bin/python3
"""basic fifo cache"""
BasicCache = __import__('base_caching').BaseCaching


class FIFOCache(BasicCache):
    """Create a class BasicCache that inherits from
    BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.data_order = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key"""
        if key and item:
            if len(self.cache_data) >= BasicCache.MAX_ITEMS:
                popped_key = self.data_order.pop(0)
                del self.cache_data[popped_key]
                print("DISCARD: {}".format(popped_key))
            self.cache_data[key] = item
            self.data_order.append(key)

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
