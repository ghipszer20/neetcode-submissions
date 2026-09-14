# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    ## HashSet approach: O(n) time, O(n) space
    def hasCycle(self, head: Optional[ListNode]):
        seen, curr = set(), head

        while curr:
            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next

        return False


    ## fast/slow pointer approach: O(n) time, O(1) space
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     first, second = head, head

    #     while first and first.next:
    #         first = first.next.next
    #         second = second.next

    #         if first == second:
    #             return True

    #     return False


        