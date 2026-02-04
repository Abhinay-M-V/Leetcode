class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        Onums=[]
        Lnums=nums[0:n]
        Rnums=nums[n:2*n+1]
        for i in range(n):
            Onums.append(Lnums[i])
            Onums.append(Rnums[i])
        return Onums


        