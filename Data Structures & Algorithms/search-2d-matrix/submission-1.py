class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, ROWS * COLS - 1

        while left <= right:
            middle = (left + right)//2
            row,col = middle // COLS, middle % COLS
            if target > matrix[row][col]:
                left = middle + 1
            elif target < matrix[row][col]:
                right = middle - 1
            else:
                return True
        return False
