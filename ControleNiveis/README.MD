# Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/colorama-required-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen?style=flat-square)

Sistema executado no terminal que simula o monitoramento de um reservatório de água. A cada leitura, o programa exibe uma mensagem de alerta colorida de acordo com o nível registrado.

A simulação utiliza valores definidos no próprio código, sem entrada de dados do usuário.

## Sumário

- [Controle de Níveis de Água](#controle-de-níveis-de-água)
  - [Sumário](#sumário)
  - [Níveis e cores](#níveis-e-cores)
  - [Como o programa funciona](#como-o-programa-funciona)
    - [Estrutura do código](#estrutura-do-código)
    - [Fluxo de execução](#fluxo-de-execução)
  - [Como executar](#como-executar)
  - [Como alterar a simulação](#como-alterar-a-simulação)
  - [Tecnologias](#tecnologias)

## Níveis e cores

| Nível | Situação              | Cor      |
| :---: | --------------------- | -------- |
|   1   | Muito baixo (crítico) | Vermelho |
|   2   | Baixo                 | Amarelo  |
|   3   | Médio                 | Verde    |
|   4   | Alto                  | Ciano    |
|   5   | Muito alto (alerta)   | Azul     |

## Como o programa funciona

### Estrutura do código

| Elemento                 | Descrição                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Lista `mensagens`        | Armazena a mensagem de cada nível. O índice corresponde ao nível menos 1.                                       |
| `definir_cor(nivel)`     | Recebe o nível (1 a 5) e retorna a cor correspondente do `colorama`. Para níveis fora da faixa, retorna branco. |
| `exibir_situacao(nivel)` | Obtém a mensagem do nível, aplica a cor e imprime no terminal. Níveis inválidos geram um aviso.                 |
| `main()`                 | Executa a simulação sobre uma lista fixa de leituras: `[1, 2, 3, 4, 5, 3, 2]`.                                  |

### Fluxo de execução

1. O `colorama` é inicializado com `init()`, garantindo suporte a cores também no Windows.
2. O programa imprime o título do monitoramento.
3. Para cada leitura da lista, o programa:
   - exibe o número da leitura;
   - chama `exibir_situacao`, que obtém a cor com `definir_cor` e imprime a mensagem colorida.
4. Após cada mensagem, `Style.RESET_ALL` restaura o estilo padrão do terminal.
5. Ao final, o estilo é restaurado novamente e a mensagem "Fim da simulação." é exibida.

## Como executar

Instale a dependência:

```bash
pip install colorama
```

Execute o programa:

```bash
python controle_niveis_agua.py
```

## Como alterar a simulação

- Para testar outras situações, edite a lista `leituras` na função `main()`, usando valores de 1 a 5.
- Para alterar textos ou cores, ajuste a lista `mensagens` e a função `definir_cor`.

## Tecnologias

- [Python 3](https://www.python.org/)
- [colorama](https://pypi.org/project/colorama/)
