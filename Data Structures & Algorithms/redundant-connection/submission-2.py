class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adjacent = {i:[] for i in range(n)}

        def dfs(node, parent): 
            if visited[node]: 
                return True
            
            visited[node] = True
            
            comparison = adjacent[node]
            for item in comparison: 
                if item == parent: 
                    continue

                if dfs(item, node):
                    return True
            
            return False
        
        for nodeOne, nodeTwo in edges: 
            adjacent[nodeOne].append(nodeTwo)
            adjacent[nodeTwo].append(nodeOne)
            visited = [False] * n

            if dfs(nodeOne, -1): 
                return [nodeOne, nodeTwo]
        
        return []