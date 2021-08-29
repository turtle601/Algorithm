class Node:
    def __init__(self, key):
        self.key = key
        self.data = False
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self,lst):
        cur = self.head

        for ch in lst:
            if not ch in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]

        cur.data = True        
            
    def search(self,depth, cur):
        if depth == 0:
            cur = self.head
    
        for ch in sorted(cur.children):
            print("--" * depth + ch)
            self.search(depth + 1,cur.children[ch])

n = int(input())

trie = Trie()

for _ in range(n):
    den = list(input().split())
    trie.insert(den[1:])

trie.search(0,None)
    
    