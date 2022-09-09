# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 1
        while count < n:
            current = current.next
            count += 1
        start = head
        prev = head
        while current.next:
            prev = start
            count += 1
            current = current.next
            start = start.next
        if count == n:
            return head.next
        prev.next = start.next
        start.next = None
        return head
        
        
        