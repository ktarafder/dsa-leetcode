from collections import deque
from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

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

sol = Solution()
# Tree after insertion of 5
new_tree = sol.insertIntoBST(root, 5)

'''
Have not learned the below yet, but Leetcode uses BFS to verify the tree
In Leetcode it is fine to return just the root node, because I'm guessing they run BFS on the tree to verify it in the backend 
TODO: Learn BFS & Update the explanation
'''
# Function to print the tree in level-order (BFS) for verification
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

print(level_order_traversal(new_tree)) # Expected: [4,2,7,1,3,5]