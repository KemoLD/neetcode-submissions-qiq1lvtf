class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.nxt = self.right
        self.right.prev = self.left


    def insert(self, node):
        p = self.right.prev
        self.right.prev = node

        node.nxt = self.right
        node.prev = p

        p.nxt = node


    def remove(self, node):
        l = node.prev
        r = node.nxt

        l.nxt = r
        r.prev = l

        node.nxt = None
        node.prev = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            x = self.left.nxt
            self.remove(x)
            del self.cache[x.key]


        
