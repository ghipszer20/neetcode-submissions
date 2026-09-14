# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameTreeAux(p_curr, q_curr):
            if not (p_curr or q_curr):
                return True
            elif not (p_curr and q_curr):
                return False
            elif p_curr.val != q_curr.val:
                return False

            return isSameTreeAux(p_curr.left, q_curr.left) and isSameTreeAux(p_curr.right, q_curr.right)
            
        return isSameTreeAux(p, q)
        