# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
# Variaveis
tempoPercurso: float = 0.0
velocidadeMedia: float = 0.0
distancia: float = 0.0
litrosGastos: float = 0.0

# Inicio
tempoPercurso = float(input("Digite o tempo de percurso em horas: "))
velocidadeMedia = float(input("Digite a velocidade média em km/h: "))
distancia = tempoPercurso * velocidadeMedia
litrosGastos = distancia / 12
print("A quantidade de litros gastos na viagem é: ", litrosGastos)
# Fim