class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct={}
        for st in strs:
            t=hash(''.join(sorted(st)))
            if t in dct:
                dct[t].append(st)
            else:
                dct[t]=[st]
        return [dct[i] for i in dct]
