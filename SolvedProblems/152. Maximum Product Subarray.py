class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_val = 1
        max_val = 1

        # Lets track the min and max at each subarray. This will be used for the next number 
        for n in nums:
            if n == 0:
                min_val = 1
                max_val = 1
                continue 
            
            temp = max_val
            max_val = max(n*max_val, n*min_val, n)
            min_val = min(n*temp, n*min_val, n)
            res = max(res, max_val)

        return res 
