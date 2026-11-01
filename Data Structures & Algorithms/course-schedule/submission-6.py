class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list
        crsMap = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        # 2. Run dfs on each course
        visited = set()
        def dfs(crs, crsMap, visited):
            if crsMap[crs] == []:
                return True

            if crs in visited:
                return False
            visited.add(crs)

            for pre in crsMap[crs]:
                if not dfs(pre, crsMap, visited):
                    return False
            visited.remove(crs)   
            crsMap[crs] = []
            return True

        # 3. for each course is it possible to finish all courses
        for i in range(numCourses):
            if not dfs(i, crsMap, visited):
                return False
        
        return True


        

        