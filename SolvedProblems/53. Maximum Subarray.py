class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return None
        g_sum = float('-inf')
    
        max_arr = []
    
        max_arr.append(nums[0])
        g_sum = max_arr[0] 
        for i in range(1, len(nums)):
            print("i = ", i)
            max_arr.append(max(nums[i], nums[i]+max_arr[i-1]))
            g_sum = max(g_sum, max_arr[i])
            print("Max_arr[i] = ", max_arr[i])
            print("MAX GLOBAL SUM = ", g_sum)
            
        return g_sum 
        
