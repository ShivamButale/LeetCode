class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
       
        if len(nums)==1:
            return 1
       
        k = 1
        
        #Iterate over array 
        i = 1
    
        while i<len(nums):
            if nums[i] < nums[i-1]:
                break
            if nums[i]==nums[i-1]:
                x = nums.pop(i)
                x = -101
                nums.append(x)
            else:
                k += 1
                i+=1
              
      
        return k
