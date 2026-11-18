# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        next_node = None

        def dfs(node: TreeNode | None) -> None:
            nonlocal next_node

            if node is None:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = next_node
            node.left = None
            next_node = node

        dfs(root)