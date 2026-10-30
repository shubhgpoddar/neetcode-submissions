# Multi Source BFS
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        def bfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == -1 or (r,c) in visited:
                return
            visited.add((r,c))
            q.append((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            distance+=1
        return







        
        




        