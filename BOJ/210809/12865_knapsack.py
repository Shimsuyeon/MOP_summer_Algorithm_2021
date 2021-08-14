n,k=map(int, input().split())

object=[[0,0]]
for i in range(n):
    w, v = map(int, input().split())
    object.append([w,v])

gabang = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        wei = object[i][0]
        val = object[i][1]

        if j<wei:#물건 안넣음
            gabang[i][j]=gabang[i-1][j]#이전 값 그대로 내려옴
        else:#물건 넣음
            gabang[i][j]=max(val+gabang[i-1][j-wei],gabang[i-1][j])
            #

print(gabang[n][k])
