class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## create a dependency list
        ## do depth first search to see if there is any dependent loop
        ## if there is any dependent loop, return false: if dfs(course) == False

        from collections import defaultdict
        dependent = defaultdict(list)

        for course, pre in prerequisites: 
            dependent[course].append(pre)
        
        visited = set()
        completed = set()

        solution = []
        def dfs(course): 
            if course in visited: 
                return False
            
            if course in completed: 
                return True
            
            visited.add(course)
            requirements = dependent[course]

            for require in requirements: 
                if not dfs(require): 
                    return False
            
            visited.remove(course)
            completed.add(course)

            solution.append(course)

            return True
        
        for i in range(numCourses): 
            if not dfs(i): 
                return []
        
        return solution
            
        
        




        
        