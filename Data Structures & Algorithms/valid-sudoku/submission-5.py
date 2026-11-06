class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        11:12

        0 - (0,2) (2,2)
        8 - (8,8) (6,6)
        formula: i//3*3 + j//3
        0,0 0,1 0,2 0,3
        '''
        ROWS, COLS = len(board), len(board[0])
        grid = defaultdict(set)

        for r in range(ROWS):
            row_set = set()
            col_set = set()
            for c in range(COLS):
                if board[r][c] != ".":
                    # check rows
                    if board[r][c] in row_set:
                        return False
                    row_set.add(board[r][c])

                    # check grid
                    key = (r//3)*3 + (c//3)
                    if board[r][c] in grid[key]:
                        return False
                    grid[key].add(board[r][c])

                if board[c][r] != ".":  
                    # check columns
                    if board[c][r] in col_set:
                        return False
                    col_set.add(board[c][r])
                    
                
        return True
                






        