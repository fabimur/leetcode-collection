# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node):
            
            if node is None:
                return 0

            # Check if left subtree is balanced
            left = balanced(node.left)
            # If left subtree isnt balanced then this one either
            if left == -1:
                return -1
            
            # Check if right subtree is balanced
            right = balanced(node.right)
            # If right subtree isnt balanced then this one either
            if right == -1:
                return -1

            # If left height and right height differ by more than one then this tree isnt balanced
            if abs(left - right) > 1:
                return -1
            
            # Return height of the tree
            return 1 + max(left, right)

        return balanced(root) != -1