#URI 2295 - FROTA DE TÁXI
[pa, pg, ra, rg] = [float(ch) for ch in input().split(' ')]
n1 = ra/pa 
n2 = rg/pg 


if n1 > n2:
  print("A")
else:
  print("G")