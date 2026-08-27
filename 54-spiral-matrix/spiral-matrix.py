class Solution:
    def spiralOrder(self, matrix):
        result = []

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:

            # 1. Go LEFT → RIGHT across the top
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            top += 1

            # 2. Go TOP → BOTTOM down the right side
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            right -= 1

            # 3. Go RIGHT → LEFT across the bottom
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])

                bottom -= 1

            # 4. Go BOTTOM → TOP up the left side
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                left += 1

        return result