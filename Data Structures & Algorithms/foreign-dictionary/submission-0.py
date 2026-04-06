class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            wordMin = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:wordMin] == word2[:wordMin]:
                return ""
            for j in range(wordMin):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        res = []
        visit = {}

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for j in adj[c]:
                if dfs(j):
                    return True
            
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)


                