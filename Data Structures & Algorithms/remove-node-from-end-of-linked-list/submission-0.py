# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        prev = None
        curr = head
        while curr:
            l += 1
            curr = curr.next
        nfromstart = l-n
        curr = head
        for i in range(nfromstart):
            prev = curr
            curr = curr.next
        if prev is None:
            return head.next
        prev.next = curr.next
        return head