"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = set()
        copies = {}
        if node is None: 
            return
        
        def depth(node): 
            nonlocal copies 

            if not node: 
                return None 

            if node in seen: 
                return
            
            seen.add(node)
            copy = Node(node.val)
            copies[node] = copy
            
            if not node.neighbors: 
                return
            
            for neighbor in node.neighbors: 
                depth(neighbor)
        
        depth(node)

        seen = set()
        def copy(node):
            nonlocal copies
            if not node: 
                return None

            if node in seen: 
                return
            
            if not node.neighbors: 
                copies[node].neighbors = []
                return

            copping = []
            for neighbor in node.neighbors: 
                copping.append(copies[neighbor])
            
            copies[node].neighbors = copping
            seen.add(node)

            for neighbor in node.neighbors: 
                copy(neighbor)
        
        copy(node)
        return copies[node]
            
            

            

        


        
            
        