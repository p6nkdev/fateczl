import os

path = "C:\\temp"
nomeArquivo = "2.txt"

def writeInFile(fib, op):
    os.makedirs(path, exist_ok=True)
    
    entPath = os.path.join(path, nomeArquivo)

    with open(entPath, op) as f:
        f.write(f"{fib}\n")


def fibonacci(n):
    tempOne = 0
    tempTwo = 1
    for i in range(1,n+1):
        op = "w" if i == 1 else "a"
        fib = tempOne + tempTwo
        tempOne = tempTwo
        tempTwo = fib
        writeInFile(fib, op)

def main():
    n = int(input("Digite o número: "))
    print(n)

    fibonacci(n)

if __name__ == '__main__':
    main()