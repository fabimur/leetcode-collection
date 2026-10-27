class Solution:
    def exploreIsland(self, grid: List[List[str]], x: int, y: int):    
        if grid[y][x] != "1":
            return
            
        grid[y][x] = "0"

        if x > 0:
            self.exploreIsland(grid, x-1, y)
        if x  + 1 < len(grid[0]):
            self.exploreIsland(grid, x+1, y)
        if y > 0:
            self.exploreIsland(grid, x, y-1)
        if y + 1< len(grid):
            self.exploreIsland(grid, x, y+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.exploreIsland(grid, x, y)
                    result += 1

        return result
        