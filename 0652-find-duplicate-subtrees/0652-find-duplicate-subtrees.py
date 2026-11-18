# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode]:
        counts = defaultdict(int)
        result = []

        def dfs(node: TreeNode | None) -> str:
            if node is None:
                return "#"

            left = dfs(node.left)
            right = dfs(node.right)
            key = f"{node.val},{left},{right}" 

            counts[key] += 1
            if counts[key] == 2:
                result.append(node)

            return key

        dfs(root)
        return result