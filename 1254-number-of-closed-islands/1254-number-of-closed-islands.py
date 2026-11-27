class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_enclosed = 0


        def mark_safe(row: int, col: int) -> None:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            
            if grid[row][col] != 0:
                return
            
            grid[row][col] = 2

            mark_safe(row, col + 1)
            mark_safe(row + 1, col)
            mark_safe(row, col - 1)
            mark_safe(row - 1, col)

        

        def dfs(row:int, col:int) -> None:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            
            if grid[row][col] != 0:
                return

            grid[row][col] = 1

            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)


        for row in range(rows):
            mark_safe(row, 0)
            mark_safe(row, cols-1)
        
        for col in range(cols):
            mark_safe(0, col)
            mark_safe(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col)
                    num_enclosed += 1

        return num_enclosed
        