#URI 3058 - SUPERMERCADO
n = int(input())
precos = []
for i in range(0, n):
  p, g = [float(num) for num in input().split(" ")]
  pf = (p / g) * 1000
  precos.append(pf)
print(f"{min(precos):.2f}") 