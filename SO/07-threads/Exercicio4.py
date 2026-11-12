import platform
import re
import subprocess
import threading


def obter_comando_ping(servidor):
    sistema = platform.system().lower()

    if sistema == "windows":
        return ["ping", "-4", "-n", "10", servidor]

    if sistema == "linux":
        return ["ping", "-4", "-c", "10", servidor]

    return None


def extrair_tempo(linha):
    padrao = re.search(r"time[=<]?\s*(\d+(?:[.,]\d+)?)\s*ms", linha, re.IGNORECASE)

    if padrao is None:
        padrao = re.search(r"tempo[=<]?\s*(\d+(?:[.,]\d+)?)\s*ms", linha, re.IGNORECASE)

    if padrao is None:
        return None

    return float(padrao.group(1).replace(",", "."))


def executar_ping(nome_servidor, endereco):
    comando = obter_comando_ping(endereco)

    if comando is None:
        print(f"{nome_servidor}: sistema operacional nao suportado.")
        return

    processo = subprocess.Popen(
        comando,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="ignore",
    )

    tempos = []

    for linha in processo.stdout:
        tempo = extrair_tempo(linha)

        if tempo is not None:
            tempos.append(tempo)
            print(f"{nome_servidor}: tempo = {tempo} ms")

    processo.wait()

    if tempos:
        media = sum(tempos) / len(tempos)
        print(f"{nome_servidor}: tempo medio = {media:.2f} ms")
    else:
        print(f"{nome_servidor}: nao foi possivel obter tempos do ping.")


def main():
    servidores = [
        ("UOL", "www.uol.com.br"),
        ("Terra", "www.terra.com.br"),
        ("Google", "www.google.com.br"),
    ]
    threads = []

    for nome_servidor, endereco in servidores:
        thread = threading.Thread(target=executar_ping, args=(nome_servidor, endereco))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
