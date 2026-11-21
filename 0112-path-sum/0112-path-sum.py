# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node: TreeNode | None, path_sum: int) -> bool:
            if node is None:
                return False


            path_sum += node.val

            if node.left is None and node.right is None and  path_sum == targetSum:
                return True
            
            return dfs(node.left, path_sum) or dfs(node.right, path_sum)

        return dfs(root, 0)
        