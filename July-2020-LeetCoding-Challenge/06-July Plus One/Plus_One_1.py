class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret_list = []
        if digits[0] == 0:
            return [1]
        sum = 0
        n = len(digits)  
        for j in range(n-1, -1, -1):
            val = digits[j]* ( 10**( n-1-j ) )
            sum += val
        sum = sum+1
        while(sum):
            dig = sum % 10
            ret_list.append(dig)
            sum = sum // 10
        ret_list.reverse()
        return ret_list
