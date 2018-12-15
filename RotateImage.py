class Solution(object):
    def rotate(self, a):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r=len(a)
        c=r

        print a

        for i in xrange(r):
            for j in xrange(c):
                a[i][j],a[j][i]=a[j][i],a[i][j]
                if i==j:
                    break
        n=c/2
        k=0
        l=r-1
        while(k<n):
            for i in xrange(r):
                a[i][k],a[i][l]=a[i][l],a[i][k]
            k+=1
            l-=1
