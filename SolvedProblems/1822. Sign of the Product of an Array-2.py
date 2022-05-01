class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 1
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                neg *= -1
        if neg==1:
            return 1 
        return -1
