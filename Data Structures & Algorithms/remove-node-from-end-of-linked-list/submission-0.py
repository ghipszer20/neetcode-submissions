# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, total_nodes = head, 0

        while curr:
            curr = curr.next
            total_nodes += 1

        if total_nodes == n:
            head = head.next
            return head
        
        curr = head

        for _ in range(total_nodes - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head

        