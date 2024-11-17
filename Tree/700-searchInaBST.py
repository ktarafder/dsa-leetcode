from typing import Optional

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return [root.val, root.left if not root.left else root.left.val, root.right.val if root.right else None] # I'm surprised I was able to figure this out ngl

# Test cases
# Example 1
#      4
#     / \
#    2   7
#   / \   
#  1   3  
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
val = 2
sol = Solution()
print(sol.searchBST(root, val)) # Expected: [2,1,3]

# Time and space complexity:
# Time complexity: O(h) where h is the height of the tree
# Space complexity: O(h) where h is the height of the tree
# This is because we're doing a depth-first search traversal of the tree. The space complexity is due to the recursive calls. The time complexity is due to the fact that we're traversing the tree.