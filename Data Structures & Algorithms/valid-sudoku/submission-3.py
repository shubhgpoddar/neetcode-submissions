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
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        grid = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != ".":
                    # check rows
                    if board[r][c] in row_set[r]:
                        return False
                    row_set[r].add(board[r][c])

                    # check grid
                    key = (r//3)*3 + (c//3)
                    if board[r][c] in grid[key]:
                        return False
                    grid[key].add(board[r][c])
                
                    # check columns
                    if board[r][c] in col_set[c]:
                        return False
                    col_set[c].add(board[r][c])
                    
                
        return True
                






        