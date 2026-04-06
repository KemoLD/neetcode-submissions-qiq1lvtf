class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        schedule = { i: [] for i in range(numCourses)}
        for i,j in prerequisites:
            schedule[i].append(j)

        cycle = set()
        visited = set()
        result = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for c in schedule[course]:
                if not dfs(c):
                    return False

            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result