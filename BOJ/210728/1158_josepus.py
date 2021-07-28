n,k=map(int, input().split())
a=[]*(n+1)
for i in range(n):
    a.append(i+1)
#1부터 n까지 리스트 a에 집어넣기(번호붙이기)
b=[]*(n+1)

temp=k-1 #리스트에서 추출해줄 위치
for i in range(n):
    if len(a)>temp:#리스트 길이값이 위치값보다 크면
        b.append(a.pop(temp)) #a에서는 해당 위치값을 빼주고, 그 빼준 값을 b에 넣어줌
        temp+=k-1 #위치값+(K-1)
    elif len(a)<=temp:#리스트 길이값보다 위치값이 크면
        temp=temp%len(a) #위치값을 길이값으로 나눠준 나머지룰 위치로
        b.append(a.pop(temp)) #a에서는 해당 위치값을 빼주고, 그 빼준 값을 b에 넣어줌
        temp+=k-1 #위치값+(K-1)

print("<",", ".join(str(i) for i in b),">", sep='')
#리스트에 있는 요소를 합쳐 한 덩어리로 만듦
# 그 후 각 문자 사이를 ','로 구분해서 출력
# 그리고 각 요소 사이를 띄어쓰기로 분리
