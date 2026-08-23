# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, maxValue, root: TreeNode) -> int:
        ## DFS, when the last root, return nothing
        ## track a list of values

        if root is None: 
            return 0
        
        if root.val >= maxValue:
            res = 1
        else:
            res = 0

        maxValue = max(maxValue, root.val)
        
        if root.left: 
            res += self.helper(maxValue, root.left) 
        if root.right:
            res += self.helper(maxValue, root.right)

        return res
    
        
    def goodNodes(self, root: TreeNode) -> int: 
        values = -100000000000
        return self.helper(values, root)
                
        