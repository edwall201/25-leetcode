# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = collections.deque([root])
        ans = 0
        while queue:
            level = len(queue)
            ans += 1
            for _ in range(level):
                node = queue.popleft()
                if not node.left and not node.right: return ans
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return ans
        