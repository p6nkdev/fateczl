def calcular_novo_preco(preco_atual, media_mensal):
    if media_mensal < 500 and preco_atual < 30:
        novo_preco = preco_atual * 1.10
    elif 500 <= media_mensal < 1000 and 30 <= preco_atual < 80:
        novo_preco = preco_atual * 1.15
    elif media_mensal >= 1000 and preco_atual >= 80:
        novo_preco = preco_atual * 0.95
    else:
        novo_preco = preco_atual

    print(f"Novo preco: R$ {novo_preco:.2f}")


def main():
    preco_atual = float(input("Digite o preco atual: "))
    media_mensal = float(input("Digite a media mensal de vendas: "))
    calcular_novo_preco(preco_atual, media_mensal)


if __name__ == "__main__":
    main()
