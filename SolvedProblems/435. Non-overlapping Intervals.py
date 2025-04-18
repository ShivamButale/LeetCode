class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x:x[0])
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # No deleteion reqd 
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        
        return res 
