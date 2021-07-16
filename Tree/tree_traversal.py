n = int(input())

dic = {}

for _ in range(n):
    root, left, right = map(str, input().split())
    dic[root] = [left, right]

def preorder(x):
   if x != '.':
       print(x,end = "")
       preorder(dic[x][0])
       preorder(dic[x][1])

def inorder(x):
    if x != '.':
        inorder(dic[x][0])
        print(x,end = "")
        inorder(dic[x][1])       

def postorder(x):
    if x != '.':
        postorder(dic[x][0])
        postorder(dic[x][1])
        print(x,end="")


preorder('A')
print()
inorder('A')       
print()
postorder('A')
