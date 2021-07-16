class Node:
    def __init__(self,key):
        self.key = key
        self.palindrome = []
        self.word_id = -1
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    @staticmethod
    def isPalindrome(word):
        return word[::] == word[::-1]

    def insert(self, index, word):
        node = self.root

        #펠린드롬 상태를 알기위해 단어를 뒤집어서 트라이에 삽입
        for i, ch in enumerate(reversed(word)):
            if self.isPalindrome(word[:len(word)-i]):
                node.palindrome.append(index)
            
            if ch not in node.children:
                node.children[ch] = Node(ch)

            node = node.children[ch]    
        #단어 삽입을 마치면 word_id에 인덱스 값을 넣음
        node.word_id = index       

    def search(self, index, word):
        node = self.root

        result = []
        #1 : 입력값 + 펠린드롬값 찾기
        #단어를 찾을 때 순차적으로 찾음 - 트라이에 해당 항목이 있다면 그것은 펠린드롬이 되고 있다고 생각하면 됨
        while word:
            # node.word > -1이 있다는 뜻은 펠린드롬 될 수 있는 항목이 다른 입력값에 존재한다는 뜻
            if node.word_id > -1:
                # 그 나머지 입력값들이 펠린드롬이라면 그 수는 펠린드롬
                if self.isPalindrome(word):
                    #결과값에 인덱스와 해당 노드이 인덱스를 넣어준다.
                    result.append([index,node.word_id])
            
            if not word[0] in node.children:
                return result
            
            node = node.children[word[0]]
            word = word[1:]

        #1 - 2 : 입력값 + 펠린드롬값 찾기
        #순서대로 끝까지 탐색한 후 
        #만약 node.word_id가 0보다 같거나 크고 index가 서로 다르다면(ex) "abcd", "dcba"와 같은)
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 2 : 펠린드롬값 + 입력값 찾기
        # 끝까지 탐색했을 때 그 노드에 펠린드롬 표시가 있다면 그 단어는 펠린드롬이다. 
        for p in node.palindrome:
            result.append([index,p])

        return result    

words = ["cbbcb","","lls","s","sssll"]
trie = Trie()

results = []

for i,word in enumerate(words):
    trie.insert(i,word)

for i,word in enumerate(words):
    results.extend(trie.search(i,word))

print(results)




