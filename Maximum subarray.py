class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #Brute force
        # Time limit exceeds warning 
        # Time complexity O(n^3) & Space complexity O(1)

        '''
        max_sum = float('-inf')
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                sum1=0
                for k in range(i,j+1):
                    sum1 += nums[k]
                max_sum = max(sum1,max_sum)
        return max_sum
        '''

        # Better [by removing one inner loop]
        # Time complexity O(n^2)
        '''
        max_sum = float('-inf')
        n=len(nums)
        for i in range(n):
            sum1=0
            for j in range(i,n):
                sum1 += nums[j]
                max_sum = max(sum1,max_sum)
        return max_sum
        '''
        # Optimal solution [ Kadane's Algorithm]

        cur_sum = 0
        max_sum = nums[0]
        for i in nums:
            cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
     