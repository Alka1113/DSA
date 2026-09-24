class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Check sign
        sign = 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # Build the number directly
        result = 0

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result