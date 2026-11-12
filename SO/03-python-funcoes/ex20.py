import math


a = 0.0
b = 0.0
c = 0.0


def entrada_dados():
    global a, b, c
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))


def verificar_e_calcular_raizes():
    global a, b, c

    if a == 0:
        print("Nao e equacao do 2o grau, pois A deve ser diferente de zero.")
        return

    delta = b ** 2 - 4 * a * c
    print(f"Delta: {delta}")

    if delta < 0:
        print("Nao existem raizes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print("Existe uma raiz real.")
        print(f"Raiz: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Existem duas raizes reais.")
        print(f"Raiz 1: {raiz1}")
        print(f"Raiz 2: {raiz2}")


def main():
    entrada_dados()
    verificar_e_calcular_raizes()


if __name__ == "__main__":
    main()
