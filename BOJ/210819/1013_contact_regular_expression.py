import re
p = re.compile('(100+1+|01)+')
t = int(input())
case=[]
for i in range(t):
    tt=input()
    case.append(tt)


for i in range(t):
    ttt=case[i]
    m = p.fullmatch(ttt)
    if m:
        print('YES')
    else:
        print('NO')

#정규 표현식으로 풀면 굉장히 간단한 문제이다
#직관적으로 해결
