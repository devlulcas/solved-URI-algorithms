#URI 1066 - EVEN, ODD, POSITIVE AND NEGATIVE
even, odd, pos, neg = 0, 0, 0, 0
for i in range(5):
  n = int(input())
  if n%2 == 0:
    even += 1
  else:
    odd += 1

  if n<0:
    neg += 1
  elif n>0:
    pos += 1 

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")