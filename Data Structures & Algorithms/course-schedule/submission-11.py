class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        prereq = defaultdict(list) 

        for course, pre in prerequisites: 
            prereq[course].append(pre)
        
        visited = set()

        def dfs(course): 
            if course in visited: 
                return False
            if course == []: 
                return True
            
            visited.add(course)
            pre = prereq[course]
            
            for pr in pre: 
                if not dfs(pr): 
                    return False
            
            visited.remove(course)
            prereq[course] = []
            return True
        
        for i in range(numCourses): 
            if not dfs(i): 
                return False
        
        return True

            

                
            
            


