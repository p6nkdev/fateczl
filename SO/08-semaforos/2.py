import multiprocessing
import random
import time

pos_cheg: int = 0
pos_saida: int = 0
semaforo = None

def init(cheg, sai, s):
    global pos_cheg
    global pos_saida
    global semaforo
    pos_cheg = cheg
    pos_saida = sai
    semaforo = s

def pessoa(id):
    global semaforo

    pessoa_andando(id)
    with semaforo:
        pessoa_cruzando_porta(id)
    pessoa_saindo(id)

def pessoa_andando(id):
    global pos_cheg

    dist: int = 0
    dist_total: int = 0
    velocidade: int = 0
    tempo: float = 0.0

    dist_total = 200
    tempo = 0.1

    while (dist < dist_total):
        velocidade = random.randint(4, 6)
        dist += velocidade
        time.sleep(tempo)
        print('Pessoa #', id, 'andou', dist, 'm. no corredor')

    pos_cheg.value += 1
    print('Pessoa #', id, 'foi a', pos_cheg.value, 'a. a chegar na porta')

def pessoa_cruzando_porta(id):
    global pos_saida

    tempo_porta: float = 0.0

    tempo_porta = random.randint(1, 2)
    print('Pessoa #', id, 'esta abrindo e cruzando a porta')
    time.sleep(tempo_porta)

    pos_saida.value += 1
    print('Pessoa #', id, 'foi a', pos_saida.value, 'a. a cruzar a porta')

def pessoa_saindo(id):
    print('Pessoa #', id, 'saiu pela porta')

def main():
    j: int = 0
    params: int = [0]*4
    chegada: int = 0
    saida: int = 0
    sem = None

    chegada = multiprocessing.Value('i', 0)
    saida = multiprocessing.Value('i', 0)

    for j in range(4):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(chegada, saida, sem)) as pool:
            pool.map(pessoa, params)

if __name__ == '__main__':
    main()
