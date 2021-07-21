'''
#시간초과
n = int(input())

num = [0 for _ in range(100001)]
for i in range(1,n+1):
    num[i]=i
    for j in range(1,i):
        if(j*j)>i:
            break
        num[i] = min(num[i], num[i-j*j]+1)
print(num[n])

'''
#min을 쓰면 시간초과가 걸리는 것 같다





#채점 오래걸림!!!
n =int(input())
dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])
