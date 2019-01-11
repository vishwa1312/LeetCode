# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sym(self,lft,rgt):
        if not lft and not rgt:
            return True
        if lft and rgt and lft.val==rgt.val:
            return (self.sym(lft.left,rgt.right) and self.sym(lft.right,rgt.left))
        else:
            return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.sym(root.left,root.right)
        else:
            return True
        
