import random
import threading
import time


DISTANCIA_MAXIMA = 30
SALTO_MAXIMO = 5
lock_chegada = threading.Lock()
ordem_chegada = []


def correr(sapo_id):
    distancia_percorrida = 0

    print(f"Sapo {sapo_id} largou na corrida.")

    while distancia_percorrida < DISTANCIA_MAXIMA:
        salto = random.randint(1, SALTO_MAXIMO)
        distancia_percorrida += salto

        if distancia_percorrida > DISTANCIA_MAXIMA:
            distancia_percorrida = DISTANCIA_MAXIMA

        print(
            f"Sapo {sapo_id} saltou {salto} cm e ja percorreu "
            f"{distancia_percorrida} cm."
        )
        time.sleep(0.1)

    with lock_chegada:
        ordem_chegada.append(sapo_id)
        posicao = len(ordem_chegada)

    print(f"Sapo {sapo_id} chegou em {posicao}o lugar!")


def main():
    threads = []

    print(
        f"Corrida iniciada! Distancia da prova: {DISTANCIA_MAXIMA} cm. "
        f"Salto maximo: {SALTO_MAXIMO} cm."
    )

    for i in range(1, 6):
        thread = threading.Thread(target=correr, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Ordem final de chegada: {ordem_chegada}")


if __name__ == "__main__":
    main()
