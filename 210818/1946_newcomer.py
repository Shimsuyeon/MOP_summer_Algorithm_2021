import sys
t = int(input())

for i in range(t):
    applicant=[]
    p=int(input())
    for j in range(p):
        a,b = map(int,sys.stdin.readline().split())
        applicant.append([a,b])

    applicant.sort()    
    max=applicant[0][1]
    cnt=1
    for i in range(1,p):
        if applicant[i][1]<max:
            cnt+=1
            max=applicant[i][1]
    print(cnt)
