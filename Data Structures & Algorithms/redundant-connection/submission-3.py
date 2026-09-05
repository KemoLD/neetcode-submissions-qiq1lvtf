class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [ i for i in range(len(edges) + 1) ]
        rank = [ 1 for i in range(len(edges) + 1) ]

        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2

            return True

        for i,j in edges:
            if not union(i,j):
                return [i,j]