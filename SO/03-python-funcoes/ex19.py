valor1 = 0.0
valor2 = 0.0


def entrada_dados():
    global valor1, valor2
    valor1 = float(input("Digite o primeiro valor real: "))
    valor2 = float(input("Digite o segundo valor real: "))


def mostrar_maior():
    global valor1, valor2

    if valor1 > valor2:
        print(f"Maior valor: {valor1}")
    elif valor2 > valor1:
        print(f"Maior valor: {valor2}")
    else:
        print(f"Os valores sao iguais: {valor1}")


def main():
    entrada_dados()
    mostrar_maior()


if __name__ == "__main__":
    main()
