class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def mark_safe(row: int, col: int) -> None:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if board[row][col] != "O":
                return
            
            board[row][col] = "S"
            
            mark_safe(row, col + 1)
            mark_safe(row + 1, col)
            mark_safe(row, col - 1)
            mark_safe(row - 1, col)


        for col in range(cols):
            mark_safe(0, col)
            mark_safe(rows -1, col)
        
        for row in range(rows):
            mark_safe(row, 0)
            mark_safe(row, cols -1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
