class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ## multi-source bfs, all distances incremented after one radial pass, from each 
        ## treasure chest at once, thus, the best distance is actually used. 

        rows = len(grid) 
        cols = len(grid[0])
        visited = set()
        queue = deque()

        ## first, add all the treasure chests into our queue. we are adding all at once!

        def addCell(r, c): 
            if (r, c) in visited or r not in range(rows) or c not in range(cols): 
                return 
            
            if grid[r][c] == 0 or grid[r][c] == -1: 
                return

            queue.append((r, c))
            visited.add((r, c))
 
        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == 0: 
                    queue.append((row, col))
        
        distance = 0
        while queue: 
            ## we focus on one level at a time, thus we use the queue length method
            for i in range(len(queue)): 
                r, c = queue.popleft()
                grid[r][c] = distance
                
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            distance += 1
        
        ## if we are adding per level, you know we need the queue method! 


        