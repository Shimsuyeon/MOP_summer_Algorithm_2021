#9251_LCS
str1 = input()
str2 = input()

length = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

for i in range(1,len(str2)+1) :
  for j in range(1,len(str1)+1) :
    if str2[i-1] == str1[j-1] :
      length[i][j] = length[i-1][j-1] + 1
    else :
      length[i][j] = max(length[i][j-1], length[i-1][j])
print(length[-1][-1])
