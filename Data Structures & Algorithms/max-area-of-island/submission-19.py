class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()
        maximum = 0
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def depth(curr): 
            position = [curr[0], curr[1]]
            area = 1

            for neighbor in neighbors: 
                candidate = [neighbor[0] + position[0], neighbor[1] + position[1]]
                candidateSet = (candidate[0], candidate[1])
                
                if candidateSet in seen: 
                    continue
                
                if candidate[0] not in range(rows) or candidate[1] not in range(cols): 
                    continue
                
                if grid[candidate[0]][candidate[1]] != 1: 
                    continue
                
                seen.add(candidateSet)
                area += depth(candidateSet)

            return area
        
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1 and (r, c) not in seen: 
                    seen.add((r, c))
                    maximum = max(maximum, depth((r, c)))
        
        return maximum

                

                 



        