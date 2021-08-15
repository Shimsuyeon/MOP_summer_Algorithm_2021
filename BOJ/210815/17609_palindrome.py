'''#시간초과
n=int(input())
for i in range(n):
    word = input()

    if list(word) == list(reversed(word)):
        print(0)
    else:
        cnt=0
        for j in word[:]:
            word2=list(word)
            word2.remove(j)
            if word2==list(reversed(word2)):
                print(1)
                cnt+=1
        if cnt==0:
            print(2)
            '''
