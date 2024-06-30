class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max(candies):
                l.append(True)
            else:
                l.append(False)
        return l
