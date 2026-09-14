# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first, second = head, head

        while first and first.next:
            first = first.next.next
            second = second.next

            if first == second:
                return True

        return False


        