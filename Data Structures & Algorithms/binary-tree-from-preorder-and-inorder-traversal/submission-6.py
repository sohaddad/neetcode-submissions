# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)
        
        def next_node(left, right):
            if left > right:
                return None
            
            val = next(pre_iter)
            root = TreeNode(val)
            mid = inorder_idx[val]
            
            root.left = next_node(left, mid - 1)
            root.right = next_node(mid + 1, right)

            return root
        
        return next_node(0, len(inorder) - 1)