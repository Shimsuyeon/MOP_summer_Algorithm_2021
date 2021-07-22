import sys

n = int(input())
nums=list(map(int,input().split()))
dp = [1 for i in range(n)]
'''
a = [0 for _ in range(n+1)]
sequence=0
for i in range(1,n):
    if a[i-1]<nums[i]:
        a[i]=nums[i]
for j in range(0,n):
    if a[j]!=0:
        sequence=sequence+1
#시도해본 코드
'''
for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
