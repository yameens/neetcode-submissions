class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None: 
            return 

        sub = []
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(board), len(board[0])
        result = []
        visited = set()

        def dfs(i, j): 
            sub.append(board[i][j])
            visited.add((i, j))

            if "".join(sub) == word: 
                return True

            if not word.startswith("".join(sub)):
                sub.pop()
                visited.remove((i, j))
                return False

            for neighbor in neighbors: 
                if neighbor[0] + i in range(rows) and neighbor[1] + j in range(cols): 
                    r, c = neighbor[0] + i, neighbor[1] + j
                    if (r, c) not in visited: 
                        if dfs(r, c): 
                            return True
                
            sub.pop()
            visited.remove((i, j))

            return False
        
        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if dfs(r, c): 
                    return True
        
        return False


            


            

        