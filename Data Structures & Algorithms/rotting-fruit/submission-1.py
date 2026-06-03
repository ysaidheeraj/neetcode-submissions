from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        dirs = {
            (0,1), (0,-1),
            (1,0), (-1,0)
        }

        minutes = -1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))
            minutes += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes if minutes > -1 else 0
        

