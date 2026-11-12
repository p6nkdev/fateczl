# 24. Divisibilidade por 2 e 3

# Variáveis
n: int = 0

# Início
n = int(input("Digite um número: "))

if (n % 2 == 0 and n % 3 == 0):
    print("Divisível por 2 e 3")
else:
    print("Não é divisível")

# Fim