class Solution:
    def mySqrt(self, x: int) -> int:
        if x<1:
            return x
        if x<4:
            return 1
        if x<9:
            return 2
        if x<16:
            return 3 
        
        left = 0
        right = x//3
        
        while(left<=right):
            mid = left + (right-left)//2
            if mid*mid == x:
                return mid
            
            if 0 < x-mid*mid < 2*mid+1:
                return mid
            
            if mid*mid < x:
                left = mid+1
            else:
                right = mid-1
                
                
