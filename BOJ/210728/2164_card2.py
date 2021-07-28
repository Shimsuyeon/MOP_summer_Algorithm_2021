n=int(input())

card=[]*(n+1)
for i in range(n):
    card.append(i+1)

while(len(card)>1):
   card.pop(0)
   card.append(card.pop(0))

print(card.pop(0))
