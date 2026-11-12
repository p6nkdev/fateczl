# Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.
import math

# Variaveis
raio: float = 0.0
comprimento: float = 0.0

# Inicio
raio = float(input("Digite o raio da circunferência: "))
comprimento = 2 * math.pi * raio
# comprimento = round(comprimento, 2) # Caso precisasse arredondar
print("O comprimento da circunferência é: ", comprimento)
# Fim
