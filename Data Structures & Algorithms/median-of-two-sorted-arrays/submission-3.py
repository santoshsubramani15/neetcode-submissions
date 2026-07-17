class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=nums1+nums2
        x.sort()
        if len(x)%2!=0:
            a=(len(x)+1)//2
            return x[a-1]
        else:
            a=len(x)//2
            p=x[(a-1)]
            q=x[a]
            r=p+q
            s=r/2
            return s