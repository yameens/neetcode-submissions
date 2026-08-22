class TreeNode:
    def __init__(self, val=0, left=None, right=None, blocked=False):
        self.val = val
        self.left = left
        self.right = right
        self.blocked = False

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## breath first search. if there is a right, then tag the left as blocked

        if root is None:
            return []

        result = []
        queue = deque([root])
        
        while queue: 
            length = len(queue)
            
            for i in range(length): 
                node = queue.popleft()
                if node: 
                    rightMost = node
                    if node.left: 
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if rightMost: 
                result.append(rightMost.val)
        
        return result
            
        
        ## right most of a level is going to be the appended. 

        ## basically the current length of the queue are all the neighbors
        ## keep resetting while there is a length
                
                    
        

            


