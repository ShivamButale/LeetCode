class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_set = set()
        longest_substring_length = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in s_set:
                s_set.add(s[right])
                longest_substring_length = max(
                    longest_substring_length, len(s_set))
                right += 1

            else:
                s_set.remove(s[left])
                left += 1

        return longest_substring_length
