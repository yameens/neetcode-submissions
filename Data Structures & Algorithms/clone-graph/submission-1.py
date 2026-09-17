"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ## number indicates which one it is connected to :)
        from collections import deque

        visited = set()
        deep = {}

        if not node: 
            return None

        queue = deque()
        queue.append(node)
        visited.add(node)
        original = node

        while queue: 
            node = queue.popleft()
            visited.add(node)
            copy = Node()

            for neighbor in node.neighbors: 
                if neighbor not in visited: 
                    queue.append(neighbor)

            deep[node] = copy
        
        for node in deep.keys(): 
            copy = deep[node] 
            copy.val = node.val
            for neighbor in node.neighbors: 
                copy.neighbors.append(deep[neighbor])
        
        return deep[original]



        