valor1 = 0
valor2 = 0


def entrada_dados():
    global valor1, valor2
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))


def calcular_diferenca():
    global valor1, valor2
    maior = valor1
    menor = valor2

    if valor2 > valor1:
        maior = valor2
        menor = valor1

    print(f"Diferenca do maior pelo menor: {maior - menor}")


def main():
    entrada_dados()
    calcular_diferenca()


if __name__ == "__main__":
    main()
