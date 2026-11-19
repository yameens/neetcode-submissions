class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        neighbors = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        islands = 0

        rows = len(grid)
        columns = len(grid[0])

        def depth(position): 
            
            for neighbor in neighbors: 
                
                item = [position[0] + neighbor[0], position[1] + neighbor[1]]
                candidate = (item[0], item[1])
                

                if candidate[0] in range(rows) and candidate[1] in range(columns): 
                    if candidate not in seen and grid[item[0]][item[1]] == "1": 
                        seen.add(candidate)
                        depth(candidate)
                        
                    else: 
                        continue
                else: 
                    continue
        
        ## depth simply marks all land as seen or not, and then we iterate through the graph to verify
        for r in range(rows): 

            for c in range(columns): 

                if (r, c) in seen: 
                    continue

                if grid[r][c] == "1": 
                    depth((r, c))
                    islands += 1
                    seen.add((r, c))
        
        return islands


        