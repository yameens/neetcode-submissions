class Node: 
    def __init__(self, key=0, val=0): ## equals 0 simply means that is the default
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.right = self.tail
        self.tail.left = self.head

        ## dummy nodes to take care of edge cases
        ## dummy nodes are so goated and remove most of my stress anyway
    
    def remove(self, node: Node) -> None: 
        prv, nxt = node.left, node.right 
        prv.right = nxt
        nxt.left = prv

    def add(self, node: Node) -> None: 
        prev = self.tail.left
        prev.right = node
        
        node.left = prev
        node.right = self.tail

        self.tail.left = node  

    def get(self, key: int) -> int:
        if key not in self.cache.keys(): 
            return -1
        
        node = self.cache[key]
        ## accessing code puts it back in the front of the list
        ## must do it in o(1) by accessing the node immedietely

        self.remove(node)
        self.add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys(): 
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.add(node)

            return 
        
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity: 
            lru = self.head.right
            self.remove(lru) 
            ## don't forget to delete it from the map ! 

            del self.cache[lru.key]
        

