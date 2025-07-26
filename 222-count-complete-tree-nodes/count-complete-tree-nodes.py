# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNum(self, root):
        if not root: return 0
        left = self.getNum(root.left)
        right = self.getNum(root.right)
        return left + right + 1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.getNum(root)

        
        