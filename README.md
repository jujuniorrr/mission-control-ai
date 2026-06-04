# Mission Control AI

## Global Solution 2026.1 – Pensamento Computacional e Automação com Python

### Descrição do Projeto

O Mission Control AI é um sistema inteligente desenvolvido em Python para simular o monitoramento de uma missão espacial experimental.

O objetivo do sistema é acompanhar diferentes parâmetros operacionais da missão ao longo de diversos ciclos de monitoramento, identificando situações de atenção e risco, gerando alertas automáticos, calculando níveis de risco e produzindo um relatório final para auxiliar a tomada de decisão.

O projeto foi desenvolvido como parte da Global Solution 2026.1 da FIAP.

---

## Objetivos do Sistema

O sistema é capaz de:

* Monitorar dados simulados da missão espacial;
* Analisar temperatura, comunicação, bateria, oxigênio e estabilidade operacional;
* Classificar cada parâmetro como NORMAL, ATENÇÃO ou CRÍTICO;
* Calcular a pontuação de risco de cada ciclo;
* Classificar a situação geral da missão;
* Gerar recomendações automáticas;
* Identificar tendências de melhora ou piora;
* Determinar a área mais afetada durante a missão;
* Exibir um relatório final detalhado.

---

## Estrutura dos Dados

O sistema utiliza uma matriz chamada `dados_missao`, onde cada linha representa um ciclo de monitoramento.

Exemplo:

```python
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]
```

Cada coluna representa:

| Posição | Informação   |
| ------- | ------------ |
| 0       | Temperatura  |
| 1       | Comunicação  |
| 2       | Bateria      |
| 3       | Oxigênio     |
| 4       | Estabilidade |

---

## Áreas Monitoradas

O sistema monitora as seguintes áreas:

* Temperatura interna
* Comunicação com a base
* Sistema de energia
* Suporte de oxigênio
* Estabilidade operacional

---

## Regras de Classificação

### Temperatura

| Condição          | Classificação |
| ----------------- | ------------- |
| Menor que 18°C    | ATENÇÃO       |
| Entre 18°C e 30°C | NORMAL        |
| Entre 31°C e 35°C | ATENÇÃO       |
| Acima de 35°C     | CRÍTICO       |

### Comunicação

| Condição        | Classificação |
| --------------- | ------------- |
| Menor que 30%   | CRÍTICO       |
| Entre 30% e 59% | ATENÇÃO       |
| 60% ou mais     | NORMAL        |

### Bateria

| Condição        | Classificação |
| --------------- | ------------- |
| Menor que 20%   | CRÍTICO       |
| Entre 20% e 49% | ATENÇÃO       |
| 50% ou mais     | NORMAL        |

### Oxigênio

| Condição        | Classificação |
| --------------- | ------------- |
| Menor que 80%   | CRÍTICO       |
| Entre 80% e 89% | ATENÇÃO       |
| 90% ou mais     | NORMAL        |

### Estabilidade

| Condição        | Classificação |
| --------------- | ------------- |
| Menor que 40%   | CRÍTICO       |
| Entre 40% e 69% | ATENÇÃO       |
| 70% ou mais     | NORMAL        |

---

## Estrutura do Projeto

```text
mission-control-ai/
│
├── README.md
├── mission_control.py
├── sistema_funcionando.png

```

---

## Tecnologias Utilizadas

* Python 3
* PyCharm
* GitHub

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/jujuniorrr/mission-control-ai.git
```

2. Acesse a pasta do projeto:

```bash
cd mission-control-ai
```

3. Execute o programa:

```bash
python mission_control.py
```

---

## Exemplo de Execução

O sistema analisa os ciclos da missão, calcula o risco operacional e gera um relatório final automático.

### Relatório Final
A imagem abaixo demonstra a execução do sistema e a geração automática do relatório final da missão.

![](sistema_funcionando.png)

---

## Funcionalidades Implementadas

* Matriz de monitoramento da missão
* Análise automática dos parâmetros
* Cálculo de risco por ciclo
* Classificação dos ciclos
* Recomendações automáticas
* Identificação da área mais afetada
* Análise de tendência da missão
* Relatório final completo

---

## Integrantes

### Roberson Reguero Luiz Junior

### Matheus Martins Lacerda

---

## Global Solution 2026.1

FIAP – Faculdade de Informática e Administração Paulista

Projeto desenvolvido para a disciplina de Pensamento Computacional e Automação com Python.

