# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # optional means returning potentially NONE
        # need a previous (set to none)
        # track your next 
        # track your current (update last)


        if head is None: 
            return None
        
        curr = head
        prev = None # previous is a new value. we are treating the current head as the former tail 

        while curr.next != None: # we are always accessing the next value. proper gaurdrail to prevent from accessing nothing

            nextNode = curr.next ## next value in the chain
            curr.next = prev ## set current behind, reversing the list
            prev = curr ## update previous value
            curr = nextNode
        
        ## we are missing the last swap. this is because we dont append curr.next on the last iteration

        curr.next = prev

        return curr


        