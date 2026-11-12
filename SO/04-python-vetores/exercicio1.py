def main():
    vetor: int = [0] * 50
    soma_intervalo: int = 0
    quantidade_intervalo: int = 0
    soma_impares: int = 0
    media_intervalo: float = 0.0
    i: int = 0
    valor: int = 0

    for i in range(50):
        vetor[i] = int(input(f'Digite o {i + 1}o valor inteiro: '))

    for i in range(50):
        valor = vetor[i]
        if 10 <= valor <= 200:
            soma_intervalo += valor
            quantidade_intervalo += 1

        if valor % 2 != 0:
            soma_impares += valor

    if quantidade_intervalo > 0:
        media_intervalo = soma_intervalo / quantidade_intervalo

    print(f'Media dos valores entre 10 e 200 = {media_intervalo:.2f}')
    print(f'Soma dos numeros impares = {soma_impares}')


if __name__ == '__main__':
    main()
