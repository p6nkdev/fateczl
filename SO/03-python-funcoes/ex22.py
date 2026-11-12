valor1 = 0
valor2 = 0


def entrada_dados():
    global valor1, valor2
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))


def mostrar_ordem_crescente():
    global valor1, valor2

    if valor1 < valor2:
        print(f"Ordem crescente: {valor1} {valor2}")
    else:
        print(f"Ordem crescente: {valor2} {valor1}")


def main():
    entrada_dados()
    mostrar_ordem_crescente()


if __name__ == "__main__":
    main()
