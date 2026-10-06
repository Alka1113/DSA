class Solution(object):
    def kthFactor(self, n, k):
        small = []
        large = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                small.append(i)

                if i != n // i:
                    large.append(n // i)

            i += 1

        large.reverse()
        factors = small + large

        if k <= len(factors):
            return factors[k - 1]

        return -1