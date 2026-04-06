class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src: [] for src,dest in tickets }

        tickets.sort()
        for src,dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if not src in adj:
                return False

            for i, dest in enumerate(adj[src]):
                x = adj[src].pop(i)
                res.append(x)
                if dfs(x):
                    return True
                adj[src].insert(i, x)
                res.pop()
            return False

        dfs("JFK")
        return res