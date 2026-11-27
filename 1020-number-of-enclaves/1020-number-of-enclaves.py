class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        def dfs(row: int, col: int) -> None:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            
            if grid[row][col] != 1:
                return
            
            grid[row][col] = 0

            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)


        

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result += 1

        return result
        