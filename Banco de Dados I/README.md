<div align="center">

# 🗄️ Banco de Dados I

![SQL](https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)

Material de estudo da disciplina de Banco de Dados I: da modelagem conceitual até consultas SQL com JOIN e subconsulta.

</div>

---

## 📂 Estrutura

| Arquivo / Pasta | O que é |
|-----------------|---------|
| [Estúdio Banco de Dados](Estúdio%20Banco%20de%20Dados/) | Página interativa para praticar modelagem e SQL no navegador |
| `Como_desenhar_os_modelos.pdf` | Guia de como desenhar os modelos (DER e lógico) |
| `Como_desenhar_os_modelos_A4.pdf` | O mesmo guia, formatado para imprimir em A4 |
| `Normalizacao.pdf` | Normalização: 1FN, 2FN e 3FN |
| `Revisao_Banco_de_Dados.pdf` | Revisão da matéria, com checklist final e pegadinhas |
| `Tarefas de Banco de Dados – Material de Estudo.pdf` | Tarefas da disciplina com checklist de entrega |

---

## 🧪 Estúdio de Banco de Dados

Uma página HTML que roda um banco SQLite direto no navegador ([sql.js](https://github.com/sql-js/sql.js)), sem instalar nada.

Ela é dividida em 8 etapas, cada uma com exercício, correção e gabarito:

| # | Etapa |
|:-:|-------|
| 1 | Níveis de modelagem |
| 2 | Modelo Entidade-Relacionamento (DER), com editor de diagrama |
| 3 | Modelo lógico (conversão do DER em tabelas) |
| 4 | Normalização (1FN, 2FN, 3FN) |
| 5 | SQL – DDL (criar a estrutura) |
| 6 | SQL – DML e consultas |
| 7 | JOINs |
| 8 | Subconsultas |

<details>
<summary><b>Diferença entre v1 e v2</b></summary>

<br>

- **v1:** usa os estudos de caso das listas do professor (livraria, concessionária...).
- **v2:** troca por estudos de caso novos (clínica veterinária, companhia aérea...) para treinar com enunciados que ainda não vi.

</details>

### ▶️ Como usar

Abra `Estúdio Banco de Dados/v2/index.html` no navegador. O arquivo `sql-asm.js` precisa ficar na mesma pasta.

> 💡 Os botões "com o Claude" (explicar, gerar exercício novo, comentar) só funcionam quando a página é aberta como Artifact no claude.ai. Fora dele, o resto da página funciona normalmente.
