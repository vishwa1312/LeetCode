class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat=[[0 for j in xrange(m+1)] for i in xrange(n+1)]
        r=n-1
        while(r>=0):
            c=m-1
            while (c>=0):

                if r==n-1 and c==m-1:
                    mat[r][c]=1
                else:
                    mat[r][c]=mat[r+1][c]+mat[r][c+1]
                c-=1
            r-=1

        return mat[0][0]
