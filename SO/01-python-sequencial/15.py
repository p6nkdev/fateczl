# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
import math

# Variaveis
cat1: float = 0.0
cat2: float = 0.0
hip: float = 0.0

# Inicio
cat1 = float(input("Digite o valor do primeiro cateto: "))
cat2 = float(input("Digite o valor do segundo cateto: "))
hip = math.sqrt(cat1**2 + cat2**2) # Ou hypot(cat1, cat2)
print("A hipotenusa do triângulo é: ", hip)
# Fim