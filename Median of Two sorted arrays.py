class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        n=len(num)
        l=0
        r=n-1
        m=(l+r)//2
        if n%2==0:
            x=float(num[m]+num[m+1])/2
            return x
        else:
            return num[m]      