class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return sum(nums)

        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
        
            if (curr + curr_sum < curr):  
                curr_sum = curr 
            else: 
                curr_sum = curr_sum + curr
            max_sum = max(max_sum, curr_sum)  

        return max_sum
