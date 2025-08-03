# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return
        max_num = max(nums)
        res = TreeNode(max_num)
        max_index = nums.index(max_num)
        left_tree = nums[:max_index]
        right_tree = nums[max_index+1:]
        res.left = self.constructMaximumBinaryTree(left_tree)
        res.right = self.constructMaximumBinaryTree(right_tree)
        return res

        