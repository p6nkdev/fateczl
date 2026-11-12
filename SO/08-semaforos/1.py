import multiprocessing
import random
import time

sentido: int = 0
semaforo = None

def init(sent, s):
    global sentido
    global semaforo
    sentido = sent
    semaforo = s

def carro(id):
    global sentido
    global semaforo

    carro_andando(id)
    with semaforo:
        sentido.value = id
        carro_cruzando(id)
    carro_saindo(id)

def carro_andando(id):
    dist: int = 0
    dist_total: int = 0
    desloc: int = 0
    tempo: float = 0.0

    desloc = random.randint(10, 30)
    tempo = 0.1
    dist_total = random.randint(100, 200)

    while (dist < dist_total):
        dist += desloc
        time.sleep(tempo)
        print('Carro #', id, 'percorreu', dist, 'm. antes do cruzamento')

def carro_cruzando(id):
    direcoes = [
        'Norte para Sul',
        'Sul para Norte',
        'Leste para Oeste',
        'Oeste para Leste'
    ]

    print('Carro #', id, 'esta passando no sentido', direcoes[id])
    time.sleep(random.randint(1000, 2000) / 1000)

def carro_saindo(id):
    print('Carro #', id, 'saiu do cruzamento')

def main():
    j: int = 0
    params: int = [0]*4
    sent = None
    sem = None

    sent = multiprocessing.Value('i', 0)

    for j in range(4):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sent, sem)) as pool:
            pool.map(carro, params)

if __name__ == '__main__':
    main()
