class Solution:
    def getSum(self, a, b):
        mask = 0xffffffff

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= 0x7fffffff:
            return a
        else:
            return ~(a ^ mask)