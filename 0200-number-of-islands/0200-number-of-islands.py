class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> None:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)

        num_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1

        return num_islands