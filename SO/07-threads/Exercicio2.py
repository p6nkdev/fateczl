import random
import threading
import time


def somar_linha(linha_id, valores):
    soma = 0

    for valor in valores:
        soma += valor
        time.sleep(0.2)

    print(f"Linha {linha_id}: valores = {valores} | soma = {soma}")


def main():
    threads = []
    parametros = []

    for linha_id in range(3):
        valores = [random.randint(1, 100) for _ in range(5)]
        parametros.append((linha_id, valores))

    for linha_id, valores in parametros:
        thread = threading.Thread(target=somar_linha, args=(linha_id, valores))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
