def maxArea(a):
    """
    :type height: List[int]
    :rtype: int
    """
     
    n=len(a)
    i,j=0,n-1
    res=0
    while(i<j):
        if a[i]<a[j]:
            r=(j-i)*a[i]
            if r>res:
                res=r
            i+=1
        else:
            r=(j-i)*a[j]
            if r>res:
                res=r
            j-=1
    return res

a = [1, 5, 4, 3] 
b = [3, 1, 2, 4, 5] 
c = [1,8,6,2,5,4,8,3,7] 
print(maxArea(a)) 
print(maxArea(b))
print(maxArea(c))
