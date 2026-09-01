class Solution:
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            # Out of bounds or wrong character
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[index]:
                return False

            # We found the whole word
            if index == len(word) - 1:
                return True

            # Mark this cell as used
            temp = board[r][c]
            board[r][c] = "#"

            # Try up, down, left, right
            found = (
                dfs(r - 1, c, index + 1) or
                dfs(r + 1, c, index + 1) or
                dfs(r, c - 1, index + 1) or
                dfs(r, c + 1, index + 1)
            )

            # Undo the change
            board[r][c] = temp

            return found

        # Try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False