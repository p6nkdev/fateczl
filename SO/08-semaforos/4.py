import multiprocessing
import random
import time

semaforo_pista = None
semaforos_escuderia = None

def init(pista, escuderias):
    global semaforo_pista
    global semaforos_escuderia
    semaforo_pista = pista
    semaforos_escuderia = escuderias

def carro(id):
    global semaforo_pista
    global semaforos_escuderia

    escuderia: int = 0

    escuderia = id // 2

    print('Carro #', id, 'da escuderia', escuderia, 'aguardando liberacao')
    with semaforos_escuderia[escuderia]:
        with semaforo_pista:
            correr(id, escuderia)
    print('Carro #', id, 'da escuderia', escuderia, 'saiu da pista')

def correr(id, escuderia):
    volta: int = 0
    tempo_volta: float = 0.0
    melhor_volta: float = 0.0

    print('Carro #', id, 'da escuderia', escuderia, 'entrou na pista')

    for volta in range(1, 4):
        tempo_volta = random.randint(60000, 90000) / 1000
        if (volta == 1 or tempo_volta < melhor_volta):
            melhor_volta = tempo_volta
        time.sleep(0.1)
        print('Carro #', id, 'volta', volta, 'tempo:', tempo_volta, 's.')

    print('Carro #', id, 'melhor volta:', melhor_volta, 's.')

def main():
    j: int = 0
    params: int = [0]*14
    sem_pista = None
    sem_escuderias = None

    for j in range(14):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem_pista = manager.Semaphore(5)
        sem_escuderias = [manager.Semaphore(1) for j in range(7)]
        with multiprocessing.Pool(processes=14, initializer=init, initargs=(sem_pista, sem_escuderias)) as pool:
            pool.map(carro, params)

if __name__ == '__main__':
    main()
