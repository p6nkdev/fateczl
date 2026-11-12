# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
# Variaveis
anoNascimento: int = 0
anoAtual: int = 0
idade: int = 0

# Inicio
anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNascimento
print("Sua idade é: ", idade)
print("Daqui a 17 anos você terá: ", idade + 17)
# Fim