class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            # cycle detected
            if crs in visited:
                return False

            pre = courseMap[crs]
            if not pre:
                return True
            visited.add(crs)     

            for p in pre:
                if not dfs(p):
                    return False
            visited.remove(crs)
            courseMap[p] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True





        