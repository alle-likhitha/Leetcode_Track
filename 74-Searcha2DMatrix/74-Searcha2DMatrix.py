# Last updated: 4/19/2025, 2:48:40 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fixed_i = None
        for i in range(len(matrix)):
            if target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                fixed_i = i
                break
        if fixed_i == None:
            return False
        else:
            low = 0
            high = len(matrix[fixed_i]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[fixed_i][mid] == target:
                    return True
                elif matrix[fixed_i][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                # print(low, high)
        return False