class Solution(object):
    def combinationSum(self, candidates, target):
        output = []
        current = []

        def backtrack(start, remaining):
            if remaining == 0:
                output.append(current[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                backtrack(i, remaining - candidates[i])

                current.pop()

        backtrack(0, target)

        return output