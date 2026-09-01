class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        original = [row[:] for row in board]

        for r in range(rows):
            for c in range(cols):

                count = 0

                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:

                        if dr == 0 and dc == 0:
                            continue

                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if original[nr][nc] == 1:
                                count += 1

                if original[r][c] == 0 and count == 3:
                    board[r][c] = 1

                elif original[r][c] == 1 and (count == 2 or count == 3):
                    board[r][c] = 1

                else:
                    board[r][c] = 0