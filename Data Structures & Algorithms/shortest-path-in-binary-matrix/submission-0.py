class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)]) # r,c, length
        visited = set((0,0))

        directions = [(0,1), (1,0), (0,-1), (-1,0),
                    (-1,-1), (1,1), (1,-1), (-1,1)]

        while q:
            r,c, length = q.popleft()
            if min(r,c) < 0 or max(r,c) == N or grid[r][c] == 1:
                continue
            
            if r == N-1 and c == N-1:
                return length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr,nc) not in visited:
                    q.append((nr,nc, 1 + length))
                visited.add((nr, nc))

        return -1
                
        