# 39. Grãos no xadrez

# Variáveis
graos: int = 1
total: int = 0
i: int = 0

# Início
for i in range(64):
    total += graos
    graos *= 2

print("Total:", total)

# Fim