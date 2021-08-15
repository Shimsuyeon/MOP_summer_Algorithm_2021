'''#1012_유기농배추
#필요한 최소의 배추흰지렁이 마리 수 출력 #서로 인접해 있는 배추들이 몇 군데에 퍼져있는가
from collections import deque
T=int(input())
#테스트 케이스 개수
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    print(queue)
    while queue:
        x,y=queue.popleft()
        for i in range(4):#4방향 탐색
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                #현재의 nx ny가 주어진 범위 내라면
                continue
            if baechu[nx][ny]==1:
                baechu[nx][ny]=0
                queue.append((nx,ny))
                #queue에 넣기
                
    print(queue)

for j in range(T):
    M,N,K=map(int, input().split())
    #가로 세로 배추개수
    baechu = [[0] * M for i in range(N)]
    cnt=0
    for i in range(K):
        a,b=map(int, input().split())
        baechu[b][a]=1
    for i in range(N):
        for j in range(M):
            if baechu[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)'''
t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0
                cnt += 1
    print(cnt)
