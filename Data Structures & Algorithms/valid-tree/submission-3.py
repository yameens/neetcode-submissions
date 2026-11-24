class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## any cycles make an invalid tree: this is a graph, that is why we can simply build an adjacency list and run depth first search on said lists. anything in the visited list gets completely BOOTED. 

        dependent = {i:[] for i in range(n)} 

        if n - 1 != len(edges): 
            return False

        for edge, depend in edges: 
            dependent[edge].append(depend)
            dependent[depend].append(edge)
        
        ## must be multidirectional 
        
        visited = set()
        def dfs(edge): 
            if edge in visited: 
                return
            
            items = dependent[edge]
            visited.add(edge)

            for item in items: 
                dfs(item)
        
        dfs(0)
            
        return len(visited) == n

            
            

            
        