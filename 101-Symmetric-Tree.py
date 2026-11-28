# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_same(l, r):
            if (not l and not r):
                return True
            if ((l and not r) or (not l and r) or (l.val != r.val)):
                return False
            return is_same(l.left, r.right) and is_same(l.right, r.left)
        return is_same(root.left, root.right)