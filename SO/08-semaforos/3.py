import multiprocessing
import random
import time

pos_cheg: int = 0
semaforo = None

def init(cheg, s):
    global pos_cheg
    global semaforo
    pos_cheg = cheg
    semaforo = s

def sapo(id):
    global pos_cheg
    global semaforo

    dist: int = 0
    dist_total: int = 0
    salto_max: int = 0
    salto: int = 0
    tempo: float = 0.0

    dist_total = 50
    salto_max = 5
    tempo = 0.1

    while (dist < dist_total):
        salto = random.randint(1, salto_max)
        dist += salto
        time.sleep(tempo)
        print('Sapo #', id, 'saltou', salto, 'cm. e percorreu', dist, 'cm.')

    with semaforo:
        pos_cheg.value += 1
        print('Sapo #', id, 'chegou na', pos_cheg.value, 'a. posicao')

def main():
    j: int = 0
    params: int = [0]*5
    chegada: int = 0
    sem = None

    chegada = multiprocessing.Value('i', 0)

    for j in range(5):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=5, initializer=init, initargs=(chegada, sem)) as pool:
            pool.map(sapo, params)

if __name__ == '__main__':
    main()
