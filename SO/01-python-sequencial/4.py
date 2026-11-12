# Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.
# Variaveis
celsius: float = 0.0
fahrenheit: float = 0.0

# Inicio
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (9 * celsius + 160) / 5
print("A temperatura convertida em Fahrenheit é: ", fahrenheit)
# Fim