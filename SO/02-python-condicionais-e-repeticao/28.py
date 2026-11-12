# 28. Novo preço

# Variáveis
preco: float = 0
venda: int = 0

# Início
preco = float(input())
venda = int(input())

if (venda < 500 and preco < 30):
    preco *= 1.10
elif (venda < 1000 and preco < 80):
    preco *= 1.15
elif (venda >= 1000 and preco >= 80):
    preco *= 0.95

print("Novo preço:", preco)

# Fim