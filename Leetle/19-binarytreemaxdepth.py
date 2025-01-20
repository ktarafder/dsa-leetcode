'''
Write a function that finds the maximum depth of a binary tree. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. 
The tree is represented as an array of nodes in level-order traversal. None indicates empty nodes.

Example:
Input: [3,9,20,None,None,15,7]
Output: 3
'''

'''
Post-order (left, right, root) traversal 
'''

def solve(root):
    if root is None:
      return 0
    l = solve(root.left)
    r = solve(root.right)
    return max(l,r) + 1

# BFS level order traversal constructing tree 
#.   3
#  9   20
#.   15  7

def solve(root):
    # base case
    if not root:
      return 0
    # recursive step
    return max(solve(root.left), solve(root.right)) + 1