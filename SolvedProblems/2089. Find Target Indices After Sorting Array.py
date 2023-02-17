class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        op = set()

        while(lo <= hi):
            mid = (lo + hi)//2
            mid_e = nums[mid]
            
            if mid_e == target:
                op.add(mid)

                curr = mid-1
                while(curr >=0 and nums[curr] == target):
                    op.add(curr)
                    curr -= 1

                next_curr = mid + 1
                while (next_curr < len(nums) and nums[next_curr] == target):
                    op.add(next_curr)
                    next_curr += 1

                op = list(op)
                op.sort()
                return op

            elif mid_e < target:
                lo = mid + 1
            else:
                hi = mid - 1
