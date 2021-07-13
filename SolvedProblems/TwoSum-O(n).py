class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Use dictionary 
        dictionary = {value:key for key,value in enumerate(nums)}
        #Travel through array 
        for i in range(0, len(nums)):
            req_num = target - nums[i]
            try:
                index = dictionary[req_num]
                if index==i or index==None:
                    continue
                return [i, index]
            except:
                continue
            
