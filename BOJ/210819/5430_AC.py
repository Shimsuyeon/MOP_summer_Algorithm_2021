'''#시간초과 나는 코드... 마지막 예제 n=0일 때 해결 필요
import sys
from collections import deque

t = int(input())

for i in range(t):
    fuc = input()
    func = list(fuc)
    n = int(input())

    
    num = list(map(int, input()[1:-1].split(',')))
    print(func)
    for i in range(len(func)):
        if func[i]=='R':
            num.reverse()
        elif func[i]=='D':
            if len(num)!=0:
                del num[0]
            else:
                print('error')

    print(num)
    '''
