#URI 3048 - SEQUÊNCIA SECRETA
array = []
length = int(input())
for i in range(length):
    array.append(int(input()))
circles = 1
next = 0
first = array[0]
for i in range(length):
  next = array[i]
  if (first != next):
    circles+=1
    first = next
print(circles)
