class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        11:01 O(n)
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS-1
        
        # find the row
        while top <= bottom:
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if top > bottom:
            return False
        
        L, R = 0, COLS-1

        while L<=R:
            mid = (L+R)//2
            if target > matrix[row][mid]:
                L = mid + 1
            elif target < matrix[row][mid]:
                R = mid - 1
            else:
                return True
        return False
            
            
        
                


        
        