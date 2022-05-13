class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True 
        
        first = coordinates[0]
        second = coordinates[1]
        
        x_diff = second[0] - first[0]
        
        y_diff = second[1] - first[1]
        if y_diff == 0:
            y_const = y_diff
        else:
            y_const = None
            ratio = x_diff / y_diff
        
        for i in range(2, len(coordinates)):
            curr = coordinates[i]
            prev = coordinates[i-1]
                
            x1 = curr[0] - prev[0] 
            y1 = curr[1] - prev[1]
            
            if y1 ==0:
                if y_const is None:
                    return False
            else:
                if y_const is not None:
                    return False
                else:  
                    curr_ratio = x1 / y1 

                    if curr_ratio != ratio:
                        return False

        return True
            
