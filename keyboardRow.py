class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dct={}
        keys=["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in xrange(len(keys)):
            for z in keys[i]:
                dct[z]=i
        res=[]
        for i in words:
            x=dct[i[0].lower()]
            p=1
            for z in i[1:]:
                if dct[z.lower()]==x:
                    p+=1
                else:
                    break
            
            if p==len(i):
                res.append(i)
        return res
