
import sys
b = []
def push(num):
    a.append(num)
def pop(a):
    if a:
        print(a[-1])
        a.pop(-1)
    elif not a: 
        print(-1)
def size(a):
    print(len(a))
def empty(a):
    if not a:
        print(1)
    elif a:
        print(0)
def top(a):
    if a:
        print(a[-1])
    elif not a:
        print(-1)


n =int(sys.stdin.readline().rstrip())
a = []

for _ in range(n):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]

    if order=='push' :
        push(input_split[1])
    elif order=='pop':
        pop(a)
    elif order=='size':
        size(a)
    elif order=='empty':
        empty(a)
    elif order=='top':
        top(a)

