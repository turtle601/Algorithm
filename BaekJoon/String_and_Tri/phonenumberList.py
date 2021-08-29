import sys
input = sys.stdin.readline

#노드 클래스
class Node(object):
    def __init__(self, key, data = None):
        self.key = key     # key: 해당 노드
        self.data = data   # data: data의 자식노드가 없다면 해당 문자열을 저장
        self.children = {} # children: key의 자식들

#트라이 클래스
class Trie(object):
    def __init__(self):
        self.head = Node(None)
 
    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                #해당 자식이 없다면 자식 생성
                cur.children[ch] = Node(ch)
            
            #자식이 부모가 되서 자식 유무 판단
            cur = cur.children[ch] 

        #단어 삽입이 끝났으면 data값에 word를 넣는다.    
        cur.data = word
        

    def search(self, word):
        cur = self.head

        for ch in word:
            cur = cur.children[ch] 

        # 단어를 다 탐색한 후 자식이 있다면 오류가 날 수 있다.  
        if cur.children:
            return False
        else:
            return True

t = int(input())

for _ in range(t):
    n = int(input())

    trie = Trie()

    nums = []

    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)

    flag = True
    
    nums.sort()

    for num in nums:
        if not trie.search(num):
            flag = False
            break
    
    if flag:
        print('YES')
    else:
        print('NO')            




