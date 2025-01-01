# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root

root = TreeNode(1, TreeNode(0), TreeNode(2))
low, high = 1, 2
sol = Solution()
def print_tree(node):
    if not node:
        return "null"
    return f"{node.val}, {print_tree(node.left)}, {print_tree(node.right)}"

trimmed_tree = sol.trimBST(root, low, high)
print(print_tree(trimmed_tree)) 