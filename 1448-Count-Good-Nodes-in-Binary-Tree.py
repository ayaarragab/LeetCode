# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recurse(root, maxSoFar):
            if not root:
                return 0
            add_or_not = root.val >= maxSoFar
            l = recurse(root.left, max(maxSoFar, root.val))
            r = recurse(root.right, max(maxSoFar, root.val))
            return r + l + (1 if (add_or_not) else 0)
        return recurse(root, root.val)