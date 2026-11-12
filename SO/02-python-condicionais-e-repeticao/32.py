# 32. Fatorial

# Variáveis
n: int = 0
fat: int = 1
i: int = 0

# Início
n = int(input("Digite um número: "))

for i in range(1, n+1):
    fat *= i

print("Fatorial:", fat)

# Fim