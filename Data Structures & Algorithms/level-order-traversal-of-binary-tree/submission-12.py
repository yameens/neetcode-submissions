# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## the length of the queue is a good indicator of how many are at that level. 
        ## as we pop, add to the list! let us do this thing. 

        queue = deque()
        res = []
        queue.append(root) 

        while queue: 
            length = len(queue) 
            level = []
            
            for i in range(length): 
                node = queue.popleft()

                if node: 
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level: 
                    res.append(level)
        
        return res
        