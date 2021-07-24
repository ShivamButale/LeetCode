class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            return nums
        
        k = 0
        #Iterate through the array 
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
