#!/usr/bin/python3
"""basic cache"""
BasicCache = __import__('base_caching').BaseCaching


class BasicCache(BasicCache):
    """Create a class BasicCache that inherits from
    BaseCaching and is a caching system"""
    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
