n, k = input().split()
n= int(n)
k=int(k)
gachi = []
dp=[0 for _ in range(k+1)]
dp[0]=1
for i in range(n):
    gachi.append(int(input()))

count=0

for i in gachi:
    for j in range(1, k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]


print(dp[k])
