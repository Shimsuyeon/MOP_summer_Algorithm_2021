#아직 푸는 중...미완성

n,k = map(int, input().split())

object = []
for i in range(0,n):
    w,v=map(int,input().split())
    object.append((w,v))
dp = [[0]*(k+1) for _ in range(n+1)]


'''
for i in range(0,n):
    if (dp[i][1]+object[i][0])<=k:
        a=int(dp[0]+object[i][0])
        b=int(dp[1]+object[i][1])
        dp.append((a,b))
        maximum=max(dp[i][1],dp[i-1][1])


print(maximum)
'''
for i in range(1,n+1):
    for j in range(1,k+1):
        w=object[i][0]
        v=object[i][1]
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])
'''
weight=[]
value=[]
for i in range(0,n):
    w,v=map(int,input().split())
    weight.append(w)
    value.append(v)

'''
