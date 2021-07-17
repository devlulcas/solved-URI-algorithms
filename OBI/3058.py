#URI 3058 - SUPERMERCADO
n = int(input())
precos = []
for i in range(n):
  p, g = [float(num) for num in input().split(" ")]
  precos.append((p / g) * 1000)
print(f"{min(precos):.2f}") 