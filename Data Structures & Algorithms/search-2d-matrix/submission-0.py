class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])

        left = 0
        right = len(matrix) * rowLen - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            x, y = (mid // rowLen, mid % rowLen)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False