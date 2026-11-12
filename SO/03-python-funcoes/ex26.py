maior_valor = 0
menor_valor = 0


def entrada_dados():
    global maior_valor, menor_valor
    valor1 = int(input("Digite o primeiro numero inteiro: "))
    valor2 = int(input("Digite o segundo numero inteiro: "))

    if valor1 > valor2:
        maior_valor = valor1
        menor_valor = valor2
    else:
        maior_valor = valor2
        menor_valor = valor1


def verificar_multiplo():
    global maior_valor, menor_valor

    if maior_valor % menor_valor == 0:
        print(f"{maior_valor} e multiplo de {menor_valor}.")
    else:
        print(f"{maior_valor} nao e multiplo de {menor_valor}.")


def main():
    entrada_dados()
    verificar_multiplo()


if __name__ == "__main__":
    main()
