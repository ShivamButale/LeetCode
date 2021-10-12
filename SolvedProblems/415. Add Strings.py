class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        one = 0
        sum_num = []
        while idx1 >= 0 and idx2 >= 0:
            sum_digits = ord(num1[idx1]) - 48 + ord(num2[idx2]) - 48 + one
            sum_num.append(sum_digits % 10)
            one = sum_digits // 10
            idx1 -= 1
            idx2 -= 1

        while idx1 >= 0:
            sum_digits = ord(num1[idx1]) - 48 + one
            sum_num.append(sum_digits % 10)
            one = sum_digits // 10
            idx1 -= 1

        while idx2 >= 0:
            sum_digits = ord(num2[idx2]) - 48 + one
            sum_num.append(sum_digits % 10)
            one = sum_digits // 10
            idx2 -= 1

        if one:
            sum_num.append(1)
        return "".join(map(str, sum_num[::-1]))
