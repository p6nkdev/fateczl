valor = 0


def entrada_dados():
    global valor
    valor = int(input("Digite um valor inteiro: "))


def verificar_divisibilidade():
    global valor

    if valor % 2 == 0 and valor % 3 == 0:
        print(f"{valor} e divisivel por 2 e por 3.")
    else:
        print(f"{valor} nao e divisivel por 2 e por 3 ao mesmo tempo.")


def main():
    entrada_dados()
    verificar_divisibilidade()


if __name__ == "__main__":
    main()
