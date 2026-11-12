hora_inicio = 0
minuto_inicio = 0
hora_fim = 0
minuto_fim = 0


def entrada_dados():
    global hora_inicio, minuto_inicio, hora_fim, minuto_fim
    hora_inicio = int(input("Digite a hora de inicio: "))
    minuto_inicio = int(input("Digite o minuto de inicio: "))
    hora_fim = int(input("Digite a hora de fim: "))
    minuto_fim = int(input("Digite o minuto de fim: "))


def calcular_tempo_jogo():
    global hora_inicio, minuto_inicio, hora_fim, minuto_fim

    inicio_total = hora_inicio * 60 + minuto_inicio
    fim_total = hora_fim * 60 + minuto_fim

    if fim_total <= inicio_total:
        fim_total += 24 * 60

    duracao = fim_total - inicio_total
    horas = duracao // 60
    minutos = duracao % 60

    print(f"Tempo de jogo: {horas} hora(s) e {minutos} minuto(s)")


def main():
    entrada_dados()
    calcular_tempo_jogo()


if __name__ == "__main__":
    main()
