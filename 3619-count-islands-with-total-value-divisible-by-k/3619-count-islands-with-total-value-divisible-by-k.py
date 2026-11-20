class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        result = 0

        def dfs(row: int, col: int) -> int:
            if not (0 <= row < max_row and 0 <= col < max_col):
                return 0

            value = grid[row][col]
            if value == 0:
                return 0

            grid[row][col] = 0

            value += dfs(row, col + 1)
            value += dfs(row + 1, col)
            value += dfs(row, col - 1)
            value += dfs(row - 1, col)

            return value

        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] != 0:
                    total = dfs(row, col)
                    if total % k == 0:
                        result += 1

        return result