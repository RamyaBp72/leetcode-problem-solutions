# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, nxt, t = None, None, head
        while t:
            nxt = t.next
            while nxt and nxt.val == t.val:
                n = nxt.next
                nxt.next = None
                nxt = n
            t.next = nxt
            t = t.next
        return head