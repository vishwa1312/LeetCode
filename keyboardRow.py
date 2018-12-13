class Solution(object):
    def check(self,keys,c):
        for i in xrange(len(keys)):
            if c in keys[i]:
                return i
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        res=[]
        keys=["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in words:
            x=self.check(keys,i[0].lower())
            
            p=1
            for z in i[1:]:
                if self.check(keys,z.lower())==x:
                    p+=1
                else:
                    break
            
            if p==len(i):
                res.append(i)
        return res
                 
