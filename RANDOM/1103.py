#URI 1103 - ALARM CLOCK
while True:
  h1,m1,h2,m2 = [int(n) for n in input().split(" ")]
  if sum([h1,h2,m1,m2]) == 0:
    break

  t1 = h1*60 + m1
  t2 = h2*60 + m2

  if t1 >= t2:
    t2 += 1440
  print(abs(t2-t1))