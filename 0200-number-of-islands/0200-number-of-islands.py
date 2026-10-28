class Solution:
    def exploreIsland(self, grid: List[List[str]], x: int, y: int) -> None:
        if x == -1 or y == -1 or y == len(grid) or x == len(grid[0]) or grid[y][x] == "0":
            return
        
        grid[y][x] = "0"

        self.exploreIsland(grid, x-1, y)
        self.exploreIsland(grid, x+1, y)
        self.exploreIsland(grid, x, y-1)
        self.exploreIsland(grid, x, y+1)


    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    result += 1
                    self.exploreIsland(grid, x, y)

        return result
        
        