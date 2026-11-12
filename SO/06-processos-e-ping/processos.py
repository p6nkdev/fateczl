import platform
import subprocess


def os():
    system: str = ''
    system = platform.system()
    return system


def proc(opcao, parametro=''):
    nome_os: str = ''
    comando: list[str] = []
    saida: subprocess.CompletedProcess

    nome_os = os()

    if opcao == 1:
        if nome_os == 'Windows':
            comando = ['TASKLIST', '/FO', 'TABLE']
        else:
            comando = ['ps', '-ef']
    elif opcao == 2:
        if nome_os == 'Windows':
            comando = ['TASKKILL', '/PID', str(parametro), '/F']
        else:
            comando = ['kill', '-9', str(parametro)]
    elif opcao == 3:
        if nome_os == 'Windows':
            comando = ['TASKKILL', '/IM', str(parametro), '/F']
        else:
            comando = ['pkill', '-f', str(parametro)]
    else:
        print('Opcao invalida.')
        return

    saida = subprocess.run(comando, capture_output=True, text=True, encoding='utf-8', errors='ignore')

    if saida.stdout.strip() != '':
        print(saida.stdout)

    if saida.stderr.strip() != '':
        print(saida.stderr)


def main():
    opcao: int = 0
    pid: str = ''
    nome_processo: str = ''

    while opcao != 9:
        print('1 - Listar processos ativos')
        print('2 - Matar processo por PID')
        print('3 - Matar processo por nome')
        print('9 - Encerrar')
        opcao = int(input('Escolha uma opcao: '))

        if opcao == 1:
            proc(1)
        elif opcao == 2:
            pid = input('Digite o PID do processo: ')
            proc(2, pid)
        elif opcao == 3:
            nome_processo = input('Digite o nome do processo: ')
            proc(3, nome_processo)
        elif opcao == 9:
            print('Aplicacao encerrada.')
        else:
            print('Opcao invalida.')


if __name__ == '__main__':
    main()
