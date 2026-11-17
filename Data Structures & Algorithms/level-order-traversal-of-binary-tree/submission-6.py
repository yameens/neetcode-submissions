# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict

        if not root: 
            return []

        queue = deque()
        queue.append(root)
        
        level = {}
        level[root] = 1
        
        lists = defaultdict(list)
        lists[1].append(root.val)

        while queue: 
            curr = queue.popleft()
            currLevel = level[curr]
    
            if curr.left: 
                queue.append(curr.left)
                level[curr.left] = currLevel + 1
                lists[currLevel + 1].append(curr.left.val)

            if curr.right: 
                queue.append(curr.right)
                level[curr.right] = currLevel + 1
                lists[currLevel + 1].append(curr.right.val)

        result = []

        for item in lists: 
            result.append(lists[item])

        return result




