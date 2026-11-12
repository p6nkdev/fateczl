import os

path = "C:\\temp"
nomeArquivo = "2.txt"

def isOdd(num):
    if (num % 2 != 0):
        return num
    else:
        return -1

def verificarValores():
    os.makedirs(path, exist_ok=True)
    
    entPath = os.path.join(path, nomeArquivo)

    if os.path.exists(entPath):
        with open(entPath, "r") as f:
            for line in f:
                num = int(line.strip())

                isNumOdd = isOdd(num)

                if (isNumOdd != -1):
                    print(num)
                
def main():
    verificarValores()

if __name__ == '__main__':
    main()