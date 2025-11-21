class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1

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
print(sol.maxDepth(root))

# Iterative
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0 
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return ans
    
sol = Solution()
print(sol.maxDepth(root))