# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        while queue:
            max_val = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(node.val, max_val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(max_val)
        return res        
        