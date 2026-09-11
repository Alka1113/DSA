class Solution:
    def findPairs(self, nums, k):
        map = {}
        count = 0

        for i in nums:
            map[i] = map.get(i, 0) + 1

        for a in map:
            if k != 0:
                b = a + k
                if b in map:
                    count += 1
            else:
                if map[a] >= 2:
                    count += 1

        return count