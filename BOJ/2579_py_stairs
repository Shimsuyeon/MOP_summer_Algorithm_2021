import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+3)]
arr = [0 for _ in range(n+3)]
for k in range(1,n+1):
    arr[k] = int(input())


dp [1] = arr[1]
dp [2] = arr[1] + arr[2]
dp [3] = max(arr[1] + arr[3] ,arr[2] + arr[3])


for i in range(4, n+1):
    dp[i] = max( dp[i-3] + arr[i-1] + arr[i] ,  dp[i-2] + arr[i] ) 
print(dp[n])

'''
#역순으로 푸는 방법 생각해보는 중
n = input()

stairs = [ 0 for _ in range(n)]

for i in range(1, n):
    stairs[i]=input()

sum=0
for i in reversed(range(n)):
    if (stairs[i]+stairs[i-1])>(stairs[i]+stairs[i-2]):
        sum+=stairs[n-1]
    elif (stairs[i]+stairs[i-1])<(stairs[i]+stairs[i-2]):
        sum+=stairs[n-2]
        
print(sum+stairs[n])
'''
