class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        op = []
        lo = 0 
        hi = len(nums)-1

        s_pos = -1
        e_pos = -1

        while lo<=hi:
            mid = (lo + hi)//2
            mid_e = nums[mid]

            if mid_e < target:
                lo = mid + 1
            elif mid_e > target:
                hi = mid - 1
            elif mid_e == target:
                # Current element is target 
                s_pos = mid
                e_pos = mid

                #update s_pos
                curr = mid
                while(curr >= 1 and nums[curr-1]==target):
                    s_pos = curr - 1
                    curr = s_pos
                    
                #update e_pos
                n_curr = mid
                while(n_curr+1 < len(nums) and nums[n_curr+1]==target):
                    e_pos = n_curr + 1
                    n_curr = e_pos
                
                break
        
        op.append(s_pos)
        op.append(e_pos)
        return op
        
