# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        curr, stack, miniDiff, prev = root, [], 10**5, -10**5
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            miniDiff = min(miniDiff, node.val - prev)
            prev = node.val
            curr = node.right
        return miniDiff