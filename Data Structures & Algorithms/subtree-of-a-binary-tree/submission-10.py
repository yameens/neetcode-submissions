# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(root, subRoot):
            if not root and not subRoot: 
                return True
            elif (root and not subRoot) or (not root and subRoot): 
                return False
            
            left, right = helper(root.left, subRoot.left), helper(root.right, subRoot.right)

            if root.val != subRoot.val: 
                return False
            
            return left and right
        
        queue = deque()
        queue.append(root)

        while queue: 
            root = queue.pop()
            if helper(root, subRoot):
                return True
            
            if root.left: 
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        
        return False
        