class Solution:
    def numPairsDivisibleBy60(self, time):
        seen = {}
        count = 0

        for num in time:
            remainder = num % 60
            needed = (60 - remainder) % 60

            if needed in seen:
                count += seen[needed]

            seen[remainder] = seen.get(remainder, 0) + 1

        return count