class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges): 
            return False
        
        ## too many edges actually represent a cycle
        ## mathematic property of a tree

        visited = set()

        dependent = {i:[] for i in range(n)}
        for node, neighbor in edges: 
            dependent[node].append(neighbor)
            dependent[neighbor].append(node)

        def dfs(node): 
            if node in visited:
                return 
            
            visited.add(node)
            neighbors = dependent[node]

            for neighbor in neighbors: 
                dfs(neighbor)
            
        
        dfs(0)
        return len(visited) == n

        