class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        max_rows = len(board)
        max_cols = len(board[0])
        path = set()

        def dfs(row: int, col: int, pos: int) -> bool:
            if pos == len(word):
                return True

            if (
                row < 0
                or col < 0
                or row >= max_rows
                or col >= max_cols
                or (row, col) in path
                or board[row][col] != word[pos]
            ):
                return False

            path.add((row, col))

            found = (
                dfs(row + 1, col, pos + 1)
                or dfs(row - 1, col, pos + 1)
                or dfs(row, col + 1, pos + 1)
                or dfs(row, col - 1, pos + 1)
            )

            path.remove((row, col))
            return found

        for row in range(max_rows):
            for col in range(max_cols):
                if dfs(row, col, 0):
                    return True

        return False