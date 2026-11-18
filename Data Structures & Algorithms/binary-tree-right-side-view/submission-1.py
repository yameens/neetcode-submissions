# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## breadth first search is a solution! just add the rightmost node per level :)

        queue = deque()
        queue.append(root) 
        levels = []
        

        while queue: 
            length = len(queue) 
            level = []

            for i in range(length): 
                curr = queue.popleft()
                if curr: 
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level: 
                levels.append(level)
        
        res = []
        for level in levels: 
            res.append(level[-1])
        
        return res


        
        