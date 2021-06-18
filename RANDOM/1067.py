#URI 1067 -  ODD NUMBERS
n1 = int(input())

cont = 1
for i in range(1, n1):
  print(cont)
  cont+=2
  if cont > n1:
    break