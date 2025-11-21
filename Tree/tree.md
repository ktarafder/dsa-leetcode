# Time & Space Complexities
The **time complexity** of tree problems is usually O(n) b/c each node is visited once and O(1) work is done at each node. If more than O(1) work is done at a node then the time complexity become O(n*k) for the k work done at each node. 

The **space complexity** of tree problems is O(n) in the worst case where the tree is a straight line. If a tree is "complete" (all nodes have 0 or 2 children at each lvl) then the time complexity is O(logn). 

# Traversals
We can traverse a tree either recursively or iteravely.

 **Important note for iterative traversal:** the visit order is opposite the insertion order e.g. if we insert left node first into the stack and then a right node, the right node is popped off the stack first so its processed before the left node

There are three types of tree traversals: preorder, inorder, and postorder.

## Preorder
Nodes are processed in: current, left, right

Logic is performed before the children (root processed first and then left or right child)

## Inorder
Nodes are processed in: left, current, right

Logic is performed in the middle of the children (left or right processed first and then the root)

## Postorder
Nodes are processed in: left, right, current

Logic is performed after the children (both left and right are processed first and then the root)