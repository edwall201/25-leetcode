# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.height(root) != -1:
            return True
        else: return False
    def height(self, root:TreeNode) -> int:
        if not root: return 0
        if (leftHeight := self.height(root.left)) == -1:
            return - 1
        if (rightHeight := self.height(root.right)) == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1: return -1
        else: return 1 + max(leftHeight, rightHeight)


            
        
        