#!/usr/bin/python3
"""basic fifo cache"""
BasicCache = __import__('base_caching').BaseCaching


class LRUCache(BasicCache):
    """Create a class BasicCache that inherits from
    BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        """Key: rank_num"""
        self.data_order = {}
        """Increases after appending item to the cache"""
        self.data_rank = 0
        self.lowest_rank = ['A', 10]

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key"""
        if key and item:
            if len(self.cache_data) >= BasicCache.MAX_ITEMS:
                """find the lowest rank and delete from cache"""
                key_list = self.data_order.keys()
                key_list = list(key_list)
                self.lowest_rank = [key_list[0], self.data_order[key_list[0]]]
                for a in self.data_order:
                    if self.data_order[a] < self.lowest_rank[1]:
                        self.lowest_rank = [a, self.data_order[a]]
                print("DISCARD: {}".format(self.lowest_rank[0]))
                del self.data_order[self.lowest_rank[0]]
                del self.cache_data[self.lowest_rank[0]]
            self.cache_data[key] = item
            self.data_order[key] = self.data_rank
            self.data_rank = self.data_rank + 1

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.data_order[key] = self.data_rank
        self.data_rank = self.data_rank + 1
        return self.cache_data.get(key)
