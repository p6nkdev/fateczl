# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.
# Variaveis
ang1: float = 0.0
ang2: float = 0.0
ang3: float = 0.0

# Inicio
ang1 = float(input("Digite o primeiro ângulo: "))
ang2 = float(input("Digite o segundo ângulo: "))
ang3 = 180 - (ang1 + ang2)
print("O valor do terceiro ângulo é: ", ang3)
# Fim