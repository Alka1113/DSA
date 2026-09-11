class Solution:
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            new_sets = []

            for subset in result:
                new_set = subset[:]
                new_set.append(num)
                new_sets.append(new_set)

            result.extend(new_sets)

        return result