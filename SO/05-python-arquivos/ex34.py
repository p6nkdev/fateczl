import os

valor: int = 0
dir: str = ""
arq: str = ""


def garantir_diretorio() -> None:
    global dir
    dir = "/tmp/exercicios"

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    os.chmod(dir, 0o744)


def mult(vlr: int, tab: int) -> int:
    res: int = vlr * tab
    return res


def grava(c: int, rslt: int) -> None:
    global dir, arq

    dir = "/tmp/exercicios"
    arq = "ex34.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    linha = str(rslt) + "\n"

    if os.path.exists(dir) and os.path.isdir(dir):
        file = os.path.join(dir, arq)
        tipo = "w"

        if os.path.exists(file) and c > 0:
            tipo = "a"

        enc = "utf-8"
        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha)


def main() -> None:
    global valor

    garantir_diretorio()

    contador: int = 0
    result: int = 0

    valor = int(input("Digite um valor entre 1 e 10: "))

    while valor < 1 or valor > 10:
        valor = int(input("Valor invalido. Digite um valor entre 1 e 10: "))

    for contador in range(10):
        result = mult(valor, contador)
        grava(contador, result)


if __name__ == "__main__":
    main()
