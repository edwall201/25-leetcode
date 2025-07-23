"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        while queue:
            level = len(queue)
            temp = []
            for _ in range(level):
                node = queue.popleft()
                temp.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(temp)
        return res
            
            