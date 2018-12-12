class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            prev=nums2[0]
            cur=nums2[0]
        elif not nums2:
            prev=nums1[0]
            cur=nums1[0]
        else:
            prev=min(nums1[0],nums2[0])
            cur=min(nums1[0],nums2[0])
        i,j=0,0
        
        l1=len(nums1)
        l2=len(nums2)
        n=l1+l2
        mid=n/2;
        iseven=True if n%2==0 else False
        cnt=0
        while (i<l1 and j<l2):
            if nums1[i]<nums2[j]:
                prev=cur
                cur=nums1[i]
                i+=1
            else:
                prev=cur
                cur=nums2[j]
                j+=1
            if cnt==mid:
                if iseven:
                    return (prev+cur)/float(2.0)
                else:
                    return cur
            cnt+=1
        if i>=l1:
            print prev
            print cur
            print j
            while(j<l2):
                prev=cur
                cur=nums2[j]
                j+=1
                if cnt==mid:
                    if iseven:
                        return (prev+cur)/float(2.0)
                    else:
                        return cur
                cnt+=1
        if j>=l2:
            while(i<l1):
                prev=cur
                cur=nums1[i]
                i+=1
                if cnt==mid:
                    if iseven:
                        return (prev+cur)/float(2.0)
                    else:
                        return cur
                cnt+=1

        
