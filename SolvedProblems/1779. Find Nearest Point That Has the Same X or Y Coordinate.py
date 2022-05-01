class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:  
        final = []
        valid = []
        for i in range(0, len(points)):    
            curr = points[i]
            if(curr[0] == x or curr[1] == y):
                valid.append(curr)
                dist = abs(x - curr[0]) + abs(y - curr[1])
                final.append(dist)
        
        if(len(valid) == 0):
            return -1
            
        a = points.index(valid[final.index(min(final))])   
        return a 
