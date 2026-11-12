# 29. Investimento

# Variáveis
tipo: int = 0
valor: float = 0

# Início
tipo = int(input())
valor = float(input())

if (tipo == 1):
    print(valor * 1.03)
elif (tipo == 2):
    print(valor * 1.05)
else:
    print("Tipo inválido")

# Fim