class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        output = []
        current = []

        def backtrack(start, remaining):
            if remaining == 0:
                output.append(current[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                current.pop()

        backtrack(0, target)
        return output