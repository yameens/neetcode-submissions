"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        ## need to make DEEP copies: Node(cur.value)
        ## the copy next need to me mapped to the COPIES, not the curr.next

        cur = head
        oldToCopy = {}
        while cur: 
            # make a hashmap of old nodes to copy. so it can be accessed later
            # make deep copies while passing through
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        ## pass two passes the copies with eachother. need to access the hash mapped
        cur = head
        while cur: 
            copy = oldToCopy[cur]
            if cur.next: 
                copy.next = oldToCopy[cur.next]
            if cur.random: 
                copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
        

            
        