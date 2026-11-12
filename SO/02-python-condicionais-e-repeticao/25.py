# 25. Duração do jogo

# Variáveis
h1: int = 0
m1: int = 0
h2: int = 0
m2: int = 0

# Início
h1, m1 = map(int, input("Início (HH MM): ").split())
h2, m2 = map(int, input("Fim (HH MM): ").split())

inicio = h1*60 + m1
fim = h2*60 + m2

if (fim < inicio):
    fim += 1440

duracao = fim - inicio

print("Duração:", duracao//60, "h", duracao%60, "min")

# Fim