# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Queue BFS:
    def maxDepth(self, root):
        if not root:
            return 0

        depth = 0
        q = deque([root])
        
        while q:
            depth += 1

            for i in range(len(q)):
                temp = q.popleft()

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)
        
        return depth
                

            




    # Recursive method: O(n) time, O(n) space 
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: 
    #         return 0
       
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        