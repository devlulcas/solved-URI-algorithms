#URI 1070 - SIX ODD NUMBERS
n1 = int(input())

if n1%2 == 0:
  n1+=1

for i in range(6):
  print(n1)
  n1+=2
  