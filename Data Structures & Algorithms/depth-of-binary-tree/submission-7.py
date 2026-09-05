# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Stack DFS:
    def maxDepth(self, root):
        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            temp = stack.pop()
            node, depth = temp[0], temp[1]

            if not node:
                continue

            if depth > maxDepth: 
                maxDepth = depth
            
            
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
        
        return maxDepth
            






    # Queue BFS:
    # def maxDepth(self, root):
    #     if not root:
    #         return 0

    #     depth = 0
    #     q = deque([root])
        
    #     while q:
    #         depth += 1

    #         for i in range(len(q)):
    #             temp = q.popleft()

    #             if temp.left:
    #                 q.append(temp.left)

    #             if temp.right:
    #                 q.append(temp.right)
        
    #     return depth
                

            




    # Recursive method: O(n) time, O(n) space 
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: 
    #         return 0
       
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        