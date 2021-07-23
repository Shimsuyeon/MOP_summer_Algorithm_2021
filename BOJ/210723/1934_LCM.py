import sys
input = sys.stdin.readline

def GCD(a, b):
    return GCD(b, a % b) if b else a
def LCM(a, b):
    return a * b // GCD(a, b)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))
