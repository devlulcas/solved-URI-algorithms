#URI 3047 - NOTA CORTADA
area_nota = 11200
meio = 5600
altura = 70
base = int(input())
topo = int(input())
area_corte =((base + topo) / 2) * altura


if (area_corte == meio):
  print("0")
elif (area_corte > meio):
  print("1")
else:
  print("2")