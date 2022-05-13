class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = []
        n2 = len(nums2)
        
        for i in nums1:
            x = nums2.index(i)
            flag = 0
            for a in range(x, n2):
                if nums2[a] > i:
                    flag = 1
                    final.append(nums2[a])
                    break
                
            if flag==0:
                final.append(-1)
          
        return final 
