class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## multi source bfs, add all the rotten fruits, and convert fresh fruits to rotten

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0
        rotten = 0

        def neighbor(r, c): 
            nonlocal fresh, rotten
            
            if r not in range(rows) or c not in range(cols): 
                return 
                
            if grid[r][c] != 1: 
                return 

            if (r, c) in visited: 
                return 

            fresh -= 1
            grid[r][c] = 2
            visited.add((r, c))
            queue.append((r, c))

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r, c)) 
                    rotten += 1
                if grid[r][c] == 1: 
                    fresh += 1
        
        minutes = 0
        while queue: 
            for i in range(len(queue)): 
                r, c = queue.popleft()

                neighbor(r + 1, c)
                neighbor(r - 1, c)
                neighbor(r, c - 1)
                neighbor(r, c + 1)

            minutes += 1

        if fresh != 0: 
            return -1 
        
        if not rotten: 
            return 0

        return minutes - 1

            

        