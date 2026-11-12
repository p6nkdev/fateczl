nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0


def entrada_dados():
    global nota1, nota2, nota3, nota4
    nota1 = float(input("Digite a 1a nota: "))
    nota2 = float(input("Digite a 2a nota: "))
    nota3 = float(input("Digite a 3a nota: "))
    nota4 = float(input("Digite a 4a nota: "))


def calcular_media_e_situacao():
    global nota1, nota2, nota3, nota4
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Media aritmetica: {media:.2f}")

    if media >= 6.0:
        print("APROVADO")
    elif media >= 3.0:
        print("EXAME")
    else:
        print("RETIDO")


def main():
    entrada_dados()
    calcular_media_e_situacao()


if __name__ == "__main__":
    main()
