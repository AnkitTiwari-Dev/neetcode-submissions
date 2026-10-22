# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root,-float('inf'),float('inf'))
    def validBST(self,root,low,high):
        if root is None:
            return True
        if low >= root.val or root.val >= high:
            return False
        return self.validBST(root.left,low,root.val) and self.validBST(root.right,root.val,high)