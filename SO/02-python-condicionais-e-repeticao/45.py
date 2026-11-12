# 45. Série alternada

# Variáveis
soma: float = 0
sinal: int = 1
i: int = 0

# Início
for i in range(1,16):
    soma += sinal * (i/(i*i))
    sinal *= -1

print("Resultado:", soma)

# Fim