# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBSTHelper(root,-sys.maxsize,sys.maxsize)
    def validBSTHelper(self,root,low,high):
        if root is None:
            return True
        if low >= root.val or root.val >= high:
            return False
        return self.validBSTHelper(root.left,low,root.val) and self.validBSTHelper(root.right,root.val,high)
        
