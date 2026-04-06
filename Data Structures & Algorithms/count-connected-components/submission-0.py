class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        count = 0

        tree = { i: [] for i in range(n) }

        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)

        def search(node, prev):

            if node in visited:
                return

            visited.add(node)
            for child in tree[node]:
                if child != prev:
                    search(child, node)

        for i in range(n):
            if i not in visited:
                search(i, None)
                count += 1

        return count

            