#2156_포도주시식

n = int(input())

wine=[0 for _ in range(10001)]
arr=[0 for _ in range(10001)]

for i in range(1,n+1):
    wine[i] = int(input())
#wine =[int(input()) for _ in range(n)]

arr[1]=wine[1]
arr[2]=wine[1]+wine[2]

for j in range(3,n+1):
    arr[j] = max(arr[j-1], arr[j-3]+ wine[j-1]+wine[j], arr[j-2]+wine[j])

    
print(arr[n])
