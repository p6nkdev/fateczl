def ler_valores_positivos(quantidade):
    valores = []

    while len(valores) < quantidade:
        entrada = input(f"Digite o {len(valores) + 1}o valor positivo: ").strip()

        try:
            numero = int(float(entrada))
        except ValueError:
            print("Valor invalido. Digite um numero.")
            continue

        if numero <= 0:
            print("Digite apenas valores positivos.")
            continue

        valores.append(numero)

    return valores


def encontrar_maior_menor(valores):
    maior = max(valores)
    menor = min(valores)
    return maior, menor


def gravar_resultado_exercicio_38(nome_arquivo, valores, maior, menor):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for valor in valores:
            arquivo.write(f"{valor}\n")

        arquivo.write(f"Maior: {maior}\n")
        arquivo.write(f"Menor: {menor}\n")


def gravar_multiplos_de_5(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, "r", encoding="utf-8") as origem, open(
        arquivo_destino, "w", encoding="utf-8"
    ) as destino:
        for linha in origem:
            texto = linha.strip()

            if not texto:
                continue

            texto_minusculo = texto.lower()
            if "maior" in texto_minusculo or "menor" in texto_minusculo:
                continue

            try:
                numero = int(texto)
            except ValueError:
                continue

            if numero % 5 == 0:
                destino.write(f"{numero}\n")


def main():
    quantidade = 100
    arquivo_saida = "valores_exercicio_38.txt"
    arquivo_multiplos = "multiplos_de_5.txt"

    valores = ler_valores_positivos(quantidade)
    maior, menor = encontrar_maior_menor(valores)

    gravar_resultado_exercicio_38(arquivo_saida, valores, maior, menor)
    gravar_multiplos_de_5(arquivo_saida, arquivo_multiplos)

    print(f"Arquivo gerado: {arquivo_saida}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Arquivo com multiplos de 5 gerado: {arquivo_multiplos}")


if __name__ == "__main__":
    main()
