class Solution(object):
    def subarraysDivByK(self, nums, k):
        total = 0
        count = 0
        seen = {0: 1}

        for num in nums:
            total += num
            remainder = total % k

            count += seen.get(remainder, 0)
            seen[remainder] = seen.get(remainder, 0) + 1

        return count