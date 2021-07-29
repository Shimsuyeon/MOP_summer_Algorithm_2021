#미완성...고치는 중
import sys

s = input()#입력받기
a=[]#괄호 안에 있는 것들 집어넣을 리스트
b=[]
c=[]
d=[]
e=[]
close=[]
result=''#출력될 결과값
count=0
for i in s:
    a.append(i)

for i in s:
    if i=='(':#만약 여는 괄호라면
        c.append(count)
        b.append(a[count-1])

    elif i==')':#만약에 닫는 괄호라면
        close.append(count)

    count+=1

#for j in range(len(c)-1):
#    for 

'''
for j in c:
    for k in range(c[j]+1,c[j+1]-2):
        d.append(a[k])
    e.append(''.join(d))
'''
print(a)
print(b)
print(c)
print(d)
print(e)
print(close)
'''
while a:#a에 들어있는 연산자 결과값에 차례대로 넣어줌
    result+=a.pop()
    
print(result)'''
