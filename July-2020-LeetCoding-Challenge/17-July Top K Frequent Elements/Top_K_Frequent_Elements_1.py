class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        x = sorted(counts.items(), key= lambda x:x[1], reverse=True)
        cons =  x[0:k]
        add = []
        for x, y in cons:
            add.append(x)
        return add
