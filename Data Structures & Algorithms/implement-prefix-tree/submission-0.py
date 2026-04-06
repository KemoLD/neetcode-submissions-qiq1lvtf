class PrefixNodeTree:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNodeTree()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = PrefixNodeTree()

            curr = curr.children[i]

        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root

        for i in word:
            if i not in curr.children:
                return False

            curr = curr.children[i]

        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in prefix:
            if i not in curr.children:
                return False

            curr = curr.children[i]

        return True
        
        