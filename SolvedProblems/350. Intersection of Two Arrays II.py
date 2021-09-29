class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        l=[]
        for i in c1:
            if i in c2:
                a = min(c1[i], c2[i])
                for j in range(0, a):
                    l.append(i)
        return l
      
