#푸는 중...골드5문제...ㅠ
import sys
from itertools import chain, combinations
s = input()#입력받기
eq=[]#괄호 안에 있는 것들 집어넣을 리스트
open=[]
close=[]
result=[]
count=0
for i in s:
    eq.append(i)

for i in s:
    if i=='(':#만약 여는 괄호라면
        open.append(count)

    elif i==')':#만약에 닫는 괄호라면
        close.append(count)

    count+=1

comb_open=[]
for i in range(0,len(open)+1):
    c=combinations(open,i)
    comb_open.extend(c)
print(comb_open)

comb_close=[]
for i in range(0,len(close)+1):
    c=combinations(close,i)
    comb_close.extend(c)
print(comb_close)



for i in range(0,len(open)):
    eq2=eq[:]
    eq2.pop(open[i])
    eq2.pop(close[i]-1)
    r=''.join(eq2)
    result.append(r)


for k in result:
    print(k)


print(open)
print(close)
