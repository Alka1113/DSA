class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # Outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            # Water / already visited
            if grid[r][c] == 0:
                return 0

            # Mark this land cell as visited
            grid[r][c] = 0

            # Count this cell + all connected land
            area = 1

            area += dfs(r - 1, c)  # up
            area += dfs(r + 1, c)  # down
            area += dfs(r, c - 1)  # left
            area += dfs(r, c + 1)  # right

            return area

        max_area = 0

        # Find every island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area