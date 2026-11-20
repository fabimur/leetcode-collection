# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        counts = Counter()

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            
            counts[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        max_freq = max(counts.values(), default=0)
        return [val for val in counts if counts[val] == max_freq]
        