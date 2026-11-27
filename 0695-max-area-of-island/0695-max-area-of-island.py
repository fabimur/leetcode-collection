class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row: int, col: int) -> int:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1
            area += dfs(row, col + 1)
            area += dfs(row + 1, col)
            area += dfs(row, col - 1)
            area += dfs(row - 1, col)

            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area