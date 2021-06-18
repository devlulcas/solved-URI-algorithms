#URI 1006 - AVERAGE 2
notas = []
for i in range(3):
  notas.append(float(input()))
media = (notas[0]*2 + notas[1]*3 + notas[2]*5) / 10
print(f"MEDIA = {media:.1f}")