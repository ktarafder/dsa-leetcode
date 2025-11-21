'''
this code will sum all nodes in a tree
'''

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNodes(self, root):
        if not root:
            return 0
        left = self.sumNodes(root.left) 
        right = self.sumNodes(root.right)
        return root.val + left + right
    
    def sumNodes2(self, root):
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return node.val + left + right
        return dfs(root)

def tree():
    # Test tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    node4 = TreeNode(4, None, None)
    node5 = TreeNode(5, None, None)
    node6 = TreeNode(6, None, None)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, None, node6)
    root = TreeNode(1, node2, node3)
    return root

root = tree()
sol = Solution()
print(sol.sumNodes(root))
print(sol.sumNodes2(root))