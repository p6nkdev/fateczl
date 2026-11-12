# 37. Fibonacci

# Variáveis
n: int = 0
a: int = 0
b: int = 1
i: int = 0

# Início
n = int(input())

for i in range(n):
    print(a)
    aux = a + b
    a = b
    b = aux

# Fim