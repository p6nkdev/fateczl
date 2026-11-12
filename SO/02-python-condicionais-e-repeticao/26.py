# 26. Verificar múltiplo

# Variáveis
a: int = 0
b: int = 0

# Início
a = int(input())
b = int(input())

if (max(a,b) % min(a,b) == 0):
    print("É múltiplo")
else:
    print("Não é múltiplo")

# Fim