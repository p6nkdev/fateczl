# 36. Série com fatorial

import math

# Variáveis
n: int = 0
soma: float = 1
i: int = 0

# Início
n = int(input())

for i in range(1, n+1):
    soma += 1/math.factorial(i)

print("Resultado:", soma)

# Fim