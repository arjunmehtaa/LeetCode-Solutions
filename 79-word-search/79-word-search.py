directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, i):
            if i >= len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            char = board[r][c]
            board[r][c] = ""
            for direction in directions:
                row = r + direction[0]
                col = c + direction[1]
                if dfs(row, col, i + 1):
                    return True
            board[r][c] = char
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
        