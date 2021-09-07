class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ranger = {}
        ranger[0] = [nums[0]]
    
        curr = 0
        prev = 0
    
        for i in range(1, len(nums)):                   
            if nums[i] - nums[i-1] == 1:
                ranger[prev].append(nums[i])
            else:
                ranger[i] = []
                ranger[i].append(nums[i])
                prev = i 
                
        final = []
        for i in ranger.values():
            if len(i)==1:
                s = str(i[0])
            else:
                s = str(i[0])
                s += "->"
                s += str(i[-1])
            final.append(s)
            
        return final 
