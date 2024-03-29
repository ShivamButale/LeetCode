class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)

        if nums[0] >= target:
            return 0
        
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        
        return 0
