class Solution:
    def goodNodes(self,root):
        def dfs(node, maxNode):
            if not node:
                return 0
            
            good = 1 if node.val >= maxNode else 0
            maxNode = max(maxNode, node.val)

            good += dfs(node.left, maxNode)
            good += dfs(node.right, maxNode)

            return good
        return dfs(root, root.val)