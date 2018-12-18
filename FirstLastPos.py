class Solution(object):
    def binsearch(self,nums,target,i,j):
        if (i==j and nums[i]!=target) or i>j or j<i:
            return [-1,-1]
        mid=(i+j)/2
        if nums[mid]==target:
            k=mid
            l=mid
            
            while(k>=i or l<=j):
                flagk=0
                flagl=0
                if k>=i and nums[k]==target:
                    k-=1
                    flagk=1
                if l<=j and nums[l]==target:
                    l+=1
                    flagl=1
                if not flagk and not flagl:
                    break        
            return [k+1,l-1]
        elif nums[mid]>target:
            return self.binsearch(nums,target,i,mid-1)
        else:
            return self.binsearch(nums,target,mid+1,j)    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        return self.binsearch(nums,target,0,len(nums)-1)
        
