# 35. Soma de ímpares

# Variáveis
a: int = 0
b: int = 0
soma: int = 0
i: int = 0

# Início
a = int(input())
b = int(input())

for i in range(min(a,b), max(a,b)+1):
    if (i % 2 != 0):
        soma += i

print("Soma:", soma)

# Fim