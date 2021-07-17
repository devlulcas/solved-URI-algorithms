#URI 2342 - OVERFLOW
limite = int(input())
[n1, sinal, n2] = [ch for ch in input().split(' ')]
n1 = int(n1)
n2 = int(n2)

resultado = 0
mult = 0
soma = 0
if sinal == "*":
    mult = n1 * n2
    resultado = mult
else:
    soma = n1 + n2
    resultado = soma

if resultado > limite:
    print("OVERFLOW")
else: 
    print("OK")