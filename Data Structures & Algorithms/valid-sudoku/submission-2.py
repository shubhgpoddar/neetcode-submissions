class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        matrix = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] != '.':
                    # check rows
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                
                    # check cols
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                    
                    # check grid
                    value = r//3*3 + c//3
                    if board[r][c] in matrix[value]:
                        return False
                    else:
                        matrix[value].add(board[r][c])
    
        return True
                    





        
        