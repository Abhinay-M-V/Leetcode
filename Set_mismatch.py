class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        s=sum(nums)
        s2=sum(set(nums))
        d=s-s2
        m=(n*(n+1)//2-s2)
        return d,m
      
