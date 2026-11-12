def calcular_fatorial(numero):
    fatorial = 1

    for contador in range(2, numero + 1):
        fatorial *= contador

    return fatorial


def calcular_divisao(numerador, denominador):
    return numerador / denominador


def gravar_termos_e_resultado(nome_arquivo, quantidade_termos):
    soma = 1.0

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("Termo 0: 1\n")

        for numero in range(1, quantidade_termos + 1):
            fatorial = calcular_fatorial(numero)
            termo = calcular_divisao(1, fatorial)
            soma += termo
            arquivo.write(f"Termo {numero}: 1/{numero}! = {termo}\n")

        arquivo.write(f"Resultado final: {soma}\n")

    return soma


def main():
    entrada = input("Digite um numero N: ").strip()

    try:
        numero = int(entrada)
    except ValueError:
        print("Digite um numero inteiro valido.")
        return

    if numero < 0:
        print("Digite um numero inteiro maior ou igual a zero.")
        return

    arquivo_saida = "serie_exercicio_36.txt"
    resultado = gravar_termos_e_resultado(arquivo_saida, numero)

    print(f"Arquivo gerado: {arquivo_saida}")
    print(f"Resultado da serie: {resultado}")


if __name__ == "__main__":
    main()
