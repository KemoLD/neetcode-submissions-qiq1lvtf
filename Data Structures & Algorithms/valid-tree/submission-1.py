class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True 

        adj = { i: [] for i in range(n)}
        visited = set()

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for child in adj[node]:
                if child != prev:
                    if not dfs(child, node):
                        return False

            return True

        return dfs(0, None) and len(visited) == n