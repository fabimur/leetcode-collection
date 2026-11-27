class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row: int, col: int, visited: set) -> None:
            visited.add((row, col))

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                r, c = row + dr, col + dc
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and (r, c) not in visited
                    and heights[r][c] >= heights[row][col]
                ):
                    dfs(r, c, visited)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)
        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        return [list(cell) for cell in pacific & atlantic]