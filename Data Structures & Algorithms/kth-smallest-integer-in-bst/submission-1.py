class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree_counter = 0
        result = None

        def inorder(node):
            nonlocal tree_counter, result
            if not node or result is not None:
                return
            inorder(node.left)
            tree_counter += 1
            if tree_counter == k:
                result = node.val
                return
            inorder(node.right)

        inorder(root)
        return result