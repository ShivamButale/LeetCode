class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        total_min = minutes
        
        hour = hour%12
        hour_pos_base = hour * 5
        hour_pos_rem = minutes / 12
        total_hour = hour_pos_base + hour_pos_rem
        
        angle_1 = abs(total_min - total_hour) * 6
        angle_2 = 360 - angle_1
        
        return min(angle_1, angle_2)
        
        
