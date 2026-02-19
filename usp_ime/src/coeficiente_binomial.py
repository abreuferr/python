#!/usr/local/bin/python3

# AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# TÍTULO     : Coeficiente Binomial (Combinação de n, k)
"""
Calcula o coeficiente binomial C(n, k), também chamado de "n escolhe k".

Representa o número de maneiras de escolher k elementos de um conjunto
de n elementos, sem repetição e sem importar a ordem.

Fórmula:
    C(n, k) = n! / (k! × (n-k)!)

Restrições:
    - n e k devem ser inteiros não negativos
    - k deve ser menor ou igual a n

Exemplos:
    C(5, 2) = 5! / (2! × 3!) = 10   (grupos de 2 em 5 elementos)
    C(6, 0) = 1                       (há apenas 1 forma de não escolher nada)
    C(6, 6) = 1                       (há apenas 1 forma de escolher tudo)
"""

import math


# ── Funções ──────────────────────────────────────────────────────────────────

def coeficiente_binomial(n: int, k: int) -> int:
    """
    Calcula C(n, k) = n! / (k! × (n-k)!) usando math.comb.

    `math.comb` (disponível desde Python 3.8) é implementado em C,
    trabalha com inteiros exatos (sem arredondamentos de ponto flutuante)
    e é mais eficiente do que calcular três fatoriais separadamente.

    Parâmetros:
        n (int): Tamanho total do conjunto (n ≥ 0).
        k (int): Tamanho do subconjunto escolhido (0 ≤ k ≤ n).

    Retorna:
        int: Valor exato do coeficiente binomial C(n, k).

    Lança:
        ValueError: Se n < 0 ou k < 0 ou k > n.

    Exemplos:
        >>> coeficiente_binomial(5, 2)
        10
        >>> coeficiente_binomial(6, 0)
        1
    """
    if n < 0 or k < 0:
        raise ValueError(f"n e k devem ser não negativos. Recebido: n={n}, k={k}.")
    if k > n:
        raise ValueError(f"k deve ser ≤ n. Recebido: n={n}, k={k}.")

    # math.comb calcula o coeficiente binomial de forma exata e eficiente
    return math.comb(n, k)


def coletar_inteiro_nao_negativo(mensagem: str) -> int:
    """
    Solicita ao usuário um número inteiro não negativo, repetindo até entrada válida.

    Parâmetros:
        mensagem (str): Texto exibido no prompt de entrada.

    Retorna:
        int: Valor inteiro ≥ 0 informado pelo usuário.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("  O valor deve ser não negativo (≥ 0). Tente novamente.\n")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida. Digite apenas números inteiros.\n")


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== COEFICIENTE BINOMIAL ===")
    print("    C(n, k) = n! / (k! × (n-k)!)\n")

    # Coleta os valores de n e k com validação
    n = coletar_inteiro_nao_negativo("Valor de n: ")

    while True:
        k = coletar_inteiro_nao_negativo("Valor de k: ")
        if k <= n:
            break
        print(f"  k deve ser menor ou igual a n ({n}). Tente novamente.\n")

    # Calcula e exibe o resultado
    try:
        resultado = coeficiente_binomial(n, k)
        print(f"\nC({n}, {k}) = {n}! / ({k}! × {n - k}!) = {resultado}")
    except ValueError as erro:
        print(f"\nErro: {erro}")