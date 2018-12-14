class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        i = 0
        j = 0
        ans = 0
        d={}
        n=len(s)
        while i<n and j<n :
            if s[j] in d:
                i=max(i,d[s[j]]+1)
            d[s[j]]=j
            ans=max(ans,j-i+1)
            j+=1

        return ans
        
