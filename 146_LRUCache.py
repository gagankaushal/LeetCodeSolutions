from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.lrudict = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.lrudict:
            ######least....most###
            self.lrudict.move_to_end(key)
            return self.lrudict[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lrudict:
            self.lrudict.move_to_end(key)
        self.lrudict[key] = value
        if len(self.lrudict)>self.capacity:
            self.lrudict.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
