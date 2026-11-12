valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0


def entrada_dados():
    global valor1, valor2, valor3, valor4
    valor1 = int(input("Digite o 1o valor em ordem crescente: "))
    valor2 = int(input("Digite o 2o valor em ordem crescente: "))
    valor3 = int(input("Digite o 3o valor em ordem crescente: "))
    valor4 = int(input("Digite o 4o valor: "))


def mostrar_quatro_em_ordem():
    global valor1, valor2, valor3, valor4
    numeros = [valor1, valor2, valor3, valor4]
    numeros.sort()
    print("Valores em ordem crescente:")
    for numero in numeros:
        print(numero)


def main():
    entrada_dados()
    mostrar_quatro_em_ordem()


if __name__ == "__main__":
    main()
