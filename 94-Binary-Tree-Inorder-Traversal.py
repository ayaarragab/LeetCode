# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def get_list(root, l):
            if not root:
                return
            get_list(root.left, l)
            l.append(root.val)
            get_list(root.right, l)
        l = []
        get_list(root, l)
        return l