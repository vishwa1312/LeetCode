class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        if n==2:
            return '11'
        s='11'
        n=n-2
        while n>0:
            print s
            cnt=1
            tmp=''
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    cnt+=1
                else:
                    tmp+=str(cnt)+s[i-1]
                    cnt=1
            tmp+=str(cnt)+s[i]
            s=tmp
            n-=1
        return s
