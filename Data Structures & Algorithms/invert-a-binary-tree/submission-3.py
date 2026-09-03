# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion with Auxiliary function:
    def invertTree(self, root):
        def invertTreeAux(curr):
            if curr == None:
                return 
            
            invertTreeAux(curr.left)
            invertTreeAux(curr.right)

            curr.left, curr.right = curr.right, curr.left

        invertTreeAux(root)

        return root
    

    # One-function recursion:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if root == None:
    #         return
        
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)

    #     root.left, root.right = root.right, root.left

    #     return root
        
        