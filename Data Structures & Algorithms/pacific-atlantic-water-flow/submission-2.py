class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## condition
        ## either less than zero, or equal to the bounds, or the new one is LESS than the previous (must be greater) or it is already in visited (set) return. 
        ## dfs: contains bound, new position, and previous height. add position to visited, go in every direction for visited! 

        ## logic, we must iterate for all the relevant columns from PACIFIC / ATLANTIC
        ## logic, we must iterate for all the relvant rows from PACIFIC / ATLANTIC

        ## if the path is in both atlantic and pacific visited, we are SUPER set (because then it connects!)

        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight): 
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or heights[r][c] < prevHeight: 
                return 

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for row in range(ROWS): 
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])
        
        for col in range(COLS): 
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
        
        result = []
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r, c) in pac and (r, c) in atl: 
                    result.append([r, c])
        
        return result