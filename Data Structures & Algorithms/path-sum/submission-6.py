# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # start at the root

        def dfs(root, count):

            # if the end reutn 0
            if not root:
                return False

            count += root.val

            # checking that it is a leaf node
            if not root.left and not root.right:
                return count == targetSum

            return dfs(root.left, count) or dfs(root.right, count)

        return dfs(root, 0)
