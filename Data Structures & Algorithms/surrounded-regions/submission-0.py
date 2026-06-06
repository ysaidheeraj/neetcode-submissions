class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        unsurrounded_regions = set()
        for i in range(ROWS):
            if board[i][0] == 'O':
                unsurrounded_regions.add((i, 0))
            if board[i][COLS-1] == 'O':
                unsurrounded_regions.add((i, COLS-1))
        
        for i in range(COLS):
            if board[0][i] == 'O':
                unsurrounded_regions.add((0, i))
            if board[ROWS-1][i] == 'O':
                unsurrounded_regions.add((ROWS-1, i))
        
        dirs = {
            (-1, 0), (1, 0),
            (0, 1), (0, -1)
        }

        visited = set()
        def dfs(i, j):
            board[i][j] = 'T'
            visited.add((i, j))
            for dr, ds in dirs:
                r, c = i + dr, j + ds
                if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in visited and board[r][c] == 'O':
                    dfs(r, c)
        
        for rx, ry in unsurrounded_regions:
            dfs(rx, ry)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
            