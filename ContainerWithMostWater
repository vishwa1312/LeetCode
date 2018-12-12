import sys
class Solution(object):
    def maxArea(self, a):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n=len(a)
        i,j=0,n-1
        res=0
        while(i<j):
            if a[i]<a[j]:
                r=(j-i)*a[i]
                if r>res:
                    res=r
                i+=1
            else:
                r=(j-i)*a[j]
                if r>res:
                    res=r
                j-=1
        return res
