class Node:
    #노드 초기화
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    #삽임 함수
    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]

        cur.data = word    

    #탐색 함수
    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                return False

            cur = cur.children[ch]

        if cur.data == None:
            return False

        else:
            return True        

    #접두사 확인함수
    def startsWith(self, prefix: str) -> bool:
        cur = self.head

        for ch in prefix:
            if ch not in cur.children:
                return False

            cur = cur.children[ch]

        return True    