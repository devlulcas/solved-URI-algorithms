#URI 3047 - A IDADE DE DONA MÔNICA
monica = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = monica - (filho1 + filho2)
mais_velho = filho3

if (filho1 >= filho2 and filho1 >= filho3):
  mais_velho = filho1
elif (filho2 >= filho1 and filho2 >= filho3):
    mais_velho = filho2

print(mais_velho)