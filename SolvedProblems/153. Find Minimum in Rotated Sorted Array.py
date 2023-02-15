class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while(lo <= hi):
            mid = (lo + hi) // 2
            mid_e = nums[mid]

            if (mid >= 1) and (mid_e < nums[mid-1]):
                return mid_e
            elif mid_e > nums[-1]:
                lo = mid + 1
            else:
                hi = mid - 1

        return nums[0]
