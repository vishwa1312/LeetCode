class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        l=len(s)
        if len(s)<=numRows or numRows==1:
            return s
        res=[""]*numRows
        i,inc=0,1
        
        for c in s:
            res[i]+=c
            if i==0:
                inc=1
            if i==numRows-1:
                inc=-1
            i+=inc
        return ''.join(res)
        
