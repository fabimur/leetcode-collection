from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            nivel = []
            for _ in range(len(q)):
                node = q.popleft()
                nivel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(nivel)

        return res