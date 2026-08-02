# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## re ordering the list
        ## 0 (length - 1) 1 (length - 2) 2 (length - 3)

        ## have two pointers
        ## stop when they converge

        arr = []
        curr = head 
        while curr: 
            arr.append(curr)
            curr = curr.next
        
        l, r = 0, len(arr) - 1
        
        while l < r: 
            arr[l].next = arr[r]
            l += 1
            arr[r].next = arr[l]
            r -= 1

            if r <= l: 
                arr[l].next = None