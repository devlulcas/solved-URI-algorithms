#URI 1005 - AVERAGE 1
notas = []
for i in range(2):
  notas.append(float(input()))
media = (notas[0]*3.5 + notas[1]*7.5) / 11
print(f"MEDIA = {media:.5f}")