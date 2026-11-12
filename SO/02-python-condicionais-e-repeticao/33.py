# 33. Série harmônica

# Variáveis
n: int = 0
soma: float = 0
i: int = 0

# Início
n = int(input("Digite N: "))

for i in range(1, n+1):
    soma += 1/i

print("Resultado:", soma)

# Fim