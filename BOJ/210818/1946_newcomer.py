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
    #오름차순으로 정렬하면 앞자리는 모두 같은 상태
    #그 상태에서 두번째 자리 값이 작은게 나오면 MAX값을 바꿔주고
    #cnt+1을 해주면서 신입사원 명수를 구함
