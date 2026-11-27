class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
            
        rows = len(image)
        cols = len(image[0])

        def dfs(row, col, old_color, new_color) -> None:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if image[row][col] != old_color:
                return
            
            image[row][col] = new_color

            dfs(row, col + 1, old_color, new_color)
            dfs(row + 1, col, old_color, new_color)
            dfs(row, col - 1, old_color, new_color)
            dfs(row - 1 , col, old_color, new_color)

        dfs(sr, sc, image[sr][sc], color)
        return image
        