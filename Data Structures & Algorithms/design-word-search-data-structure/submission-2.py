class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if not i in curr.children:
                curr.children[i] = Trie()

            curr = curr.children[i]

        curr.end = True
        

    def search(self, word: str) -> bool:

        root = self.root

        def look(index, curr):

            for i in range(index, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if look(i + 1, child):
                            return True
                    return False
                else:
                    if not word[i] in curr.children:
                        return False
                    else:
                        curr = curr.children[word[i]]

            return curr.end

        return look(0, root)
        
