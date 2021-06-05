#URI 3058 - SUPERMERCADO
n = int(input())
precos = []
for i in range(0, n):
  p, g = [float(num) for num in input().split(" ")]
  ppg = p / g 
  precos.append(ppg * 1000)
print(min(precos))