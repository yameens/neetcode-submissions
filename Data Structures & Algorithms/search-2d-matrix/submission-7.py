class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## binary search, find the value within the matrix

        l, r = 0, len(matrix) - 1

        while l <= r: 
            middle = (l + r) // 2
            if matrix[middle][0] > target: 
                r = middle - 1
            elif matrix[middle][-1] < target: 
                l = middle + 1
            else: 
                for num in matrix[middle]: 
                    if num == target: 
                        return True
                break
        
        return False

        