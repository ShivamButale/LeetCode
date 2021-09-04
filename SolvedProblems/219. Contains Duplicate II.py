class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicti = {}
        for i, num in enumerate(nums):
            if dicti.get(num) and i+1-dicti[num] <= k:
                return True 
            dicti[num] = i+1
        return False
