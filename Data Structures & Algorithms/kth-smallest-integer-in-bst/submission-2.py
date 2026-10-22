# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.collector(root,[],k)
        return res[-1]
    def collector(self,root,coll,k):
        if root is None:
            return coll
        if len(coll) == k:
            return coll
        self.collector(root.left,coll,k)
        if len(coll) == k:
            return coll
        coll.append(root.val)
        self.collector(root.right,coll,k)
        return coll