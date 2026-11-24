class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i:[] for i in range(n) }
        visited = [False] * n

        for node, neighbor in edges: 
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        
        def dfs(node): 
            adjacent = graph[node]

            for neighbor in adjacent:
                if visited[neighbor] == False: 
                    visited[neighbor] = True
                    dfs(neighbor)
            
        completed = 0

        for node in range(n): 
            if visited[node] == False: 
                visited[node] = True
                dfs(node)
                completed += 1
        
        return completed