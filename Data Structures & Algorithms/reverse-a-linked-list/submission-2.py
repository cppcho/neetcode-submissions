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
        if head.next is None:
            return head
            
        prev = None
        curr = head
        while curr.next:
            curr.next.next = curr
            curr.next = prev
            prev = curr
            curr = curr.next
        
        return curr


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

        