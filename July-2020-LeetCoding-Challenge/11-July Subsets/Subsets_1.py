class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def helper(i, sset):
            if i==len(nums):
                return 
            helper(i+1, sset+[nums[i]])
            ans.add(tuple(sset+[nums[i]]))
            helper(i+1, sset)
            ans.add(tuple(sset))
        
        helper(0, [])
        
        return list(ans)+[]
