# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        split_para = preorder[0]
        root = TreeNode(split_para)
        split_index = inorder.index(split_para)
        inorder_left = inorder[:split_index]
        inorder_right = inorder[split_index+1:]
        preorder_left = preorder[1:1 +len(inorder_left)]
        preorder_right = preorder[len(inorder_left) + 1:]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
