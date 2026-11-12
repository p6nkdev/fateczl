<div align="center">

# 🐧 Sistemas Operacionais

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Exercícios da disciplina de Sistemas Operacionais, todos em Python.
Começa na lógica de programação e chega em arquivos, processos, threads e semáforos.

</div>

---

## 📂 Estrutura

| # | Pasta | Assunto |
|:-:|-------|---------|
| 01 | [python-sequencial](01-python-sequencial/) | Entrada, cálculo e saída |
| 02 | [python-condicionais-e-repeticao](02-python-condicionais-e-repeticao/) | `if/elif/else`, `for` e `while` |
| 03 | [python-funcoes](03-python-funcoes/) | Exercícios refeitos com funções e `main()` |
| 04 | [python-vetores](04-python-vetores/) | Listas/vetores |
| 05 | [python-arquivos](05-python-arquivos/) | Leitura e escrita de arquivos |
| 06 | [processos-e-ping](06-processos-e-ping/) | Comandos do sistema com `subprocess` |
| 07 | [threads](07-threads/) | Concorrência com `threading` |
| 08 | [semaforos](08-semaforos/) | Sincronização com semáforos e `multiprocessing` |

---

## 📝 Exercícios

<details>
<summary><b>01 · Sequencial</b> (exercícios 1 a 17)</summary>

<br>

Áreas (quadrado, triângulo), reajuste de salário, conversão Celsius → Fahrenheit, Bhaskara, troca de valores, volume do paralelepípedo, poupança, soma dos quadrados, comprimento da circunferência, idade, hipotenusa, salário líquido com dependentes e consumo de combustível.

</details>

<details>
<summary><b>02 · Condicionais e repetição</b> (exercícios 18 a 45)</summary>

<br>

| Exercícios | Assunto |
|------------|---------|
| 18 a 29 | Condicionais: maior valor, Bhaskara, média do aluno, ordenação, divisibilidade, duração de jogo, múltiplos, velocidade média, novo preço, investimento |
| 31 a 45 | Repetição: quadrados, fatorial, série harmônica, tabuada, soma de ímpares, Fibonacci, maior/menor, grãos no xadrez, primos, dados, séries, potência |

</details>

<details>
<summary><b>03 · Funções</b> (ex18 a ex29)</summary>

<br>

Os mesmos exercícios 18 a 29, reescritos com funções separadas e `main()`.

</details>

<details>
<summary><b>04 · Vetores</b></summary>

<br>

| Arquivo | O que faz |
|---------|-----------|
| `exercicio1.py` | 50 valores: média dos que estão entre 10 e 200 e soma dos ímpares |
| `exercicio2.py` | 100 valores: maior, menor e média |
| `exercicio4.py` | 30 notas: média do grupo, quantas ficaram acima e as posições abaixo da média |

</details>

<details>
<summary><b>05 · Arquivos</b></summary>

<br>

| Arquivo | O que faz |
|---------|-----------|
| `arquivos1.py` | Grava os quadrados de 10 a 149 em `C:\temp\1.txt` |
| `arquivos2.py` | Grava os N primeiros termos de Fibonacci em `C:\temp\2.txt` |
| `arquivos3.py` | Lê o arquivo do exercício 2 e mostra só os ímpares |
| `ex27.py` | Média de 4 notas gravada em arquivo |
| `ex34.py` | Tabuada gravada em arquivo |
| `exercicio_36.py` | Série com fatorial, gravando cada termo em arquivo |
| `exercicio_38.py` | Lê valores positivos, grava em arquivo e depois mostra o maior e o menor |

</details>

<details>
<summary><b>06 · Processos e ping</b></summary>

<br>

| Arquivo | O que faz |
|---------|-----------|
| `ping.py` | Executa `ping` 10 vezes no Google e mostra o tempo médio (Windows e Linux) |
| `processos.py` | Lista processos (`TASKLIST` / `ps -ef`) e mata processo por PID ou nome (`TASKKILL` / `kill`) |

</details>

<details>
<summary><b>07 · Threads</b></summary>

<br>

| Arquivo | O que faz |
|---------|-----------|
| `Exercicio1.py` | Cria 5 threads que mostram o próprio ID |
| `Exercicio2.py` | Cada thread soma uma linha de valores aleatórios |
| `Exercicio3.py` | Corrida de sapos, cada sapo é uma thread |
| `Exercicio4.py` | Ping em vários servidores ao mesmo tempo |

</details>

<details>
<summary><b>08 · Semáforos</b></summary>

<br>

| Arquivo | O que faz |
|---------|-----------|
| `1.py` | Cruzamento: só um carro cruza por vez |
| `2.py` | Porta: as pessoas passam uma de cada vez |
| `3.py` | Corrida de sapos com ordem de chegada protegida por semáforo |
| `4.py` | Carros de escuderias disputando a pista |

</details>

---

## ▶️ Como executar

Precisa do Python 3.10 ou mais novo.

```bash
python 01-python-sequencial/1.py
```

> 💡 Os exercícios de arquivos gravam em `C:\temp` ou `/tmp/exercicios`, dependendo do exercício.
