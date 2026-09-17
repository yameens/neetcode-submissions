class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## breadth first search, vs. depth first search

        ## breadth first search has a common pattern
        ## it holds a visited set to avoid repetitive land
        ## it visits neighbors (not in set)
        ## adds to set and puts it in the queue

        from collections import deque

        if grid is None: 
            return -1

        visited = set()
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def bfs(row, column):
            queue = deque()
            queue.append((row, column))
            
            while queue: 
                row, column = queue.popleft()
                for neighbor in neighbors: 
                    r, c = row + neighbor[0], column + neighbor[1]
                    if r in range(rows) and c in range(columns) and (r, c) not in visited and grid[r][c] == "1": 
                        queue.append((r, c))
                        visited.add((r, c))

        for row in range(len(grid)): 
            for column in range(len(grid[row])): 
                if (row, column) not in visited and grid[row][column] == "1": 
                    islands += 1
                    visited.add((row, column))
                    bfs(row, column)
        
        return islands



        
        