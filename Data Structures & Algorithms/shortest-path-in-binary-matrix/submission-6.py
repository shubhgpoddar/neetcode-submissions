class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        q = deque([(0,0,1)]) # r,c, length
        visited = {(0, 0)}

        directions = [(0,1), (1,0), (0,-1), (-1,0),
                    (-1,-1), (1,1), (1,-1), (-1,1)]

        while q:
            r,c, length = q.popleft()
            if r == N-1 and c == N-1:
                return length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if ((nr,nc) not in visited) and not (min(nr, nc) < 0 or max(nr,nc) >= N or grid[nr][nc] == 1):
                    q.append((nr,nc, 1 + length))
                    visited.add((nr, nc))

        return -1
                
        