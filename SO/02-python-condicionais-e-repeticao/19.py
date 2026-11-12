# 19. Maior valor

# Variáveis
a: float = 0
b: float = 0
maior: float = 0

# Início
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

if (a > b):
    maior = a
else:
    maior = b

print("Maior valor:", maior)

# Fim