class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        visited = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1

        def rotFruit(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visited:
                return
            
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh-=1
                rotten.append((r,c))
            visited.add((r,c))
            return
        
        minutes = 0

        while fresh > 0 and rotten:
            
            for i in range(len(rotten)):
                r,c = rotten.popleft()
                rotFruit(r+1, c)
                rotFruit(r, c+1)
                rotFruit(r-1, c)
                rotFruit(r, c-1)
            minutes+=1
            
        
        if fresh > 0:
            return -1
        return minutes







            

        

        