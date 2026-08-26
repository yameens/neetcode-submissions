# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ## the nodes on the left must be limited by the right value
        ## the nodes on the right must be limited by the left value

        def helper(root, left, right):
            if root is None: 
                return True
            if not (left < root.val and root.val < right): 
                return False
            
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        
        return helper(root, -float('inf'), float('inf'))
            
        