class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i:[] for i in range(n) }
        visited = [False] * n

        for node, neighbor in edges: 
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        
        def dfs(node): 
            visited[node] = True
            adjacent = graph[node]

            for neighbor in adjacent:
                if visited[neighbor] == False: 
                    dfs(neighbor)
            
        completed = 0

        for node in range(n): 
            if visited[node] == False: 
                dfs(node)
                completed += 1
        
        return completed