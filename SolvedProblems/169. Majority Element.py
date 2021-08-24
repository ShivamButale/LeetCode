class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicti = defaultdict(int)
        for i in nums:
            dicti[i] += 1
        x = sorted(dicti.items(), key = lambda k:k[1], reverse=True)
        return x[0][0]
