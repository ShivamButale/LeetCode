class Solution:
    def helper(self, nums, sum, sol):
        dp = {}
        for index, value in enumerate(nums):
            if sum - value in dp:
                sol.add((value, sum-value, -sum))
            dp[value] = index
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        previous = float('inf')
        
        for index, val in enumerate(nums):
            if val == previous:
                #ignore
                continue
            self.helper(nums[index+1:], -val, sol)
            previous = val
        return sol
    
