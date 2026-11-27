class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flood(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] != 0:   # agua o ya visitada
                return
            grid[r][c] = 1        # marcar como visitada
            flood(r, c + 1)
            flood(r + 1, c)
            flood(r, c - 1)
            flood(r - 1, c)

        # Eliminar la tierra conectada al borde
        for r in range(rows):
            flood(r, 0)
            flood(r, cols - 1)
        for c in range(cols):
            flood(0, c)
            flood(rows - 1, c)

        # Contar las islas que quedan
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    flood(r, c)
                    count += 1
        return count