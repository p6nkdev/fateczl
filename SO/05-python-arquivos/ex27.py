import os

nome: str = ""
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ""
arq: str = ""


def garantir_diretorio() -> None:
    global dir
    dir = "/tmp/exercicios"

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    os.chmod(dir, 0o744)


def med(n1: float, n2: float, n3: float, n4: float) -> float:
    media: float = (n1 + n2 + n3 + n4) / 4
    return media


def escreveArq(caminho: str, arquivo: str, linha_cad: str) -> None:
    file: str = ""
    tipo: str = ""
    enc: str = ""

    if os.path.exists(caminho) and os.path.isdir(caminho):
        file = os.path.join(caminho, arquivo)
        tipo = "w"

        if os.path.exists(file):
            tipo = "a"

        enc = "utf-8"
        with open(file, tipo, encoding=enc) as arq_file:
            arq_file.write(linha_cad)


def cadastro(
    nm: str,
    nt1: float,
    nt2: float,
    nt3: float,
    nt4: float,
    vlr_med: float,
) -> None:
    global dir, arq

    dir = "/tmp/exercicios"
    arq = "ex21.txt"

    linha: str = (
        nm
        + ";"
        + str(nt1)
        + ";"
        + str(nt2)
        + ";"
        + str(nt3)
        + ";"
        + str(nt4)
        + ";"
        + str(vlr_med)
        + "\n"
    )

    escreveArq(dir, arq, linha)


def entrada() -> None:
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    valor_media = med(nota1, nota2, nota3, nota4)
    print(f"Media: {valor_media:.2f}")

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def main() -> None:
    garantir_diretorio()

    contador: int = 0

    for contador in range(5):
        entrada()


if __name__ == "__main__":
    main()
