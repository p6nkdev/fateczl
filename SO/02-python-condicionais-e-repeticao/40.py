# 40. Números primos

# Variáveis
a: int = 0
b: int = 0
n: int = 0
i: int = 0
primo: bool = True

# Início
a = int(input())
b = int(input())

for n in range(min(a,b), max(a,b)+1):
    if (n > 1):
        primo = True
        for i in range(2, int(n**0.5)+1):
            if (n % i == 0):
                primo = False
                break
        if (primo):
            print(n)

# Fim