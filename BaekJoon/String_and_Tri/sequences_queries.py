import sys
input = sys.stdin.readline

# 노드 생성
class Node(object):
    def __init__(self, data):
        self.data = data    #다녀왔다는 표시, 한번 다녀왔으면 0, 두번 1, ...
        self.left = {}      #좌측이 0
        self.right = {}     #우측이 1

# 트라이 생성
class Trie(object):
    #root노드에 Node 생성
    def __init__(self):
        self.head = Node(0)

    #삽입함수
    def insert(self,word):
        cur = self.head

        for ch in word:
            # 삽입 단어가 0일 시
            if ch == "0":
                if cur.left:
                    # left에 다녀왔다는 표시 += 1 추가 
                    cur.left.data += 1

                else:
                    # 다녀온 적이 없다면 노드 생성
                    cur.left = Node(0)

                cur = cur.left

            # 삽입 단어가 1일 시
            else:
                if cur.right:
                    cur.right.data += 1
                
                else:
                    cur.right = Node(0)              

                cur = cur.right  
    
    # 삭제 함수
    def delete(self, word):
        cur = self.head

        for ch in word:
            # 삭제할 값이 0이고
            if ch == "0":
                # 0을 다녀왔다는 표시(data)가 0보다 클 경우 -= 1
                if cur.left.data > 0:
                    cur.left.data -= 1

                # 0일 경우 해당 노드를 없앱니다. 
                else:
                    cur.left = False
                    break
                
                cur = cur.left

            # 삭제할 값이 1이고
            else:
                # 1을 다녀왔다는 표시(data)가 0보다 클 경우 -= 1
                if cur.right.data > 0:
                    cur.right.data -= 1
                
                # 0일 경우 해당 노드를 없앱니다. 
                else:
                    cur.right = False
                    break

                cur = cur.right

    #XOR 연산함수 - 만들어진 트라이에서 입력받은 수에서 반대로 가면 된다. 0 -> 1, 1 -> 0
    def xor(self, word):
        cur = self.head
        ans = "0b"

        for ch in word:
            # 0 -> 1
            if ch == "0":
                if cur.right :
                    ans += "1"
                    cur = cur.right
                #0 -> 1로 가고 싶지만 트라이에 해당 값이 없을 때(cur.right == {})
                else:
                    ans += "0"                    
                    cur = cur.left
            # 1 -> 0
            else:
                if cur.left :
                    ans += "1"
                    cur = cur.left 

                #1 -> 0로 가고 싶지만 트라이에 해당 값이 없을 때(cur.left == {})
                else:
                    ans += "0"
                    cur = cur.right           
 
        answer = int(ans,2)
        return answer

n = int(input())

trie = Trie()
t = format(0,'b').zfill(30)
trie.insert(t)

for _ in range(n):
    how, x = map(int, input().split())
    # 자릿수의 공정한 비교를 위해 30으로 다 채운다. 
    word = format(x,'b').zfill(30)
    
    # 1일 때 삽입
    if how == 1:
        trie.insert(word)

    # 2일 때 삭제
    elif how == 2:
        trie.delete(word)

    # 3일 때 xor
    elif how == 3:
        result = trie.xor(word)
        print(result)        