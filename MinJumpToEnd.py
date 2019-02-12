class Solution(object):
    def jump(self, ar):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minJumpIdx=0
        res=[0]*len(ar)
        i=1
        while(i<len(ar) and i>minJumpIdx):
            if minJumpIdx+ar[minJumpIdx]>=i:
                res[i]=res[minJumpIdx]+1
                i+=1
            else:
                minJumpIdx+=1
        return res[-1]
        
