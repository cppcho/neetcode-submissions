# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
a -> b -> c -> d -> e

d -> e

1. d -> e
    r(e)
        newHead = none
        return e
    new head = e
    



"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        newHead = self.reverseList(head.next)
        if not newHead:
            return head

        if head.next:
            head.next.next = head
        head.next = None

        return newHead

        