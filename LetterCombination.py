class Solution(object):
    def generateCombinations(self,digits,dct):
        if len(digits)==0:
            return []
        if len(digits)==1:
            return dct[digits[0]]
        r=[]
        for i in dct[digits[0]]:
            for j in self.generateCombinations(digits[1:],dct):
                r.append(i+j)
        return r
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct={
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        return self.generateCombinations(digits,dct)
