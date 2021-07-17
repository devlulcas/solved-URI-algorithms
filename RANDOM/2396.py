#URI 2396 - CORRIDA
[ncarros, nvoltas] = [int(n) for n in input().split(' ')]

corrida = {}
tempos = []
for carro in range(ncarros):
  tempo = [int(tvolta) for tvolta in input().split(' ')]
  tempo_total = sum(tempo)
  tempos.append(tempo_total)
  corrida[tempo_total] = carro + 1

tempos.sort()

print(corrida[tempos[0]])
print(corrida[tempos[1]])
print(corrida[tempos[2]])