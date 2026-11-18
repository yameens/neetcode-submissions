# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ## negative infinity to infinity, pass on the new bounds with each iteration
        def helper(minimum, maximum, curr): 
            if not curr: 
                return True

            if not (minimum < curr.val < maximum): 
                return False
            
            return (helper(minimum, curr.val, curr.left) and helper(curr.val, maximum, curr.right))
        
        return helper(float("-inf"), float("inf"), root)