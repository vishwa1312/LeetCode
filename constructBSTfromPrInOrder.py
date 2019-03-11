class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root=TreeNode(preorder[0])
        idx=inorder.index(preorder[0])
        preorder.pop(0)
        root.left = self.buildTree(preorder,inorder[:idx])
        root.right = self.buildTree(preorder,inorder[idx+1:])
        return root
