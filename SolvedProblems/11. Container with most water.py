class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        if len(height) == 2:
            return min(height)
        max_area = 0
        i = 0 
        j = len(height) - 1

        while i!=j:
            horizontal = j - i 
            minimum = min(height[i], height[j])
            area = horizontal * minimum 
            max_area = max(area, max_area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area 
