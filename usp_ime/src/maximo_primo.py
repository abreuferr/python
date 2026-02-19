"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Números primos em um intervalo
SOBRE       : Exibe todos os números primos de 2 até um limite máximo informado pelo usuário.   
            Um número é primo se for maior que 1 e divisível apenas por 1 e por ele mesmo.
            Exemplo: limite = 20 → 2, 3, 5, 7, 11, 13, 17, 19
"""

import math


def is_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Utiliza a otimização de testar divisores apenas até √numero,
    reduzindo a complexidade de O(n) para O(√n).

    Parâmetros:
        numero (int): Número inteiro a ser verificado (deve ser ≥ 2).

    Retorna:
        bool: True se o número for primo, False caso contrário.

    Exemplos:
        >>> is_primo(7)
        True
        >>> is_primo(9)
        False
    """
    # Números menores que 2 não são primos por definição
    if numero < 2:
        return False

    # 2 é o único número primo par
    if numero == 2:
        return True

    # Números pares maiores que 2 nunca são primos
    if numero % 2 == 0:
        return False

    # Testa divisores ímpares de 3 até √numero.
    # Testar até √numero é suficiente: se numero = a × b e a > √n,
    # então b < √n já teria sido encontrado antes.
    for fator in range(3, math.isqrt(numero) + 1, 2):
        if numero % fator == 0:
            return False

    return True


def primos_ate(limite: int) -> list[int]:
    """
    Retorna uma lista com todos os números primos de 2 até `limite` (inclusive).

    Parâmetros:
        limite (int): Valor máximo do intervalo de busca.

    Retorna:
        list[int]: Lista de números primos encontrados no intervalo [2, limite].

    Exemplo:
        >>> primos_ate(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    # Filtra os números no intervalo [2, limite] que são primos
    return [n for n in range(2, limite + 1) if is_primo(n)]


def coletar_limite(mensagem: str) -> int:
    """
    Solicita ao usuário um número inteiro positivo, repetindo até entrada válida.

    Parâmetros:
        mensagem (str): Texto exibido no prompt de entrada.

    Retorna:
        int: Valor inteiro positivo informado pelo usuário.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 2:
                print("  O limite deve ser maior ou igual a 2. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida. Digite apenas números inteiros.")


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== NÚMEROS PRIMOS ATÉ UM LIMITE ===\n")

    # Coleta o limite máximo com validação
    limite = coletar_limite("Digite o limite máximo: ")

    # Obtém a lista de primos no intervalo
    lista_primos = primos_ate(limite)

    # Exibe os resultados de forma descritiva
    print(f"\nPrimos de 2 até {limite} ({len(lista_primos)} encontrados):")
    print(", ".join(str(p) for p in lista_primos))