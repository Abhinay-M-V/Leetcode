class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        n1=(n*(n+1))/2
        sum1=sum(nums)
        return n1-sum1