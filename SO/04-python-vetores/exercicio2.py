def main():
    vetor: int = [0] * 100
    soma: int = 0
    maior: int = 0
    menor: int = 0
    media: float = 0.0
    i: int = 0

    for i in range(100):
        vetor[i] = int(input(f'Digite o {i + 1}o valor inteiro: '))

    maior = vetor[0]
    menor = vetor[0]

    for i in range(100):
        if vetor[i] > maior:
            maior = vetor[i]

        if vetor[i] < menor:
            menor = vetor[i]

        soma += vetor[i]

    media = soma / len(vetor)

    print(f'Maior valor = {maior}')
    print(f'Menor valor = {menor}')
    print(f'Media dos valores = {media:.2f}')


if __name__ == '__main__':
    main()
