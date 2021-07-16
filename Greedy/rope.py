n = int(input())
rop = [int(input()) for _ in range(n)]
rop.sort(reverse=True)

dp = rop[0]

for i in range(1,len(rop)):
    check = rop[i] * (i+1)
    if dp < check:
        dp = check

print(dp)                      
