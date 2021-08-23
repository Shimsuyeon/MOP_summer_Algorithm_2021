import re
# 정규표현식

def solution(s):
    length=len(s)
    str,cnt=0,1
    cand = [length]
    #문자열 쪼개기
    for size in range(1,length):
        comp=""
        split = [s[i:i+size] for i in range(0,length,size)]
        stack = [[split[0],1]]

        for unit in split[1:]:
            if stack[-1][str]!=unit:
                stack.append([unit, 1])
            else:
                stack[-1][cnt]+=1
        comp += ('').join([str[cnt]+w if cnt>1 else w for w, cnt in stack])
        cand.append(len(comp))
    return min(cand)
