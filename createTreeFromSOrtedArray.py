class Solution(object):
    
    def sortedArrayToBST(self, arr):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not arr: 
            return None
  
        # find middle 
        mid = (len(arr)) / 2

        # make the middle element the root 
        root = TreeNode(arr[mid]) 

        # left subtree of root has all 
        # values <arr[mid] 
        root.left = self.sortedArrayToBST(arr[:mid]) 

        # right subtree of root has all  
        # values >arr[mid] 
        root.right = self.sortedArrayToBST(arr[mid+1:]) 
        return root 
            
