#!/usr/local/bin/python3

# AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# TÍTULO     : Maior número primo em um intervalo
"""
Encontra o maior número primo dentro do intervalo [2, limite] informado
pelo usuário.

Estratégia: percorre o intervalo de trás para frente e retorna o primeiro
primo encontrado, evitando varrer a lista inteira desnecessariamente.

Exemplo: limite = 20 → maior primo = 19
"""

import math


def is_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo com complexidade O(√n).

    Parâmetros:
        numero (int): Número inteiro a ser verificado.

    Retorna:
        bool: True se primo, False caso contrário.

    Exemplos:
        >>> is_primo(17)
        True
        >>> is_primo(18)
        False
    """
    # Números menores que 2 não são primos por definição
    if numero < 2:
        return False

    # 2 é o único primo par
    if numero == 2:
        return True

    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False

    # Testa divisores ímpares de 3 até √numero.
    # Basta ir até √numero: se numero = a × b e a > √n,
    # então b < √n já teria sido encontrado antes.
    for fator in range(3, math.isqrt(numero) + 1, 2):
        if numero % fator == 0:
            return False

    return True


def maior_primo(limite: int) -> int | None:
    """
    Retorna o maior número primo no intervalo [2, limite].

    Percorre o intervalo de trás para frente e retorna o primeiro primo
    encontrado, o que é mais eficiente do que varrer toda a lista e
    guardar o maior — o último primo encontrado de baixo para cima já
    seria o maior, mas a busca reversa permite parar mais cedo.

    Parâmetros:
        limite (int): Valor máximo do intervalo de busca (deve ser ≥ 2).

    Retorna:
        int  : O maior primo encontrado no intervalo.
        None : Se não houver nenhum primo no intervalo (limite < 2).

    Exemplos:
        >>> maior_primo(20)
        19
        >>> maior_primo(10)
        7
    """
    # Percorre do limite até 2 em ordem decrescente
    for numero in range(limite, 1, -1):
        if is_primo(numero):
            return numero  # primeiro primo encontrado já é o maior

    # Nenhum primo encontrado no intervalo
    return None


def coletar_limite(mensagem: str) -> int:
    """
    Solicita ao usuário um inteiro ≥ 2, repetindo até entrada válida.

    Parâmetros:
        mensagem (str): Texto exibido no prompt.

    Retorna:
        int: Valor inteiro ≥ 2 informado pelo usuário.
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
    print("=== MAIOR NÚMERO PRIMO EM UM INTERVALO ===\n")

    # Coleta o limite máximo com validação de entrada
    limite = coletar_limite("Digite o limite máximo (≥ 2): ")

    # Busca o maior primo no intervalo [2, limite]
    resultado = maior_primo(limite)

    # Exibe o resultado de forma descritiva
    if resultado:
        print(f"\nO maior número primo no intervalo [2, {limite}] é: {resultado}")
    else:
        print(f"\nNenhum número primo encontrado no intervalo [2, {limite}].")