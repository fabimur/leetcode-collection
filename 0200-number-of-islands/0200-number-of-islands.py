class Solution:
    def dfs(self, grid: List[List[str]], x, y) -> None:
        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
            return

        if grid[y][x] == "0":
            return
        
        grid[y][x] = "0"
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)
        



    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.dfs(grid, x, y)
                    result += 1


        return result


        
        