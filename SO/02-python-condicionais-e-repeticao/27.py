# 27. Velocidade média

# Variáveis
voltas: int = 0
extensao: float = 0
tempo: float = 0
vel: float = 0

# Início
voltas = int(input())
extensao = float(input())
tempo = float(input())

dist = (voltas * extensao) / 1000
tempo_h = tempo / 60

vel = dist / tempo_h

print("Velocidade:", vel, "km/h")

# Fim