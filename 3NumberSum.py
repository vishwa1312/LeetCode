class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l=len(nums)
        res=[]
        if l<3:
            return res
        for i in xrange(l):
            x=i+1
            z=l-1
            if not (i>0 and nums[i]==nums[i-1]) :
                while(x<z):
                    if nums[i]+nums[x]+nums[z]==0:
                        res.append([nums[i],nums[x],nums[z]])
                        while(x<z and nums[x]==nums[x+1]):
                            x+=1
                        while(x<z and nums[z]==nums[z-1]):
                            z-=1
                        x+=1
                        z-=1
                    else:
                        if nums[i]+nums[x]+nums[z] < 0:
                            x+=1
                        else:
                            z-=1
        return res
            
        
