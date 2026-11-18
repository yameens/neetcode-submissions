# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        maximum = float("-inf")

        def helper(maximum, curr): 
            nonlocal total 

            if not curr: 
                return None
            
            ## pass the max in the previous path
            if curr.val >= maximum: 
                maximum = curr.val
                total += 1
            
            helper(maximum, curr.right)
            helper(maximum, curr.left)
        
        helper(maximum, root)
        return total
        