
from colorama import Fore, Style, init

# Inicializa o colorama (necessário principalmente no Windows)
init()

# Lista com as mensagens de cada nível (índice 0 = nível 1, ..., índice 4 = nível 5)
mensagens = [
    "Nível 1 - MUITO BAIXO (CRÍTICO): reservatório quase vazio!",
    "Nível 2 - BAIXO: atenção, o nível está abaixo do ideal.",
    "Nível 3 - MÉDIO: reservatório em condição normal.",
    "Nível 4 - ALTO: nível elevado, mantenha o monitoramento.",
    "Nível 5 - MUITO ALTO (ALERTA): risco de transbordamento!",
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado (1 a 5)."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE  # nível inválido


def exibir_situacao(nivel):
    """Exibe no terminal a mensagem do nível com a cor correspondente."""
    if 1 <= nivel <= len(mensagens):
        cor = definir_cor(nivel)
        print(cor + mensagens[nivel - 1] + Style.RESET_ALL)
    else:
        print(Fore.WHITE + f"Nível {nivel} inválido!" + Style.RESET_ALL)


def main():
    print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

    # Simulação: leituras definidas no código
    leituras = [1, 2, 3, 4, 5, 3, 2]

    for numero, nivel in enumerate(leituras, start=1):
        print(f"Leitura {numero}:")
        exibir_situacao(nivel)
        print()

    # Restaura o estilo padrão do terminal ao final
    print(Style.RESET_ALL + "Fim da simulação.")


if __name__ == "__main__":
    main()