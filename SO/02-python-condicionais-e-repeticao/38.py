# 38. Maior e menor

# Variáveis
i: int = 0
n: float = 0
maior: float = 0
menor: float = 999999999

# Início
for i in range(100):
    n = float(input())
    
    if (n > 0):
        if (n > maior):
            maior = n
        if (n < menor):
            menor = n

print("Maior:", maior)
print("Menor:", menor)

# Fim