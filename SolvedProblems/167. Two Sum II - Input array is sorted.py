class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            try:
                x = numbers.index(target-numbers[i])
                if x!=i:
                    l = [i+1, x+1]
                    return sorted(l)
            except:
                pass
        
