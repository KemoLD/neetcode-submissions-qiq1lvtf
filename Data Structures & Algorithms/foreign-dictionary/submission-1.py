class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        adj = { c: set() for word in words for c in word }

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            wordMin = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:wordMin] == word2[:wordMin]:
                return ""
            for j in range(wordMin):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visit = set()
        cycle = set()
        def search(letter):
            if letter in visit:
                return True
            if letter in cycle:
                return False

            cycle.add(letter)
            for c in adj[letter]:
                if not search(c):
                    return False

            visit.add(letter)
            cycle.remove(letter)
            res.append(letter)

            return True


        for c in adj:
            if not search(c):
                return ""

        res.reverse()
        return "".join(res)