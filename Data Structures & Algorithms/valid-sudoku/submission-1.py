class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## boxes are entered into a map
        ## each row / each column have its own respectice set

        ## iterate between, and add it into a map as you go
        from collections import defaultdict
        grids = defaultdict(set)
        columns = defaultdict(set)

        for i, row in enumerate(board): 
            currentRow = set()
            
            for j, col in enumerate(board[i]): 
                if col == ".":
                    continue
                    
                if col in currentRow: 
                    return False
                currentRow.add(col)
                
                if col in columns[j]: 
                    return False
                columns[j].add(col)

                ## strategy to group things together, simply round up after dividing by three

                box = (j // 3, i // 3)
                if col in grids[box]: 
                    return False
                grids[box].add(col)
        
        return True

                 
            
            
            
                


        