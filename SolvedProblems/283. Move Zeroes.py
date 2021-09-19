class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        l = len(nums)
        i=0
        while i<l:
            if(nums[i] == 0):
                del nums[i]
                l -= 1
                k+=1
            else:
                i+=1
        for i in range(0, k):
            nums.append(0)
