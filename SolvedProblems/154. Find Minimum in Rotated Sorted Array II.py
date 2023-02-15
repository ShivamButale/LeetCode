class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        r = len(num)-1
        ans = num[(l+r)//2]
        while l<=r:
            mid = (l+r)//2
            if num[mid] < ans:
                ans = num[mid]
            if num[mid] < num[r]:
                r=mid-1
            elif num[mid] > num[r]:
                l=mid+1
            else:
                r = r-1
        return ans
