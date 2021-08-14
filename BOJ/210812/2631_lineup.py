import sys
from collections import deque

n=int(input())
line=[int(input()) for _ in range(n)]
dp=[0 for _ in range(n)]
dp[0]=1
MAX=0
for i in range(1,n):
  for j in range(0,i):
    if line[i] > line[j]:
      MAX = max(MAX,dp[j])
  dp[i]=MAX+1
  MAX=0
print(n-max(dp)) 


#가장 긴 부분 수열을 구함
#전체 길이에서 긴 부분 수열의 길이를 빼면
#옮겨야 할 사람의 수가 
