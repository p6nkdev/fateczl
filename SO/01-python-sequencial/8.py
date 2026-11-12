# Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
# Variaveis
deposito: float = 0.0
valorFinal: float = 0.0

# Inicio
deposito = float(input("Digite o valor do depósito em poupança: "))
valorFinal = deposito + (deposito * 0.013)
print("O valor após 1 mês de aplicação é: ", valorFinal)
# Fim