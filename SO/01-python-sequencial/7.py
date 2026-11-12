# Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
# Variaveis
comprimento: float = 0.0
largura: float = 0.0
altura: float = 0.0
volume: float = 0.0

# Inicio
comprimento = float(input("Digite o comprimento do paralelepípedo: "))
largura = float(input("Digite a largura do paralelepípedo: "))
altura = float(input("Digite a altura do paralelepípedo: "))
volume = comprimento * largura * altura
print("O volume do paralelepípedo é: ", volume)
# Fim