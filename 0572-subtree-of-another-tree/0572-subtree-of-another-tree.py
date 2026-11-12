# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(a, b):
            # If both are None return True
            if not a and not b:
                return True
            
            # If only one is None return False
            if not a or not b:
                return False

            # They are the same if both right subtrees and both left subrees are the same
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        # An empty tree is a subtree of every tree
        if not subRoot:
            return True

        # An empty tree has no subtees (except the empty one)
        if not root:
            return False

        # Call the aux function
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)