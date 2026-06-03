from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        distance = 0
        queue = deque([])

        neighbours = {
            (-1,0), (1,0),
            (0,-1), (0,1)
        }

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i, j)
                if grid[i][j] == 0:
                    visited = set()
                    for x, y in neighbours:
                        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
                            if grid[i+x][j+y] > 0:
                                grid[i+x][j+y] = min(1, grid[i+x][j+y])
                                visited.add((i+x, j+y))
                                queue.append((i+x,j+y, grid[i+x][j+y]))
                
                    while queue:
                        row, col, min_dist = queue.popleft()
                        for x, y in neighbours:
                            if (row+x, col+y) not in visited and 0 <= row + x < len(grid) and 0 <= col + y < len(grid[0]):
                                if grid[row + x][col + y] > 0:
                                    grid[row + x][col + y] = min(min_dist + 1, grid[row + x][col + y])
                                    queue.append((row+x ,col+y, grid[row + x][col + y]))
                                    visited.add((row+x, col+y))
        
                    
            
