# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    mx=-999999
    def maxPathSum1(self, root):
        
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            a=self.maxPathSum1(root.left)
            b=self.maxPathSum1(root.right)
            c=root.val
            sum=max(c,a+c,b+c)
            self.mx = max(sum,self.mx,a+b+c)
            return sum
    def maxPathSum(self, root):
        
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSum1(root)
        return self.mx
