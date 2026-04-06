class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [ i for i in range(len(edges) + 1)]
        rank = [ 1 for i in range(len(edges) + 1)]

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(one, two):
            a, b = find(one), find(two)

            if a == b:
                return False
            if rank[a] > rank[b]:
                parent[b] = a
                rank[a] += rank[b]
            else:
                parent[a] = b
                rank[b] += rank[a]
            return True

        for i,j in edges:
            if not union(i,j):
                return [i,j]
