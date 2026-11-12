# Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
# Variaveis
base: float = 0.0
altura: float = 0.0
area: float = 0.0

# Inicio
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = (base * altura) / 2
print("A área do triângulo é: ", area)
# Fim