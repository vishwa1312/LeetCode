class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        c=0
        while(i<len(nums)):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                c+=1
                i+=1
            else:
                c=0
                i+=1
            if c>1:
                nums.pop(i)
                i-=1
        return len(nums)
