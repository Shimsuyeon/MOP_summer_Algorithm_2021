import sys

s = input()#입력받기
a=[]#괄호 안에 있는 것들 집어넣을 리스트
result=''#출력될 결과값
for i in s:
    if i.isalpha():#피연산자인지 아닌지 확인
        result+=i#피연산자이면 결과값에 바로 집어넣기
    else:
        if i=='(':#만약 여는 괄호라면
            a.append(i)#a 리스트에 넣음
        elif i=='*' or i=='/':#만약 곱하기랑 나누기라면
            while a and (a[-1]=='*' or a[-1]=='/'):#a에서 곱하기랑 나누기가 나올때까지
                result+=a.pop()#a에서 빼서 결과값에 집어넣음
            a.append(i)#a에 넣어줌
        elif i=='+' or i=='-':#만약 더하기랑 빼기면
            while a and a[-1]!='(':#여는 괄호가 아니면
                result+=a.pop()#a에 들어있는 마지막값을 결과값에 집어넣음
            a.append(i)#a에 i를 넣어줌
        elif i==')':#만약에 닫는 괄호라면
            while i and a[-1]!='(':#여는 괄호가 아니면
                result+=a.pop()#결과값에 a마지막걸 넣어줌
            a.pop()#a에서 빼냄
while a:#a에 들어있는 연산자 결과값에 차례대로 넣어줌
    result+=a.pop()
    
print(result)
