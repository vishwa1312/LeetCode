# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,ar):
        if root:
            self.inorder(root.left,ar)
            ar.append(root.val)
            self.inorder(root.right,ar)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ar=[]
        self.inorder(root,ar)
        return ar[k-1]
        
