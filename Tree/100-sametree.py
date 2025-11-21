class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

# p = [1,2,3]
p_left = TreeNode(2, None, None)
p_right = TreeNode(3, None, None)
p = TreeNode(1, p_left, p_right)

# q = [1,2,3]
q_left = TreeNode(2, None, None)
q_right = TreeNode(3, None, None)
q = TreeNode(1, q_left, q_right)

sol = Solution()
print(sol.isSameTree(p, q))