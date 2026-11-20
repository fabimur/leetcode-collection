# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if node is None:
                result.append("null")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)
                
            

        dfs(root)
        return result

        

    def deserialize(self, data):
        values = iter(data.split(","))

        def dfs():
            value = next(values)

            if value == "null":
                return None

            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))