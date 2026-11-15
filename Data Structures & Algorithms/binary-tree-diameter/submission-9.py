# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest = 0

        def depth(curr): 
            if not curr: 
                return 0

            right = depth(curr.right)
            left = depth(curr.left)

            self.largest = max(self.largest, right + left)
            return max(right, left) + 1
        
        depth(root)
        return self.largest


        