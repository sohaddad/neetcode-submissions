class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for i in range(len(matrix)):
            flat.extend(matrix[i])
        L = 0
        R = len(flat) - 1
        
        while L <= R:
            mid = (L + R) // 2
            if target < flat[mid]:
                R = mid - 1
            elif target > flat[mid]:
                L = mid + 1
            else:
                return True
        return False