class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ## bfs, for one continguous piece of land, update current area for neighboring
        ## once that is over, we update a max!
        ## bfs only done for those not seen :) 

        from collections import deque

        if not grid: 
            return 0

        visited = set()
        maxLand = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        columns = len(grid[0])

        def bfs(row, column): 
            queue = deque()
            queue.append((row, column)) 
            currentLand = 0

            while queue: 
                row, column = queue.popleft()
                for neighbor in neighbors: 
                    r, c = row + neighbor[0], column + neighbor[1]
                    if r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r, c) not in visited: 
                        queue.append((r, c))
                        visited.add((r, c))
                        currentLand += 1
            
            return currentLand
             
        for row in range(rows): 
            for column in range(columns): 
                if grid[row][column] == 1 and (row, column) not in visited: 
                    visited.add((row, column))
                    currentLand = bfs(row, column) + 1
                    maxLand = max(currentLand, maxLand)
        
        return maxLand






        