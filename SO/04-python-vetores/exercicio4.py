def main():
    vetor: float = [0.0] * 30
    soma: float = 0.0
    media: float = 0.0
    acima_media: int = 0
    posicoes_abaixo: str = ''
    i: int = 0

    for i in range(30):
        vetor[i] = float(input(f'Digite a {i + 1}a nota: '))
        soma += vetor[i]

    media = soma / len(vetor)

    for i in range(30):
        if vetor[i] > media:
            acima_media += 1

        if vetor[i] < media:
            posicoes_abaixo += f'{i} '

    print(f'Media do grupo = {media:.2f}')
    print(f'Quantidade de notas acima da media = {acima_media}')
    if posicoes_abaixo != '':
        print(f'Posicoes abaixo da media = {posicoes_abaixo.strip()}')
    else:
        print('Posicoes abaixo da media = nenhuma')


if __name__ == '__main__':
    main()
