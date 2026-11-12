# 42. Série

# Variáveis
soma: float = 0
num: int = 1
den: int = 1
i: int = 0

# Início
for i in range(50):
    soma += num/den
    num += 1
    den += 2

print("Resultado:", soma)

# Fim