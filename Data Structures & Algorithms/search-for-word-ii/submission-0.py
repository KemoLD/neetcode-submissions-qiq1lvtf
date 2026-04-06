class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self
        for x in word:
            if not x in curr.children:
                curr.children[x] = Trie()
            curr = curr.children[x]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] not in node.children:
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(res)

        