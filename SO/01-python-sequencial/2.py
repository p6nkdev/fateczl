# Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.
# Variaveis
salario: float = 0.0
resultado: float = 0.0

# Inicio
salario = float(input("Digite o salário do funcionário: "))
resultado = salario + (salario * 0.15)
print("O novo salário com reajuste de 15% é: ", resultado)
# Fim