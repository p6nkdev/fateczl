# Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
import math

# Variaveis
a: float = 0.0
b: float = 0.0
c: float = 0.0
delta: float = 0.0
raiz1: float = 0.0
raiz2: float = 0.0

# Inicio
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))
delta = b**2 - 4*a*c
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)
print("As raízes reais da equação são: ", raiz1, " e ", raiz2)
# Fim

# Problemático: a não pode ser zero, delta deve ser maior ou igual a zero para que as raízes sejam reais.