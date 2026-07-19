class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## all about splitting really, really effectively. 
        ## look at the first index of the middle row. binary search style! 

        rowMiddle = 0
        l, r = 0, len(matrix) - 1

        while l <= r: 
            rowMiddle = (l + r) // 2
            if target < matrix[rowMiddle][0]: 
                r = rowMiddle - 1

            elif target > matrix[rowMiddle][0]:
                if target > matrix[rowMiddle][-1]: 
                    l = rowMiddle + 1
                else: 
                    for number in matrix[rowMiddle]: 
                        if number == target: 
                            return True
                        else: 
                            l = rowMiddle + 1

            elif target == matrix[rowMiddle][0]: 
                return True
        
        return False
        