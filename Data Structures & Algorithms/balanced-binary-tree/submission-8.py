# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## worry about the height
        balanced = True 

        def dfs(curr): 
            nonlocal balanced
            
            if not curr: 
                return 0

            right = dfs(curr.right)
            left = dfs(curr.left)

            if abs(right - left) > 1: 
                balanced = False
            
            return max(right, left) + 1
        
        dfs(root)
        return balanced
        