# 18. Diferença entre maior e menor valor

# Variáveis
a: int = 0
b: int = 0
diferenca: int = 0

# Início
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if (a > b):
    diferenca = a - b
elif (a < b):
    diferenca = b - a
else:
    diferenca = 0

print("Diferença:", diferenca)

# Fim