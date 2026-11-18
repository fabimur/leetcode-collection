# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        moves = 0

        def dfs(node: TreeNode | None) -> int:
            nonlocal moves

            if node is None:
                return 0
            if node.right is None and node.left is None:
                return node.val - 1

            left = dfs(node.left)
            right = dfs(node.right)

            moves += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return moves