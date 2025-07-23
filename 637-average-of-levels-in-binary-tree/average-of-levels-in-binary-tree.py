# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        queue = collections.deque([root])
        ans = []
        while queue:
            level = len(queue)
            sum = 0
            for _ in range(level):
                node = queue.popleft()
                sum += node.val
                if node.left: queue.append(node.left) 
                if node.right:queue.append(node.right)
            ans.append(sum/level)
        return ans