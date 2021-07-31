n=int(input())

num=[]
for i in range(n):
    num.append(int(input()))
dp=[1,2,4]

for i in range(3,1000001):
    dp.append(dp[i-1]%1000000009+dp[i-2]%1000000009+dp[i-3]%1000000009)

for i in num:
    print(dp[i-1]%1000000009)
