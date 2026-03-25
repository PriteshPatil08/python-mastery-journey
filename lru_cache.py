# This program implements an LRU (least recently used) cache using OrderedDict to manage item ordering efficiently.
# It demonstrates core Python concepts like class design, state management, and dictionary-based data structures.
# It maintains recent usage by moving accessed items to the end and evicts least recently used when capacity is exceeded.
# You will learn how to design performant, real-world caching systems with O(1) operations.

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache : OrderedDict[int, int] = OrderedDict()


    def get(self, key: int) -> int:
        if key not in self.cache:
            return None
        
        self.cache.move_to_end(key = key, last = True)

        return self.cache[key]


    def put(self, key:int, value: int) -> None:
        self.cache[key] = value

        self.cache.move_to_end(key = key, last = True)
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


cache = LRUCache(5)
cache.put(6,6)
cache.put(9,9)
cache.put(4,4)
cache.put(1,1)
cache.put(7,7)
cache.get(6)
cache.put(3,3)

print(cache.cache) #(9,9) removed because (6,6) was accessed recently.