# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node: TreeNode | None, path_sum: int, path: list[int]) -> int:

            if node is None:
                return
            
            path.append(node.val)
            path_sum += node.val

            if node.left is None and node.right is None and path_sum == targetSum:
                result.append(path.copy())
            
            dfs(node.left, path_sum, path)
            dfs(node.right, path_sum, path)
            path.pop()

        dfs(root, 0, [])
        return result
        