class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute force approach
        '''
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt > (n/2):
                return nums[i]
                '''
        # better { By using dictionary }
        '''
        map = {}
        for num in nums:
            map[num] = map.get(num,0)+1
        for key,value in map.items():
            if value > len(nums)//2:
                return key
        return -1 
        '''

        # optimal solution { Moore's Voting Algorithm }
        
        count = 0
        ele = None
        for num in nums:
            if count == 0:
                ele = num
            if num == ele:
                count += 1
            else:
                count -=1
        return ele
       
