def calcular_investimento_corrigido(tipo, valor):
    if tipo == 1:
        valor_corrigido = valor * 1.03
        print(f"Valor corrigido na poupanca: R$ {valor_corrigido:.2f}")
    elif tipo == 2:
        valor_corrigido = valor * 1.05
        print(f"Valor corrigido na renda fixa: R$ {valor_corrigido:.2f}")
    else:
        print("Tipo de investimento invalido.")


def main():
    tipo = int(input("Digite o tipo de investimento (1 = poupanca, 2 = renda fixa): "))
    valor = float(input("Digite o valor do investimento: "))
    calcular_investimento_corrigido(tipo, valor)


if __name__ == "__main__":
    main()
