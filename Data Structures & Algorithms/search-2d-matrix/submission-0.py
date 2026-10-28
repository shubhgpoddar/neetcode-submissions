class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        # identify row
        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if top > bottom:
            return False
        row = (top + bottom) //2
        
        L, R = 0, columns - 1

        while L<=R:
            mid = (L+R)//2
            if target > matrix[row][mid]:
                L = mid + 1
            elif target < matrix[row][mid]:    
                R = mid - 1
            else:
                return True
        return False
        