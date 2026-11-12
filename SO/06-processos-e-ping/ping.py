import platform
import subprocess


def os():
    system: str = ''
    system = platform.system()
    return system


def media_ping():
    nome_os: str = ''
    comando: list[str] = []
    saida: subprocess.CompletedProcess
    linhas: list[str] = []
    ultima_linha: str = ''
    partes: list[str] = []
    media: str = ''

    nome_os = os()

    if nome_os == 'Windows':
        comando = ['ping', '-4', '-n', '10', 'www.google.com.br']
    else:
        comando = ['ping', '-4', '-c', '10', 'www.google.com.br']

    saida = subprocess.run(comando, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    linhas = saida.stdout.splitlines()

    for linha in linhas:
        if linha.strip() != '':
            ultima_linha = linha.strip()

    if nome_os == 'Windows':
        partes = ultima_linha.split(',')
        for parte in partes:
            if 'M' in parte or 'A' in parte:
                media = parte.split('=')[1].strip()
                print(f'Media = {media}')
                return
    else:
        partes = ultima_linha.split('=')
        if len(partes) > 1:
            media = partes[1].strip().split('/')[1].strip()
            print(f'avg = {media} ms')
            return

    print('Nao foi possivel identificar a media do ping.')


def main():
    media_ping()


if __name__ == '__main__':
    main()
