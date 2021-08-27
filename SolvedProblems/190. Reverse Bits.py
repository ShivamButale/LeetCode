class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        curr_shift = 32
        
        ### basic idea:
        # At every iteration remove last digit and move it to the correct position
        
        while n:
            
            curr_digit = n & 1  ## extract last digit 
            curr_shift -= 1     
            
            curr = curr_digit << curr_shift ## moving the extracted digit to the correct location
            reverse = reverse | curr        ## adding the result to the reverse number we are generating 
            
            n = n >> 1         ## right shift by 1 as the last digit is processed
        
        
        return reverse
