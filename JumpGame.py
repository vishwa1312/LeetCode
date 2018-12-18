class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)-2
        z=len(nums)-1
        while(l>=0):
            if l+nums[l]>=z:
                z=l
            l-=1
        if z==0:
            return True
        else:
            return False
        
