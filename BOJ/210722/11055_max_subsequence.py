n = int(input())
nums=list(map(int,input().split()))


dp = [0 for _ in range(n)]

for i in range(n):
    dp[i]=nums[i]
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i]=max(dp[i],dp[j]+nums[i])
print(max(dp[:n+1]))
