class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(node, curr):
            if not node: return False

            if not node.left and not node.right:
                if node.val + curr == targetSum: return True
            
            curr += node.val
            return dfs(node.left, curr) or dfs(node.right, curr)
        
        return dfs(root,0)

def tree():
    # Test tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
    #           5
    #          / \
    #         4   8
    #        /   / \
    #       11  13  4
    #      / \       \
    #     7   2       1

    node7 = TreeNode(7, None, None)
    node2 = TreeNode(2, None, None)
    node1 = TreeNode(1, None, None)
    node11 = TreeNode(11, node7, node2)
    node13 = TreeNode(13, None, None)
    node4_right = TreeNode(4, None, node1)
    node4_left = TreeNode(4, node11, None)
    node8 = TreeNode(8, node13, node4_right)
    root = TreeNode(5, node4_left, node8)
    return root

# Test
solution = Solution()
root = tree()
print(solution.hasPathSum(root, 22))  # Should return True (5->4->11->2)

# Iterative
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        stack = [(root, 0)]
        while stack:
            node, curr = stack.pop()
            if not node.left and not node.right:
                if node.val + curr == targetSum:
                    return True
            if node.left:
                stack.append((node.left, curr+node.val))
            if node.right:
                stack.append((node.right, curr+node.val))
        return False
    
sol = Solution()
print(sol.hasPathSum(root, 22))