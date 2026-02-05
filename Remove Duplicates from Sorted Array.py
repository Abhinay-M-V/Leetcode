class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count=0
        # n=len(nums)
        # for num in nums:
        #     if nums.count>1:
        n=set(nums)
        nums[:]=sorted(n)
        return len(nums) 