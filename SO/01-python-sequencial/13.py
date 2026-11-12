# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
# Variaveis
quantidadeAlimento: float = 0.0
diasDuracao: float = 0.0

# Inicio
quantidadeAlimento = float(input("Digite a quantidade de alimento em quilos: "))
diasDuracao = (quantidadeAlimento * 1000) / 50
print("Esse alimento durará ", diasDuracao, " dias.")
# Fim