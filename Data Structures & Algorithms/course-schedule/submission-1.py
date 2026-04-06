class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        c = { i: [] for i in range(numCourses) }

        for i, j in prerequisites:
            c[i].append(j)

        def search(course, visited):
            if c[course] == []:
                return True
                
            if course in visited:
                return False

            visited.add(course)
            for x in c[course]:
                if not search(x, visited):
                    return False

            c[course] = []
            return True

        for i in range(numCourses):
            if not search(i, set()):
                return False

        return True