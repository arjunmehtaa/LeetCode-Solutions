# K is the number of sorted lists
# Time Complexity	: O(N*LOG(K))
# Space Complexity	: O(1)             NOT SURE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(merge(l1, l2))
            lists = mergedLists
        return lists[0]
                                
def merge(l1, l2):
    final = ListNode()
    head = final
    while l1 and l2:
        if l1.val < l2.val:
            final.next = l1
            l1 = l1.next
        else:
            final.next = l2
            l2 = l2.next
        final = final.next
    if l1:
        final.next = l1
    if l2:
        final.next = l2
    return head.next
                                   
                        
                                   
                                   
        