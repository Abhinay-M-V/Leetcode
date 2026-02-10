class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        abs=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                abs.append(i)
        return abs
        