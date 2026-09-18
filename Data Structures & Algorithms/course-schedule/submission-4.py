class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## build a hash map, have the prerequesite class to the other classes as the key
        ## course b is the prerequesite

        from collections import defaultdict

        if not prerequisites: 
            return True
        
        courses = defaultdict(list)
        for course in prerequisites: 
            courses[course[1]].append(course[0])
        
        visited = set()
        visiting = set()
        
        def dfs(course): 
            visiting.add(course)
            neighbors = courses[course]

            for neighbor in neighbors: 
                if neighbor in visiting: 
                    return False
                if neighbor not in visited and dfs(neighbor) is False: 
                    return False
            
            visiting.remove(course)
            visited.add(course)
            
            return True
        
        for course in prerequisites: 
            pre = course[1]
            if pre not in visited and not dfs(pre): 
                return False
        
        return True


        
        ## unconnected nodes gets cooked, that is the whole purpose of visited, is to continue to loop through all options unexplored, skip over explored ones and continue !
                






        