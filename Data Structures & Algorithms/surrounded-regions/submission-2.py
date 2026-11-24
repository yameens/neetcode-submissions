class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ## non surroundable o's connect from the edges (read the description) 
        ## if an o is touching, add to this visited set of o's (these are going to stay protected)

        ## collect all starting nodes (which are exterier o's)

        ROWS = len(board)
        COLS = len(board[0])
        protected = set()
        queue = deque()

        def addPosition(r, c): 
            nonlocal queue

            if r not in range(ROWS) or c not in range(COLS): 
                return 
            
            if board[r][c] == 'X': 
                return 

            if (r, c) in protected: 
                return
            
            queue.append((r, c))

        for r in range(ROWS): 
            for c in range(COLS): 
                if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1: 
                    if board[r][c] == 'O': 
                        queue.append((r, c))
        
        while queue: 
            iterate = len(queue) 
            for i in range(iterate): 
                curr = queue.popleft()
                r, c = curr[0], curr[1]
                protected.add(curr)
                
                addPosition(r + 1, c)
                addPosition(r, c + 1) 
                addPosition(r - 1, c)
                addPosition(r, c - 1)

                
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r, c) not in protected and board[r][c] == 'O':
                    board[r][c] = 'X'
        

        





        