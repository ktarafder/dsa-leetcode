class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

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

# Preorder
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
    return

print("Preorder traversal:")
preorder(root) # Expected output: 1, 2, 4, 5, 3, 6

# Inorder traversal
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
    return

print("Inorder traversal:")
inorder(root) # Expected output: 4, 2, 5, 1, 3, 6

# Postorder traversal
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
    return

print("Postorder traversal:")
postorder(root) # Expected output: 4, 5, 2, 6, 3, 1