class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list
        crsMap = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        # 2. Run dfs on each course
        visiting = set()
        def dfs(crs, crsMap, visiting):
            if crsMap[crs] == []:
                return True

            # cycle detected
            if crs in visiting:
                return False
            visiting.add(crs)

            for pre in crsMap[crs]:
                if not dfs(pre, crsMap, visiting):
                    return False
            visiting.remove(crs)   
            crsMap[crs] = []
            return True

        # 3. for each course is it possible to finish all courses
        for i in range(numCourses):
            if not dfs(i, crsMap, visiting):
                return False
        
        return True


        

        