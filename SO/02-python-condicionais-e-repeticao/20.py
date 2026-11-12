# 20. Equação do 2º grau

# Variáveis
a: float = 0
b: float = 0
c: float = 0
delta: float = 0

# Início
import math

a = float(input("Digite A: "))
b = float(input("Digite B: "))
c = float(input("Digite C: "))

delta = b**2 - 4*a*c

if (delta < 0):
    print("Não existem raízes reais")
elif (delta == 0):
    x = -b/(2*a)
    print("Raiz:", x)
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Raízes:", x1, x2)

# Fim