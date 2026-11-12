import os

path = "C:\\temp"
nomeArquivo = "1.txt"

def writeInFile(quad, op):
    os.makedirs(path, exist_ok=True)
    
    entPath = os.path.join(path, nomeArquivo)

    with open(entPath, op) as f:
        f.write(f"{quad}\n")


def quadrados():
    for i in range(10,150):
        op = "w" if i == 10 else "a"
        quad = i ** 2
        writeInFile(quad, op)

def main():
    quadrados()

if __name__ == '__main__':
    main()
