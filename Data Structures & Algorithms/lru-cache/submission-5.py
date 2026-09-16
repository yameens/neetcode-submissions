class LRUCache:

    def __init__(self, capacity: int):
        from collections import deque

        self.cache = {}
        self.capacity = capacity      

        self.recent = deque()  

    def get(self, key: int) -> int:
        if key not in self.cache.keys(): 
            return -1 
        
        ## update the index!
        index = self.recent.index(key)
        del self.recent[index]

        self.recent.append(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys(): 
            self.cache[key] = value
            index = self.recent.index(key)
            del self.recent[index]
            self.recent.append(key)
            
            return
            
        self.cache[key] = value
        self.recent.append(key)

        if len(self.recent) > self.capacity: 
            old = self.recent.popleft()
            del self.cache[old]
        
        

        

        
        
