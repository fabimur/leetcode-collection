class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0  # (altura, diámetro)
            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)
            return 1 + max(lh, rh), max(ld, rd, lh + rh)

        return dfs(root)[1]