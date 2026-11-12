def calcular_velocidade_media(voltas, extensao_metros, tempo_minutos):
    distancia_km = (voltas * extensao_metros) / 1000
    tempo_horas = tempo_minutos / 60
    velocidade_media = distancia_km / tempo_horas
    print(f"Velocidade media: {velocidade_media:.2f} km/h")


def main():
    voltas = int(input("Digite o numero de voltas: "))
    extensao_metros = float(input("Digite a extensao do circuito em metros: "))
    tempo_minutos = float(input("Digite o tempo de duracao em minutos: "))
    calcular_velocidade_media(voltas, extensao_metros, tempo_minutos)


if __name__ == "__main__":
    main()
