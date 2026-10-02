# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque()

        if root:
            queue.append(root)
            
        while len(queue) > 0:
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            last = temp.pop()
            output.append(last)   

        return output