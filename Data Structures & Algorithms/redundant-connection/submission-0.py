class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = { i:[] for i in range(len(edges) + 1)}

        def dfs(node, prev):
            if node in visited:
                return True

            visited.add(node)
            for n in adj[node]:
                if n == prev:
                    continue
                elif dfs(n, node):
                    return True
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if dfs(u, -1):
                return [u, v]
        return []

