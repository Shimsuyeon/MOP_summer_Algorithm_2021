#미완성...고치는 중
'''
[3, 2, 1]

[3, 56, 7, 9]

9를 1번 -> 9
9와 7합침 -> 79
79를 2번 반복->7979
7979를 56과 합침->567979
567979를 3번 반복->567979567979567979
여기에 3을 추가 -> 3567979567979567979

len(리스트) ->19
'''
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
