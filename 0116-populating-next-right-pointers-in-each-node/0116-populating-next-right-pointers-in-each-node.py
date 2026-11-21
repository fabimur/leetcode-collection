"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: Node | None) -> Node | None:
        def dfs(node: Node | None, next_node: Node | None) -> None:
            if node is None:
                return None

            node.next = next_node

            if node.left is None:
                return None

            dfs(node.left, node.right)
            dfs(node.right, next_node.left if next_node is not None else None)

        dfs(root, None)
        return root