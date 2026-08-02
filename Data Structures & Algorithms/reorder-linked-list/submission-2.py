# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []

        while curr: 
            arr.append(curr)
            curr = curr.next
        
        l, r = 0, len(arr) - 1
        while l < r: 
            arr[l].next = arr[r]
            l += 1
            arr[r].next = arr[l]
            r -= 1

            if l >= r: 
                arr[l].next = None
        



        