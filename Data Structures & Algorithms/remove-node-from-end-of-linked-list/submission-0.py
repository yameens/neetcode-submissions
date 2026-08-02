# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ## nth node. requires weaving'

        curr = head 
        length = 0
        while curr: 
            length += 1
            curr = curr.next

        count = 0
        curr = head
        previous = None
        
        while curr: 
            nexts = curr.next
            if count == (length - n): 
                if previous: 
                    previous.next = nexts
                else: 
                    head = nexts

                curr = None
                break

            previous = curr  
            curr = nexts
            count += 1
        
        return head

        