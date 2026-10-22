
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            node = TreeNode(root_val)
            mid = inorder_map[root_val]

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(inorder) - 1)
